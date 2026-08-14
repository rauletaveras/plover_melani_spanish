from plover_melani.theory import Stroke, Theory


theory = Theory()

# Required interface for Plover "Python" dictionary. {{{


# From the API: The maximum number of strokes that this dictionary can translate. 
# Plover uses this value to optimize dictionary lookups 
# by only using this dictionary when looking up outlines this length or shorter.
LONGEST_KEY = 1 

def lookup(key):
    """
    From API reference for `key` (`outline: Tuple[str]`): 
    Given an outline which is a tuple of steno strokes, returns the translation for this outline, 
    or raises a KeyError when no translation is available. 
    The translation should be in Plover’s translation language.
    """

    assert len(key) <= LONGEST_KEY
    try:
        stroke_list = [Stroke(s) for s in key] # Creates a list of `plover_stroke.BaseStroke` out of the input outline.
    except ValueError as e:
        raise KeyError from e
    translation = ''

    # Constructs the translation by concatenating the theory-resolved stroke.
    for stroke in stroke_list:
        translation += theory.translate_stroke(stroke)
        
    return translation

# def reverse_lookup(text):
#     stroke_list = theory.strokes_from_text(text)
#     if not stroke_list:
#         return []
#     return [tuple(str(s) for s in stroke_list)]

# }}}

# vim: foldmethod=marker