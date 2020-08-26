import logging
from logging import config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger(__name__)