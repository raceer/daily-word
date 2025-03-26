from aqt import mw

class DeckModifier:
    def __init__(self, deck_name):
        self.did = mw.col.decks.id(deck_name, True)
        self.deck = mw.col.decks.get(self.did, True)

    def add_word(self, front, back, example=""):
        model = mw.col.models.by_name("Basic")
        new_note = mw.col.newNote(model)
        new_note["Front"] = front
        new_note["Back"] = back
        new_note["Example"] = example
        new_note.note_type()["did"] = self.did
        mw.col.addNote(new_note)
        mw.col.decks.save(self.deck) 

