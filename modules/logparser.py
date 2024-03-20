import logging
import re

# ------------------------------------------------------------------------------

class LogParser:

  new_game_pattern = \
    r'.*------------------------------------------------------------\n.*' + \
    r'InitGame: '
  new_player_pattern = r'.*ClientUserinfoChanged: \d n\\(.*)\\t\\.*'
  kill_event_pattern = r'.*Kill: .*: (.*) killed (.*) by (.*)'

  @staticmethod
  def split_raw_log_into_games(raw_log: str) -> list[str]:
    logging.info('Separating raw log per game log...')
    # The first item is empty
    return re.split(LogParser.new_game_pattern, raw_log)[1:]
  
  @staticmethod
  def get_players_list_from_game_log(game_log: str) -> list[str]:
    logging.info('Parsing players from game log...')
    # Remove duplicates
    players = list(set(re.findall(LogParser.new_player_pattern, game_log)))
    logging.debug(players)
    return players
  
  @staticmethod
  def get_kills_list_from_game_log(game_log: str) -> list[(str, str, str)]:
    logging.info('Parsing killing events from game log...')
    kill_events = re.findall(LogParser.kill_event_pattern, game_log)
    logging.debug(kill_events)
    return kill_events
