from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from util.logging import logger

"gets the user information and the login functionality"
class UserInfo:
    def __init__(self, type, username, password):
        self.type = type
        self.username = username
        self.password = password

    "this method decides whether it is insta login or facebook login and is abstracted"
    def login(self,  driver, delay):
        if self.type == 'fb':
            self.facebook_login(driver,delay)
            logger.debug("using fb login")
        if self.type == 'insta':
            self.instagram_login(driver,delay)
            logger.debug("using insta login")

    "runs facebook login"
    def facebook_login(self, driver, delay):
        logger.debug("login in using fb cred")

        delay = 5  # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'KPnG0')))
        except TimeoutException:
            print('error timeout exp')
        fb_login_button_span = myElem
        fb_login_button = fb_login_button_span.find_element_by_xpath('..')
        fb_login_button.click()

        try:
            email_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'email')))
            password_input = driver.find_element_by_id('pass')
        except TimeoutException:
            print('error timeout exp')

        print(self)
        print(self.password)
        email_input.send_keys(self.username)
        password_input.send_keys(self.password)

        fbLoginButton = driver.find_element_by_id('loginbutton')
        fbLoginButton.click()

        logger.debug("fb login successful")

        "evict turn on notification popup"
        self.evict_turn_on_notification_popup(driver)


    "runs instagram login"
    def instagram_login(self, driver, delay):
        logger.debug("login in using insta cred")

        try:
            username_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'username')))
            password_input = driver.find_element_by_name('password')
        except TimeoutException:
            print('error timeout exp')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        #button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
        button_login = driver.find_element_by_xpath("//button[@type='submit']")
        button_login.click()
        sleep(5)

        "evict save login info popup"
        not_now_pop_up = driver.find_element_by_xpath("//button[@type='button']")
        not_now_pop_up.click()
        sleep(3)

        "evict turn on notification popup"
        self.evict_turn_on_notification_popup(driver)


    def evict_turn_on_notification_popup(self, driver):
        "evict popup"
        try:
            not_now_pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
        except TimeoutException:
            print('error timeout exp')

        not_now_pop_up.click()