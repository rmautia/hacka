from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Driver:

    def __init__(self):
        self.driver = None

    def chrome_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return self.driver

    def edge_driver(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        return self.driver

    def fox_driver(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        return self.driver

    def close_driver(self):
        self.driver.quit()
