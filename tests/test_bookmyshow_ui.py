from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_homepage_loads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:5000")
    assert "BookMyShow Lite" in driver.title
    movie_cards = driver.find_elements("class name", "movie")
    assert len(movie_cards) > 0
    driver.quit()
