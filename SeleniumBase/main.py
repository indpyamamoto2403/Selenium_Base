import PYTHONPATH #必ず一行目に

from utils.customDriver import customDriver
import pprint
import sys
pprint.pprint(sys.path)

dri = customDriver()
dri.open("localhost:8080")