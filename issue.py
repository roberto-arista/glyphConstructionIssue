from pathlib import Path

import fontParts.world as fp
from glyphConstruction import (
    GlyphConstructionBuilder,
    ParseGlyphConstructionListFromString,
)

txt = """\
A._failing = A@origin, origin+100
A._notFailing = space + A@origin, origin+100
"""

if __name__ == "__main__":
    constructions = ParseGlyphConstructionListFromString(txt)

    font = fp.OpenFont(Path("mutator sans/MutatorSansLightCondensed.ufo"))

    for eachConstruction in constructions:
        try:
            # build a construction glyph
            constructionGlyph = GlyphConstructionBuilder(eachConstruction, font)

            # get the destination glyph in the font
            glyph = font.newGlyph(constructionGlyph.name, clear=True)

            # draw the construction glyph into the destination glyph
            constructionGlyph.draw(glyph.getPen())

            # copy construction glyph attributes to the destination glyph
            glyph.name = constructionGlyph.name
        except TypeError:
            print(f"Failing: {eachConstruction}")
