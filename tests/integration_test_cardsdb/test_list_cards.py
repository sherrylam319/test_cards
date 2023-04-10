import pytest
import cards


# case 1
def test_list_cards_1(empty_db, three_items_db):
    item = empty_db.list_cards(owner="Mary")
    assert item == [cards.Card(summary="have dinner",
                                owner="Mary",
                                state="todo",
                                id=1)
                               ]
    

# case 2
def test_list_cards_2(empty_db, three_items_db):
    item = empty_db.list_cards(state="finished")
    assert item == [cards.Card(summary="do homework",
                               owner="Peter",
                               state="finished",
                               id=3)]
    
# case 3
def test_list_cards_3(empty_db, three_items_db):
    all_cards = empty_db.list_cards()
    assert all_cards ==[
            cards.Card(summary="have dinner",
                    owner="Mary",
                    state="todo",
                    id=1),
            cards.Card(summary="buy something",
                    owner="John",
                    state="todo",
                    id=2),
             cards.Card(summary="do homework",
                    owner="Peter",
                    state="finished",
                    id=3)
        ]
    


