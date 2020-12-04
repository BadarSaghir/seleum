# This is a sample Python script.
from selenium import webdriver

object = {}
chrome_driver = "/usr/bin/chromedriver"
# chrome_driver = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")
catch = driver.find_elements_by_css_selector(".event-widget time")
url = driver.find_elements_by_css_selector(".event-widget li a")
# catch.get_attribute('datetime')
i = 0
for so, a in zip(catch, url):
    object[i] = {
        "time": so.text,
        'name': a.text,
        "link": a.get_attribute("href")

    }

    print(so.text, a.get_property('attributes')[0]['name'])
    i += +1
print(object)
print(catch[0].text)
driver.quit()
