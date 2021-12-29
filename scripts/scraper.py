from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

from pathlib import Path
print(Path(__file__).absolute())

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("https://www.tiktokv.com/share/video/6939914179348385025/")