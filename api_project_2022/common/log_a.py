from nb_log import LogManager
from config.config import ROOT_PATH
import os
logpath = os.path.join(ROOT_PATH,"log")
logger = LogManager("ceshi").get_logger_and_add_handlers(
    log_filename="yuanshen.log",log_path=logpath)

print("hello")
logger.debug("这是debug")
logger.info("info")
logger.error("najsn")
