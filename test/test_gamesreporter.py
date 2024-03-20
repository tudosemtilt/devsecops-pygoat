import pytest
import os
import shutil

from modules.gamesreporter import GamesReporter

TEMP_DIR = os.path.abspath('temp')

TEST_GAME_ID = 'game_test'
TEST_PLAYERS_LIST = [ 'Squirtle', 'Charmander', 'Bulbasaur' ]
TEST_KILLS_LIST_WORLD = [('<world>', 'Squirtle', 'POISON_HURT')]
TEST_KILLS_LIST_PLAYER = [('Charmander', 'Bulbasaur', 'DAMAGE')]

# ------------------------------------------------------------------------------

@pytest.fixture
def use_temp_report_path():
  os.makedirs(TEMP_DIR)
  test_report_path = os.path.join(TEMP_DIR, 'report.json')
  yield test_report_path
  shutil.rmtree(TEMP_DIR)

# ------------------------------------------------------------------------------

def test_returns_new_reporter_when_instantiated():
  reporter = GamesReporter()

  assert reporter.get_content() == {}


def test_adds_new_default_game_content():
  reporter = GamesReporter()
  reporter.add_new_game(TEST_GAME_ID)

  content = reporter.get_content()
  assert content == {
    f'{TEST_GAME_ID}': {
      'total_kills': 0,
      'players': [],
      'kills': {},
      'killing_methods': {}
    }
  }


def test_adds_new_players_from_list():
  reporter = GamesReporter()
  reporter.add_new_game(TEST_GAME_ID)
  reporter.add_players_from_list(TEST_GAME_ID, TEST_PLAYERS_LIST)
  content = reporter.get_content()

  assert content[TEST_GAME_ID]['players'] == TEST_PLAYERS_LIST


def test_add_kill_event_from_world():
  reporter = GamesReporter()
  reporter.add_new_game(TEST_GAME_ID)
  reporter.add_players_from_list(TEST_GAME_ID, TEST_PLAYERS_LIST)
  reporter.add_kills_from_list(TEST_GAME_ID, TEST_KILLS_LIST_WORLD)

  content = reporter.get_content()
  assert content[TEST_GAME_ID]['total_kills'] == 1
  assert content[TEST_GAME_ID]['kills']['Squirtle'] == -1
  assert content[TEST_GAME_ID]['killing_methods']['POISON_HURT'] == 1


def test_add_kill_event_from_player():
  reporter = GamesReporter()
  reporter.add_new_game(TEST_GAME_ID)
  reporter.add_players_from_list(TEST_GAME_ID, TEST_PLAYERS_LIST)
  reporter.add_kills_from_list(TEST_GAME_ID, TEST_KILLS_LIST_PLAYER)

  content = reporter.get_content()
  assert content[TEST_GAME_ID]['total_kills'] == 1
  assert content[TEST_GAME_ID]['kills']['Charmander'] == 1
  assert content[TEST_GAME_ID]['killing_methods']['DAMAGE'] == 1


def test_export_report_to_json_file(use_temp_report_path):
  reporter = GamesReporter()
  reporter.add_new_game(TEST_GAME_ID)
  reporter.add_players_from_list(TEST_GAME_ID, TEST_PLAYERS_LIST)
  reporter.add_kills_from_list(TEST_GAME_ID, TEST_KILLS_LIST_WORLD)
  reporter.add_kills_from_list(TEST_GAME_ID, TEST_KILLS_LIST_PLAYER)
  reporter.export_to_json(use_temp_report_path)

  assert os.path.isfile(use_temp_report_path)
