import pytest
from unittest import mock
import cards
from typer.testing import CliRunner
import shlex
from cards.cli import app

runner = CliRunner()


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


#purpose of the test: to test if the InvalidCardId work as expected (except how it is triggered)

def test_delete_invalid(mock_cardsdb):
    mock_cardsdb.delete_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("delete 1")
    assert "Error: Invalid card id 1" in out


def test_update_invalid(mock_cardsdb):
    mock_cardsdb.update_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("update 3 -o mary -s something")
    assert "Error: Invalid card id 3" in out