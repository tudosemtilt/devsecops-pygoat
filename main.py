import logging

from modules.filehandler import FileHandler
from modules.logparser import LogParser
from modules.gamesreporter import GamesReporter

logging.basicConfig(
  level=logging.DEBUG, 
  filename='main.log', 
  format='%(asctime)s [%(levelname)s]: %(message)s'
)

# ------------------------------------------------------------------------------

def main():
  raw_log = FileHandler.read_data_from_log(FileHandler.quake_log_path)
  if raw_log == None:
    msg = 'Failed to parse log from file path!'
    logging.error(msg)
    raise Exception(msg)

  reporter = GamesReporter()

  games_log = LogParser.split_raw_log_into_games(raw_log)
  for i, game_log in enumerate(games_log):
    game_id = f'game_{i+1}'
    reporter.add_new_game(game_id)

    players = LogParser.get_players_list_from_game_log(game_log)
    kills = LogParser.get_kills_list_from_game_log(game_log)
    
    reporter.add_players_from_list(game_id, players)
    reporter.add_kills_from_list(game_id, kills)
      
  reporter.export_to_json('report.json')


if __name__ == '__main__':
  main()
