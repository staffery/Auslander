import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_page = "https://service.berlin.de/dienstleistung/324659/en/"
first_page_link = '//*[@id="top"]/div/div/div/div/div[2]/div[3]/div/div[2]/div[9]/div/div/div[2]/div[2]/p[1]/strong/a'


def main():
    chrome = os.getcwd()
    driver = webdriver.Chrome(chrome + "/chromedriver 4")
    wait = WebDriverWait(driver, 20)

    driver.get(main_page)

    driver.find_element_by_class_name("termin-buchen").click()
    driver.find_element_by_link_text("Book Appointment").click()

    wait.until(EC.visibility_of_element_located((By.ID, "xi-cb-1"))).click()

    driver.find_element_by_xpath('//*[@id="xi-sel-400"]/option[14]').click()
    # driver.find_element_by_xpath(first_page_link).click()
    # href = link.get_attribute('href')
    # driver.get(href)

    driver.find_element_by_class_name("termin-buchen").click()
    driver.find_element_by_xpath(
        '//*[@id="mainForm"]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a'
    ).click()


main()
