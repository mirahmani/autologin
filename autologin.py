'''
Written on 11 July 2017
@author : Miranti Rahmani
'''


from credentials import credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities

#urls
gmail = 'http://mail.google.com'
quora = 'http://www.quora.com'
wordpress = 'https://wordpress.com/log-in'

#set web driver
chrome_options = Options()
chrome_options.add_argument('user-data-dir=/Users/mirantirahmani/Library/Application Support/Google/Chrome')
capabilities = DesiredCapabilities.CHROME.copy()
chromedriver = '/Volumes/DATA/_PyRandomProjects/autologin/chromedriver/chromedriver' #where you put chromedriver
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options = chrome_options, desired_capabilities=capabilities)

#open web in new window
driver.get(gmail)
gmail_id = driver.find_element_by_xpath('//*[@id="identifierId"]')
gmail_id.click()
gmail_id.send_keys(credentials.google['uid'])
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
gmail_pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
gmail_pwd.click()
gmail_pwd.send_keys(credentials.google['pwd'])
gmail_pwd = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
gmail_pwd.click()

#open quora in new tab
driver.execute_script('window.open("' + quora + '");')
driver.switch_to_window(driver.window_handles[1])
quora_id = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div/input')
quora_id.click()
quora_id.send_keys(credentials.quora_login['uid'])
quora_pwd = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div[2]/input')
quora_pwd.click()
quora_pwd.send_keys(credentials.quora_login['pwd'])
quora_login_button = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div[3]/input')
quora_login_button.click()

#open wordpress in new tab
driver.execute_script('window.open("' + wordpress + '");')
driver.switch_to_window(driver.window_handles[2])
wp_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'usernameOrEmail')))
wp_id.click()
wp_id.send_keys(credentials.wp['uid'])
wp_pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'password')))
wp_pwd.click()
wp_pwd.send_keys(credentials.wp['pwd'])
wp_login_button = driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div[1]/div/form/div/div[3]/button')
wp_login_button.click()