import os
from time import sleep
from colorama import init, Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("https://web.whatsapp.com/")

init()
os.system('cls')
sleep(0.3)

Message = input(Fore.LIGHTCYAN_EX + "Enter Message: " + Fore.LIGHTMAGENTA_EX)
sleep(0.5)
Names = input(Fore.LIGHTGREEN_EX +
              "\nEnter Names [Split with &]: " + Fore.LIGHTYELLOW_EX).split('&')
sleep(0.5)
Number = int(input(Fore.LIGHTWHITE_EX +
                   "\nEnter The Number of Repeatation: " + Fore.CYAN))
sleep(0.5)

for name in Names:
    driver.find_element(By.XPATH, f"//span[@title='{name}']").click()
    sleep(0.5)
    for number in range(Number):
        driver.find_element(
            By.XPATH, f"//div[@role = 'textbox' and @title='Type a message']").send_keys(Message + Keys.ENTER)
    else:
        print(Fore.GREEN + "[+] - " + Fore.WHITE + name)
