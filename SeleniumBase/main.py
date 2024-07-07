import PYTHONPATH #必ず一行目に
from log import Logger
from utils.customDriver import customDriver
import pprint
import sys
pprint.pprint(sys.path)

dri = customDriver()
dri.open("localhost:8080")
logger = Logger.StandardLogger()
logger.debug("aaa")
try:
    1/0
except Exception as e:
    logger.error(e)
    

print(9)
    