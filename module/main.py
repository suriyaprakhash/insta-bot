from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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



delay = 5 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'KPnG0')))
except TimeoutException:
    print('error timeout exp')
fb_login_button_span = myElem
fb_login_button = fb_login_button_span.find_element_by_xpath('..')
fb_login_button.click()

try:
    email = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'email')))
    password = driver.find_element_by_id('pass')
except TimeoutException:
    print('error timeout exp')

with open('/home/suriya/Work/insta-bot-password.json') as json_file:
    secret = json.load(json_file)

print(secret)
print(secret['password'])
email.send_keys(secret['username'])
password.send_keys(secret['password'])

fbLoginButton = driver.find_element_by_id('loginbutton')
fbLoginButton.click()


try:
    not_now_pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
except TimeoutException:
    print('error timeout exp')

not_now_pop_up.click()



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




