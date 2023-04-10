from typer.testing import CliRunner
from cards.cli import app
import cards
import pytest
from pathlib import Path
from unittest import mock


import shlex

runner = CliRunner()


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_add(mock_cardsdb):
    cards_cli("add Do something")
    expect = cards.Card(summary="Do something", state="todo")
    mock_cardsdb.add_card.assert_called_with(expect)

def test_version():
    with mock.patch.object(cards, "__version__", "1.2.1") as card_version:
        assert cards_cli("version") == "1.2.1"

def test_delete(mock_cardsdb):
    cards_cli("delete 1")
    mock_cardsdb.delete_card.assert_called_with(1)


def test_list(mock_cardsdb):
    cards_cli("list -o Tom")
    mock_cardsdb.list_cards.assert_called_with(owner="Tom", state=None)


def test_update(mock_cardsdb):
    cards_cli("update 1 -o Tom -s something")
    card_object = cards.Card(summary="something", owner="Tom", state=None)
    mock_cardsdb.update_card.assert_called_with(1, card_object)
    

def test_start(mock_cardsdb):
     cards_cli("start 1")
     mock_cardsdb.start.assert_called_with(1)


def test_finish(mock_cardsdb):
    cards_cli("finish 1")
    mock_cardsdb.finish.assert_called_with(1)













