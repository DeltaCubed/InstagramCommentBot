from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Create a python file called "secrets.py", and declare two variables, "username" and "pw"
from secrets import username, pw
import getpass


class commentBot():
 # Default constructor, opens instagram and logs you in.
    def __init__(self, username, pw, target):
        self.driver = webdriver.Chrome(
            "/usr/bin/chromedriver")  # Specifies path
        self.username = username
        self.target = target
        self.driver.get("https://instagram.com")
        sleep(2)
        # Pushes username and password
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        # Clicks the submit button.
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.get("https://instagram.com/{}".format(self.target))

    def commentthings(self, list_of_things_to_comment):
        # Clicks on the first photo taken by class!
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "v1Nh3.kIKUG._bz0w")))
        self.driver.find_element_by_class_name("v1Nh3.kIKUG._bz0w").click()
        sleep(2)
        # Makes this the new page
        self.driver.get(self.driver.current_url)
        sleep(2)
        for element in list_of_things_to_comment:
            # Waits for textarea to be accessable
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, """//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/textarea""")))
            self.driver.find_element_by_xpath(
                """//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/textarea""").click()
            self.driver.find_element_by_xpath(
                """//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/textarea""").clear()
            self.driver.find_element_by_xpath(
                """//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/textarea""").send_keys(element)
            sleep(2)
            # Clicks post
            self.driver.find_element_by_xpath(
                '//button[@type="submit"]').click()
            sleep(4)


print("Who's your target?")
target = input("Enter your target here:")
new_username = input(
    "Did you insert your username and password into secrets.py already? (y/n)")
if(new_username == "y"):
    print("You're all set. Enjoy trolling your target!")
else:
    username = input("What is your username then?")
    pw = getpass.getpass(
        prompt="What is your password? (Don't worry, I won't tell!)")

things_to_print = ["You lost the game", "Mwhahaha, guess what? You lost the game!",
                   "OMG! SOMEONE CALL 911... Because you lost the game!",
                   "HAHAHAHA. You should look in the mirror. You're looking at a guy who lost the game."]
try:
    new_bot = commentBot(username, pw, target)
    new_bot.commentthings(things_to_print)
except:
    print("There was a error with finding/interacting with that user on instagram.")
    print("Try again, or contact Ethan")
