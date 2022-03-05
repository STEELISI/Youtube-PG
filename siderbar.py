from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait

videos = ['hkaXd07-rTU']

prev = ""

for l in videos:
    toget = "https://www.youtube.com/watch?v=" + l
    print("toget",toget)


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--public")
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    for i in range(1,2):
        try:
            driver.get(toget)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html = driver.page_source
            print(str(html))

            time.sleep(5000)
        except:
            continue
    driver.close()
