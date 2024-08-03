import PYTHONPATH #必ず一行目に
from log import Logger
from utils.customDriver import customDriver
driver = customDriver()
driver.open("http://google.com")
try:
    1/0
except Exception as e:
    print("error")
    

print(6)
    