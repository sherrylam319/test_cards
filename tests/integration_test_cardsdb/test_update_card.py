import pytest
import cards 

# case 1
def test_update_1(empty_db, three_items_db):
    empty_db.update_card(card_id=1, card_mods=cards.Card("have breakfast", "Lily", "finished"))
    get_updated_card = empty_db.get_card(1)
    assert get_updated_card == cards.Card(summary="have breakfast", 
                                          owner="Lily",
                                          state="finished",
                                          id=1)
    
# case 2
def test_update_2(empty_db, three_items_db):
    with pytest.raises(cards.InvalidCardId):
        empty_db.update_card(card_id=5, card_mods=cards.Card("have breakfast", "Lily", "finished"))

    

