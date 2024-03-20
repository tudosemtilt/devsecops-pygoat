import logging
import os.path

# ------------------------------------------------------------------------------

class FileHandler:

  quake_log_path = os.path.abspath(os.path.join('resources', 'qgames.log'))

  @staticmethod
  def read_data_from_log(path: str) -> str | None:
    logging.info(f'Reading file from {path}')
    try:
      with open(path, 'r') as file:
        content = file.read()
        logging.info('File read successfully!')
        return content
    except FileNotFoundError:
      return None
