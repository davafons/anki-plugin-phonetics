from anki.hooks import addHook
from aqt import mw
from aqt.qt import *

from .phonetics import regeneratePhonetics

buttonText = "Bulk-add Phonetics"

def onRegenerate(browser):
    regeneratePhonetics(browser.selected_notes())

def setupMenu(browser):
    a = QAction(buttonText, browser)
    a.triggered.connect(lambda: onRegenerate(browser))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)

addHook("browser.setupMenus", setupMenu)