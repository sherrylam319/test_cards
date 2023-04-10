import pytest 
import cards


def test_start_test(empty_db, three_items_db):
    empty_db.start(1)
    card = empty_db.get_card(1)
    assert card == cards.Card(summary="have dinner",
                                owner="Mary",
                                state="in prog"
                          )
    
#----------delete_card-----------

#case 1

def test_delete_card_1(empty_db, three_items_db):
    empty_db.delete_card(1)

    with pytest.raises(cards.InvalidCardId):
        empty_db.get_card(1)

#case 2

def test_delete_card_2(empty_db, three_items_db):
    with pytest.raises(cards.InvalidCardId):
        empty_db.get_card(5)


def test_delete_card_3(empty_db, three_items_db):
    with pytest.raises(cards.InvalidCardId):
        empty_db.delete_card(5)


#-----------delete_all------------

def test_delete_all(empty_db, three_items_db):
    empty_db.delete_all()
    all_cards = empty_db.list_cards()
    assert all_cards == []
