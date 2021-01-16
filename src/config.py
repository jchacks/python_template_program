import logging
import os

import tqdm
from dotenv import load_dotenv

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

load_dotenv(f"{PROJECT_ROOT}/.env", verbose=True)
load_dotenv(f"{PROJECT_ROOT}/secret.env", verbose=True)


#! Put any env vars loaded from dot env here


class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg)
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)


def make_logger():
    logger = logging.getLogger()
    logger.setLevel('DEBUG')
    handler = TqdmLoggingHandler()
    logger.addHandler(handler)
    return logger
