from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from core.UserInfo import UserInfo
import json
from util.logging import logger

path = '/home/suriya/Work/ws/projects/insta-bot/geckodriver-v0.26.0-linux64/geckodriver'


# binary = FirefoxBinary(path)
# browser = webdriver.Firefox(firefox_binary=binary)



# url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
# session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
#
# driver = webdriver.Remote(command_executor=url, desired_capabilities={})
# driver.session_id = session_id

driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.instagram.com/')
print(driver.title)
# elem = driver.find_element_by_xpath("//span[@value='Log in with Facebook']").click()
#fb_login_button=driver.find_element_by_class_name('.sqdOP yWX7d    y3zKF ')
#fb_login_button = driver.find_elements_by_xpath("//*[@cla
# ss='sqdOP' and @class='yWX7d' and @class='y3zKF']")
#fb_login_button = driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
# fb_login_button = driver.findElement(By.xpath("//button[contains(@class, 'sqdOP yWX7d    y3zKF ')]"));
#fb_login_button= driver.findElement(By.xpath("//*[@class= 'sqdOP']"));
#fb_login_button = driver.find_element_by_tag_name('button')
#fb_login_button= driver.findElement(By.cssSelector("button[class='sqdOP yWX7d    y3zKF     ']"));


"read from the secret file the user information"
with open('/home/suriya/Work/insta-bot-password.json') as json_file:
    secret = json.load(json_file)

user_info = UserInfo(type=secret['type'], username=secret['username'], password=secret['password'])
user_info.login(driver, 10)

logger.debug('login process succesful')


"use the search input field to search for the list of keywords"
try:
     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'TqC_a')))
     search = driver.find_element_by_tag_name('input')
except TimeoutException:
    print('error timeout exp')

search.send_keys('landscape')

# elem = driver.find_element(By.CLASS_NAME, "eyXLr wUAXj ")
# print(elem)
# elem.text = 'landscape'
# elem.send_keys(Keys.ENTER)




