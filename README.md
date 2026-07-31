# Plover implementation of Spanish Melani system

Based on https://gist.github.com/sammdot/84c601404c6a74c0895c294ab4b818be

Forked from the implementation by Sonsoles García Martín, Noelia Ruiz Martínez used at MQD.

My intention is to provide a simpler, less optimized, less opinionated Melani system implementation for Spanish in Plover, even if it's ultimately less powerful, so to be a reference based on what publicly-available documentation there is.

I am not a professional stenographer. This is a learning project for me.

## Decisions

The Melani system in the reference uses the `eo` chord sometimes to mark "-os" and sometimes to mark a translations as ending with a consonant.
This "-os" outputting function was shared with `ieao`, and there wasn't an obvious pattern explained.
Some analysis of the example text might reveal some ergonomic principle.
I decided to keep `eo` as "-os" _only_, for symmetry with `ia` ("-as"),
and make `ieao`, a chord not elsewhere employed, mark a translation as ended instead.
