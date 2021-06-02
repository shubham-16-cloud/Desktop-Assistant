from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

class autologin():

    def instabot(username,password,speak):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("prefs", {\
            "profile.default_content_setting_values.notifications":2
                    })
        driver= webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get("https://www.instagram.com")
        time.sleep(1)
        try:
            txt_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            txt_username.send_keys(username)
            txt_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            txt_password.send_keys(password)
            driver.implicitly_wait(20)
            btn_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            btn_login.click()
            time.sleep(3)
            btn_not_now= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            btn_not_now.click()
            time.sleep(2)
            #btn_notification = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            #btn_notification.click()
            speak("Please wait, while Checking for messages")
            message_count = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div')
            time.sleep(2)
            n = message_count.get_attribute("innerHTML")
            speak(f"There are {n} messages in your message box")
        except NoSuchElementException as e:
            print(e)
            speak("No message in your message box")
        except WebDriverException:
            speak("Sorry sir I could't open instagram")
            driver.close()

    def facebook(username,password,speak):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("prefs", {\
                "profile.default_content_setting_values.notifications":2
                        })
        driver= webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get("https://www.facebook.com")
        speak("opening Facebook")
        time.sleep(2)
        try:
            txt_username = driver.find_element_by_xpath('//*[@id="email"]')
            txt_username.send_keys(username)
            txt_password = driver.find_element_by_xpath('//*[@id="pass"]')
            txt_password.send_keys(password)
            #driver.implicitly_wait(20)
            btn_login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            btn_login.click()
            time.sleep(5)
            speak("please wait while checking for messages")
            message_count = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[2]/span/span')
            time.sleep(3)
            n = message_count.get_attribute("innerHTML")
            speak(f"you have {n} messages in message box")
        except NoSuchElementException as e:
            speak('Sir, there is no message in your message box')
        except WebDriverException :
            speak("Window is not define")
            driver.close()
