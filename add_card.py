from aqt import mw

config = mw.addonManager.getConfig(__name__)
deck_name = config["daily_deck_name"]

mw.col.decks.id(deck_name)

