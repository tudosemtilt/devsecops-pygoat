import pytest
import os
import shutil

from modules.filehandler import FileHandler

TEMP_DIR = os.path.abspath('temp')
SAMPLE_LOG = '0:00 --------\n0:01 Test log\n0:02 --------'

# ------------------------------------------------------------------------------

@pytest.fixture
def use_temp_log():
  os.makedirs(TEMP_DIR)
  test_path = os.path.join(TEMP_DIR, 'test.log')
  with open(test_path, 'w+') as f:
    f.write(SAMPLE_LOG)
  yield test_path
  shutil.rmtree(TEMP_DIR)


def test_returns_log_when_reading_from_existing_file(use_temp_log):
  raw_log = FileHandler.read_data_from_log(use_temp_log)
  assert raw_log == SAMPLE_LOG


def test_returns_none_when_reading_data_from_missing_file():
  raw_log = FileHandler.read_data_from_log('')
  assert raw_log == None
    
