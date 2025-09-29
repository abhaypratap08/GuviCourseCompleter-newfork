from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Login():
    email=driver.find_element(By.ID,'email')
    email.send_keys("m.24scse1010070@galgotiasuniversity.ac.in")
    password=driver.find_element(By.ID,'password')
    password.send_keys("1534ads@aqw")
    driver.find_element(By.ID,'login-btn').click()

def installExtension():
    driver.get('https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en')
    add = driver.find_element(By.CLASS_NAME, "UywwFc-vQzf8d")
    add.click()
    time.sleep(3)

def gotoCourse():
    driver.get('https://www.guvi.in/courses-video/?course=galgotiasservletsandjsp')
    video = driver.find_element(By.CSS_SELECTOR, ".plyr__control")
    video.click()



if __name__=="__main__":
    driver = webdriver.Chrome()  # You can also use Firefox, Edge, etc.
    driver.get("https://www.guvi.in/sign-in/")  # Open a webpage
    driver.maximize_window()

    Login()
    time.sleep(1)
    installExtension()
    gotoCourse()

    time.sleep(10)

    driver.close()