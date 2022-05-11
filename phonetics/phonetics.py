#
# Copyright: Micah Gajewski <micahbgaj@gmail.com>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Automatic Phonetics Generation.
#

from aqt import mw
from . import parser

config = mw.addonManager.getConfig(__name__)

srcFields = config["srcFields"]
dstFields = config["dstFields"]

def regeneratePhonetics(nids):
    mw.checkpoint("PhoneticComponentAddon")
    mw.progress.start()

    for nid in nids:
        note = mw.col.get_note(nid)

        src = None
        for fld in srcFields:
            if fld in note:
                src = fld
                break

        if not src:
            # no src field
            continue

        dst = None
        for fld in dstFields:
            if fld in note:
                dst = fld
                break

        if not dst:
            # no dst field
            continue

        if note[dst]:
            # already contains data, skip
            continue

        srcTxt = mw.col.media.strip(note[src])
        if not srcTxt.strip():
            continue

        try:
            note[dst] = parser.getHighlightedPhonetics(srcTxt)
        except Exception as e:
            raise e

        note.flush()

    mw.progress.finish()
    mw.reset()