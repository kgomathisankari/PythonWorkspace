from selenium import webdriver

chrome = webdriver.Chrome(executable_path="/Users/ulaganathan/Software/ChromeDriver/chromedriver")
chrome.get("https://www.w3schools.com/python/python_intro.asp")

chrome.find_element_by_link_text("Next ❯").click()
