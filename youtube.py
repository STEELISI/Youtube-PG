from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait


videos = ['hkaXd07-rTU','ldjtA3hj5cc','XSvBYVjgtGs']

prev = ""

for l in videos:
    toget = "https://www.youtube.com/watch?v=" + l
    print("toget",toget)


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--public")
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    for i in range(1,3):
        try:
            driver.get(toget)
            driver.switch_to_window(driver.window_handles[0])
            driver.refresh()
            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            commas = str(html).split(",")
            for line in commas:            
                if('dVideoId' in str(line)):
                    print(l,"||",line)
            #print(html)
            time.sleep(5)
            driver.refresh()
            driver.switch_to_window(driver.window_handles[1])
            driver.refresh()
        except:
            continue
    driver.close()
