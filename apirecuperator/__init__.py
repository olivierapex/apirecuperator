import sys
import logging


def run_recuperator(config_file_path=None):
    try:
        from apirecuperator.recuperator import run
        return run(config_file_path)
    except ImportError as error:
        print(str(error))
        logging.exception(str(error))
        sys.exit(2)
