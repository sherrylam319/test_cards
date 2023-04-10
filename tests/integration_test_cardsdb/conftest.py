import pytest 
import cards


@pytest.fixture(scope="function")
def empty_db(tmp_path):
    p = tmp_path / "db_path" 
    p.mkdir()
    db = cards.CardsDB(p)
    yield db
    db.close()



@pytest.fixture 
def three_items_db(empty_db):
    items = [
        cards.Card("have dinner", "Mary"),
        cards.Card("buy something", "John"),
        cards.Card("do homework", "Peter", "finished")
    ]
    for item in items:
       empty_db.add_card(item)

    
