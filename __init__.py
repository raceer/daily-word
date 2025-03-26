from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

import random
from . import add_card, retrieve_word

config = mw.addonManager.getConfig(__name__)
deck_name = config["daily_deck_name"]

def add_daily_word() -> None:
    showInfo("Card count: %s" % deck_name)

    deck = add_card.DeckModifier(deck_name)
    # words = retrieve_word.TextParser.get_daily_word("https://www.suomisanakirja.fi/paivan.php")
    parser = retrieve_word.TextParser("https://www.suomisanakirja.fi/paivan.php")
    words = parser.get_daily_word()
    deck.add_word(words[0], words[1], words[2])
    # deck.add_word("wir", "did")

action = QAction("Add daily word", mw)
qconnect(action.triggered, add_daily_word)
mw.form.menuTools.addAction(action)
