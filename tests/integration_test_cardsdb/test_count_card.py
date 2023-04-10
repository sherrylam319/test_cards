import pytest


# case 1
def test_count_card_1(empty_db):
    length = empty_db.count()
    assert length == 0


# case 2
def test_count_card_2(empty_db,three_items_db):
    length = empty_db.count()
    assert length == 3
