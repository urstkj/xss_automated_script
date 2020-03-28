from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pyautogui, pandas
# browser = webdriver.Firefox()  #if you want to check output in browser.
def headlessfirefox(): #headless browser support but screenshot not working
    options = webdriver.FirefoxOptions()
    options.add_argument('--headles s')
    return webdriver.Firefox(options=options)
browser = headlessfirefox()
urls = pandas.read_csv('url_file.csv')
f = open("urls.txt", "w+")
for index, row in urls.iterrows():
    web_url = str(row['url'])
    # web_url = str(row['url']+'custom xss payload for all url') #please add custom xss payload
    browser.get(web_url)
    try:
        WebDriverWait(browser,10).until(ec.alert_is_present(), 'Timed out waiting for PA creation '+'confirmation popup to appear.' )
        alert = browser.switch_to.alert
        # print("xss found at "+alert.text)
        print(web_url)
        # pyautogui.screenshot().save(alert.text+"_screenshot.png") #remove comment for saving the screenshot
        alert.accept()
        f.write(web_url+'\n')
    except TimeoutException:
        print("xss not found at "+browser.current_url)
f.close()
