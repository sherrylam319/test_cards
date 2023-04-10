import pytest 
import cards
import sys


#test add_card: case 1

@pytest.mark.parametrize("summary, owner", [("have dinner", "Mary")])
def test_add_card_1(empty_db, summary, owner):
    cardss = cards.Card(summary=summary, owner=owner)
    cards_added = empty_db.add_card(cardss)
    assert cards_added == 1

#test add_card: case 2 

@pytest.mark.parametrize("owner", [("Mary")])
def test_add_card_2(empty_db, owner, capsys):
    with pytest.raises(cards.MissingSummary, match="The summary is missing"):
        cardss = cards.Card(owner=owner)
        cards_added = empty_db.add_card(cardss)

#test add_card: case 3
@pytest.mark.parametrize("summary", [("have dinner")])
def test_add_card_3(empty_db, summary):
    cardss = cards.Card(summary=summary)
    cards_added = empty_db.add_card(cardss)
    assert cards_added == 1


#test add_card: case 4
@pytest.mark.parametrize("summary, owner", 
                        [("do exerise", "Tom")])
def test_add_card_4(summary, owner, empty_db, three_items_db):
    cardss = cards.Card(summary=summary, owner=owner)
    cards_added = empty_db.add_card(cardss)
    assert cards_added == 4








