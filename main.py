from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as key
import threading

def Login(email="m.24scse1010070@galgotiasuniversity.ac.in",password="1534ads@aqw"):
    driver.get("https://www.guvi.in/sign-in/")
    emailIN=driver.find_element(By.ID,'email')
    emailIN.send_keys(email)
    passwordIN=driver.find_element(By.ID,'password')
    passwordIN.send_keys(password)
    driver.find_element(By.ID,'login-btn').click()
    time.sleep(1)

def installExtension():
    driver.get('https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en')
    add = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div/main/div/section[1]/section/div/div[1]/div[2]/div/button/span[6]")
    add.click()
    time.sleep(3)

def gotoCourse():
    current_lecture = 0 
    VideoIsPlaying = False
    driver.get(Course_link)
    checkDone = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]/a')
    listCourse = driver.find_elements(By.XPATH, "/html/body/main/div[6]/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/ul/li")
    for i in range(len(listCourse)):
        driver.execute_script("window.scrollTo(0, 0);")
        listCourse = driver.find_elements(By.XPATH, "/html/body/main/div[6]/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/ul")
        time.sleep(1)
        print("testing point " + str(i+1) )
        if "completed" not in listCourse[current_lecture].get_attribute("class"):
            print("Course not completed "  + listCourse[current_lecture].text)
            ActivityOpen = False
            ActivityOpen = checkVideo()
            if ActivityOpen:
                if VideoIsPlaying:
                    video = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[1]/div[1]/div[1]/div[2]/video')
                    driver.execute_script("arguments[0].pause();", video)
                
                DoActivity()
            else:
                
                videoPlay = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[1]/div[1]/div[1]/button')
                videoPlay.click()
                VideoIsPlaying = True
                count=0
                video = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[1]/div[1]/div[1]/div[2]/video')
                driver.execute_script("arguments[0].playbackRate = 16;", video)
                # IMPORTANT WHEN USING SPEED CONTROLLER EXTENSION
                # while count<150:
                #     key.press('d')
                #     count+=1
                # IMPORTANT WHEN USING SPEED CONTROLLER EXTENSION
                
                while not ActivityOpen:
                    time.sleep(2)
                    ActivityOpen = checkVideo()                                                            
                
        else:
            print("Course Completed "+ listCourse[current_lecture].text)
            
            time.sleep(2)
            current_lecture+=1
            listCourse[current_lecture].click()

def checkVideo():
    time.sleep(0.5)
    timeVid = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]/a')
    if "disabled" not in timeVid.get_attribute("class"):
        return True
    return False
    
def DoActivity():
    # try:
        
        print("Doing Activity")
        time.sleep(3)
        activityButton = driver.find_element(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[1]/div/ul/li[1]')
        activityButton.click()
        listQuestions = driver.find_elements(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div')
        listDict = {}
        isCorrectDict = {}
        for i in range(len(listQuestions)):
            listDict[i] = 0
            isCorrectDict[i] = False
    
        options = driver.find_elements(By.XPATH, '/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div/button')
        while False in isCorrectDict.values():
            print(listDict , isCorrectDict)
            for i in range(len(listQuestions)):
                print(f'Doing Question {i+1}')
                time.sleep(1)
                option = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[2]/div/button[{listDict[i]+1}]')
                option.click()
                if i != (len(listQuestions)-1):
                    time.sleep(1)
                    if i==0:
                        nextButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button')
                        nextButton.click()
                    else:
                        nextButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button[2]')
                        nextButton.click()

                else:
                    submitButton = driver.find_element(By.XPATH, f'/html/body/main/div[6]/div/div[3]/div[3]/div[2]/div/div[4]/div[{i+1}]/div[2]/div[3]/button[2]')
                    submitButton.click()
                    #time.sleep(2) # remove just for testing
                    
                    for i in range(len(listQuestions)):
                        
                        time.sleep(1)
                        test = driver.find_element(By.XPATH, f'/html/body/div[12]/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[{i+1}]/a/span')
                        print()
                        if "has-error" in test.get_attribute("class").lower():
                            print(test.text + f" in Question {i+1}")
                            listDict[i] +=1
                            isCorrectDict[i] = False
                        elif "correct" in test.text.lower():
                                isCorrectDict[i] = True
                    time.sleep(1)
                    if False in isCorrectDict.values():
                        closeButton = driver.find_element(By.XPATH, '/html/body/div[12]/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[1]/a/span')
                        closeButton.click()
                    
                time.sleep(1)
            print(isCorrectDict)
            print(listDict)
    # except Exception as e:
    #     print("Excaping do activity")
    #     driver.refresh()
    #     print("refreshed")
    #     time.sleep(3)
    #     return None
        
        
if __name__=="__main__":

    Course_link = 'https://www.guvi.in/courses-video/?course=galgotiasjavacollections'
    driver = webdriver.Chrome()  
     

    #installExtension()
    time.sleep(1)
    Login()
    gotoCourse()



    driver.close()