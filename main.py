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
        if "completed" not in listCourse[current_lecture].get_attribute("class"):
            print("Course not completed "  + listCourse[current_lecture].text)
            ActivityOpen = checkVideo()
            if ActivityOpen:
                DoActivity()
            else:
                time.sleep(1)
                videoPlay = driver.find_element(By.XPATH, "/html/body/main/div[6]/div/div[1]/div[1]/div[1]/button")
                videoPlay.click()
                count=0
                # IMPORTANT WHEN USING SPEED CONTROLLER EXTENSION
                # while count<150:
                #     key.press('d')
                #     count+=1
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
    if "disabled" not in timeVid.get_attribute("class"):
        return True
    return False
    
def DoActivity():
    print("Doing Activity")
    activityButton = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]')
    activityButton.click()
    listQuestions = driver.find_elements(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div')
    listDict = {}
    isCorrectDict = {}
    for i in range(len(listQuestions)):
        listDict[i] = 0
        isCorrectDict[i] = False
  
    options = driver.find_elements(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div/button')
    for i in range(len(listQuestions)):
        print(f'Doing Question {i+1}')
        option = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[2]/div/button[{listDict[i]+1}]')
        option.click()
        if i != len(listQuestions)-1:
            if i==0:
                nextButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button')
                nextButton.click()
            else:
                nextButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button[2]')
                nextButton.click()

        else:
            submitButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button[2]')
            submitButton.click()
            time.sleep(1)
            for i in range(len(options)):
                test = driver.find_element(By.XPATH, f'/html/body/div[9]/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[{i+1}]/a')
                if "wrong" in test.text.lower():
                    print(test.text + f" in Question {i+1}")
                    listDict[i] +=1
                    isCorrectDict[i] = False
                elif "correct" in test.text.lower():
                    isCorrectDict[i] = True
                    
        time.sleep(1)
        
        
if __name__=="__main__":
    driver = webdriver.Chrome()  
    driver.get("https://www.guvi.in/sign-in/") 

    
    Login()
    time.sleep(1)
    #installExtension()
    gotoCourse()



    driver.close()