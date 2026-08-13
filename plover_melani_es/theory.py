"""Taken basically wholesale from https://github.com/opensteno/plover_melani/blob/master/plover_melani/theory.py"""

import json
import os

from pkg_resources import resource_stream

from plover.oslayer.config import CONFIG_DIR
from plover_stroke import BaseStroke

from plover_melani import system


class Stroke(BaseStroke):
    """Wrapper for `plover_stroke.BaseStroke`"""
    pass

Stroke.setup(system.KEYS, system.IMPLICIT_HYPHEN_KEYS,
             system.NUMBER_KEY, system.NUMBERS)


META_ATTACH = '{^}' # Plover's symbol for concatenating strings rather than inputting an automatic space.

class Theory:

    def __init__(self, fragments=None):
        self._combos = {}
        self._max_combos_len = 0
        self._word_parts = {}
        self._max_word_part_len = 0

        # `fragments`` is a dictionary mapping steno combos to translations.
        if fragments is None:
            fragments_filename = os.path.join(CONFIG_DIR, 'melani_es_mapping.json')
            if os.path.exists(fragments_filename):
                with open(fragments_filename, 'rb') as fp:
                    fragments = json.loads(fp.read().decode('utf-8'))
            else:
                with resource_stream('plover_melani', 'dictionaries/melani_es_mapping.json') as fp:
                    fragments = json.loads(fp.read().decode('utf-8'))

        # Assign values to `self._combos` (dict) and `self._max_combos_len` (int).
        # `_combos` is a dictionary of type {Stroke:string}, where the strings
        # are Plover translation language.
        for steno, translation in fragments.items():
            stroke = Stroke.from_steno(steno)
            assert stroke not in self._combos
            self._combos[stroke] = translation
            self._max_combos_len = max(len(combo) for combo in self._combos) if self._combos else 0

        # Normalizes translation strings in `_combos` to make them more similar to final form.
        for combo, part in self._combos.items():
            if part.endswith(META_ATTACH):
                part = part[:-3]
            else:
                part = part + ' '
            if part in self._word_parts:
                self._word_parts[part] += (combo,)
            else:
                self._word_parts[part] = (combo,)

        # I'm pretty sure this is only used in reverse lookup. Initial inside comments in original.
        for part, combo_list in self._word_parts.items():
        # We want left combos to be given priority over right ones,
        # e.g. 'R-' over '-R' for 'r'.
            self._word_parts[part] = sorted(combo_list)
            if self._word_parts:
                self._max_word_part_len = max(len(part) for part in self._word_parts)
            else:
                self._max_word_part_len = 0

    def translate_stroke(self, stroke):
        """Converts a single stroke into its semi-final text form 
        (passed into `strokes_to_text`)."""
        if not self._combos:
            raise KeyError
        keys = list(stroke.keys())
        text = ''
        while keys:
            combo = Stroke(keys[0:self._max_combos_len])
            while combo:
                if combo in self._combos:
                    part = self._combos[combo]
                    text += part
                    break
                combo -= combo.last()
            if not combo:
                raise KeyError
            keys = keys[len(combo):]
        attach_start = text.startswith(META_ATTACH)
        attach_end = text.endswith(META_ATTACH)
        text = text.replace(META_ATTACH, '')
        if attach_start:
            text = META_ATTACH + text
        if attach_end:
            text = text + META_ATTACH
        return text

    def strokes_to_text(self, stroke_list):
        """Converts a series of strokes into final text."""
        text = ''
        attach_next = True
        for s in stroke_list:
            part = self.translate_stroke(s)
            if not attach_next and not part.startswith(META_ATTACH):
                text += ' '
            attach_next = part.endswith(META_ATTACH)
            text += part.replace(META_ATTACH, '')
        if not attach_next:
            text += ' '
        return text