from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as key
import threading

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
    driver.get('https://www.guvi.in/courses-video/?course=galgotiasdsausingc')
    checkDone = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]/a')
    listCourse = driver.find_elements(By.XPATH, "/html/body/main/div[6]/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/ul/li")
    for i in range(len(listCourse)-1):
        print( listCourse[current_lecture].get_attribute("class"))
        if "completed" not in listCourse[current_lecture].get_attribute("class"):
            print("Course not completed")
            ActivityOpen = checkVideo()
            if ActivityOpen:
                DoActivity()
            else:
                time.sleep(1)
                videoPlay = driver.find_element(By.XPATH, "/html/body/main/div[6]/div/div[1]/div[1]/div[1]/button")
                videoPlay.click()
                count=0
                # IMPORTANT WHEN USING SPEED CONTROLLER EXTENSION
                while count<150:
                    key.press('d')
                    count+=1
                # IMPORTANT WHEN USING SPEED CONTROLLER EXTENSION
                
                while not ActivityOpen:
                    time.sleep(2)
                    ActivityOpen = checkVideo()
                DoActivity()
                
        else:
            print("Course Completed")
            
            time.sleep(2)
            current_lecture+=1
            listCourse[current_lecture].click()

def checkVideo():
    timeVid = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]/a')
    print(timeVid.get_attribute("class"))
    if "active" in timeVid.get_attribute("class"):
        return True
    return False
    
def DoActivity():
    print("Doing Activity")
    activityButton = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]')
    activityButton.click()
    listQuestions = driver.find_elements(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[1]')
    print(len(listQuestions))
    

if __name__=="__main__":
    driver = webdriver.Chrome()  
    driver.get("https://www.guvi.in/sign-in/") 

    
    Login()
    time.sleep(1)
    installExtension()
    gotoCourse()
    
  

    time.sleep(10)

    driver.close()