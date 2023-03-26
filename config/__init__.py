import os
import logging

logger = logging.getLogger(__name__)

class Config:

    def __init__(self):
        logger.debug("Loading Config")
        path_current_directory = os.path.dirname(__file__)
        self.log_config = path_current_directory + "\logging.conf"
        print(self.log_config)

    def config_path(self):
        return self.log_config
