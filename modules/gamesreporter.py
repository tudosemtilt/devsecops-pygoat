import logging
import json

# ------------------------------------------------------------------------------

class GamesReporter:

  def __init__(self):
    self.__content = {}

  def get_content(self) -> dict:
    return self.__content

  def add_new_game(self, game_id: str) -> None:
    logging.info(f'Adding new game "{game_id}"...')
    self.__content[game_id] = {
      'total_kills': 0,
      'players': [],
      'kills': {},
      'killing_methods': {}
    }
  
  def add_players_from_list(self, game_id: str, players: list[str]) -> None:
    logging.info(f'Adding players to "{game_id}"...')
    logging.debug(players)
    self.__content[game_id]['players'] = players
    for player in players:
      self.__content[game_id]['kills'][player] = 0

  def add_kills_from_list(self, game_id: str, kill_log: list[(str, str, str)]) -> None:
    logging.info(f'Adding kills to "{game_id}"...')
    for (killer, victim, method) in kill_log:
      logging.debug(f'killer="{killer}", victim="{victim}", method="{method}"')
      self.__content[game_id]['total_kills'] += 1
      self.__add_kill_method(game_id, method)
      if killer == '<world>':
        logging.debug(f'Decrements score from "{victim}"')
        self.__add_kill_from_world(game_id, victim)
      else:
        logging.debug(f'Increments score from "{killer}"')
        self.__add_kill_from_player(game_id, killer)

  def export_to_json(self, path: str) -> None:
    logging.info(f'Generating JSON report on {path}')
    with open(path, 'w+') as f:
      f.write(json.dumps(self.__content, indent=2))

  def __add_kill_from_world(self, game_id: str, victim: str) -> None:
    self.__content[game_id]['kills'][victim] -= 1
  
  def __add_kill_from_player(self, game_id: str, killer: str) -> None:
    self.__content[game_id]['kills'][killer] += 1

  def __add_kill_method(self, game_id: str, method: str) -> None:
    self.__content[game_id]['killing_methods'][method] = \
      self.__content[game_id]['killing_methods'].get(method, 0) + 1
