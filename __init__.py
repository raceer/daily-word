from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

import random
from . import add_card

config = mw.addonManager.getConfig(__name__)
deck_name = config["daily_deck_name"]

def add_daily_word() -> None:
    showInfo("Card count: %s" % deck_name)

    deck = add_card.DeckModifier(deck_name)
    deck.add_word("hey", "nice to meet you")

action = QAction("Add daily word", mw)
qconnect(action.triggered, add_daily_word)
mw.form.menuTools.addAction(action)
