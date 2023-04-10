

from cards.cli import app
import cards
import pytest
from pathlib import Path
from unittest import mock





@pytest.fixture
def mock_cardsdb():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value
