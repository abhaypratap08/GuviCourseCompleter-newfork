from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as key

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
    current_lecture = 0 
    gotLecture = False
    driver.get('https://www.guvi.in/courses-video/?course=galgotiasservletsandjsp')
    checkDone = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]/a')
    while gotLecture==False:
        if checkDone.get_attribute("disabled")=="disabled":
            print("Course not completed")
            gotLecture = True
            videoPlay = driver.find_element(By.CSS_SELECTOR, ".plyr__control")
            videoPlay.click()
            count=0
            while count<150:
                key.press('d')
                count+=1
        else:
            print("Course Completed")
            listCourse = driver.find_elements(By.XPATH, "/html/body/main/div[6]/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/ul")
            print(listCourse)
            current_lecture+=1
            listCourse[current_lecture].click()

def checkVideo():
    timeVid = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[1]/div[1]/div[1]/div[1]/div[2]')
    
    while timeVid.text!="00:00":
        print(timeVid.text)
        time.sleep(2)

if __name__=="__main__":
    driver = webdriver.Chrome()  
    driver.get("https://www.guvi.in/sign-in/") 

    
    Login()
    time.sleep(1)
    installExtension()
    gotoCourse()
    checkVideo()
  

    time.sleep(10)

    driver.close()