import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"
name = "USERNAME"



chrome_driver_path = Service("../ChromeDriver/chromedriver.exe")
op = webdriver.ChromeOptions()


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path, options=op)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, "//span[@class='result-data-large number result-data-value download-speed']").text
        self.up = self.driver.find_element(By.XPATH,"//span[@class='result-data-large number result-data-value upload-speed']").text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(3)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "a[role='link'] div[class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
        login_button.click()
        time.sleep(3)

        email_entry = self.driver.find_element(By.CSS_SELECTOR,"input[name='text']")
        email_entry.click()
        email_entry.send_keys(TWITTER_EMAIL)
        email_entry.send_keys(Keys.ENTER)
        time.sleep(5)

        name_confirmation = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        name_confirmation.click()
        name_confirmation.send_keys(name)
        name_confirmation.send_keys(Keys.ENTER)
        time.sleep(5)

        password_entry = self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password_entry.click()
        password_entry.send_keys(TWITTER_PASSWORD)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)

        twit_entry = self.driver.find_element(By.CSS_SELECTOR,".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        twit_entry.click()
        twit_entry.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 100down/20up? WTF")
        time.sleep(3)

        submit_button = self.driver.find_element(By.CSS_SELECTOR,"span[class='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-a023e6 r-rjixqe r-bcqeeo r-qvutc0'] span[class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")
        submit_button.click()
        print("Success")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()