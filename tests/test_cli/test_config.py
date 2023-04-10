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


def test_config_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path
    
    monkeypatch.setattr(cards.cli, "get_path", fake_get_path)
    assert cards_cli("config") == str(tmp_path)



def test_env_path(monkeypatch, tmp_path):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    assert cards_cli("config") == str(tmp_path)


    