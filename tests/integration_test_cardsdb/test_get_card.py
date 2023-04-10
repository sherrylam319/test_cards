import pytest
import cards

# case 1
def test_get_card_1(empty_db, three_items_db):
    card_id = empty_db.get_card(2)
    assert card_id == cards.Card(summary="buy something",
                                owner="John",
                                state="todo"
                          )
    
#case 2
def test_get_card_2(empty_db, three_items_db):
    with pytest.raises(cards.InvalidCardId):
        empty_db.get_card(4)



