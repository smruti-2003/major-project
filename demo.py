from uahi.logger import logging
from uahi.exception import UahiException
import sys

logging.info("division by zero")

try:
    a = 2/0
except Exception as e:
    raise UahiException(e,sys)