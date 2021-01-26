import logging
from logging.handlers import TimedRotatingFileHandler
import os

folder = 'log'

if not os.path.isdir(folder):
    os.mkdir(folder)
    

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = TimedRotatingFileHandler('log/applog.log', when="midnight", interval=1, encoding='utf8')
handler.suffix = f"%Y-%m-%d"

handler.setFormatter(formatter)
log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(handler)

def push(message):
    log.error(message)
