from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait

import json

#extract videos from a file
videos = set()
f = open("vid.txt")
for p in f:
    videos.add(p.strip())

# videos = ['hkaXd07-rTU','ldjtA3hj5cc','XSvBYVjgtGs']
prev = ""

info = []

for l in videos:
    toget = "https://www.youtube.com/watch?v=" + l
    print("toget",toget)


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--public")
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    for i in range(1,2):
        try:
            driver.get(toget)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html = driver.execute_script("return document.getElementsByTagName('html')[0 ].innerHTML")

            all_info = str(html)
            fname = "result.txt"

            if "promotedSparklesWebRenderer" in all_info:
                place = all_info.find("promotedSparklesWebRenderer")
                info = all_info[place:place+2000]
                if "title" in info:
                    title_place = info.find("title")
                    end_place = info[title_place:].find("}")
                    line_sub_title = info[title_place+22:title_place+end_place-1]

                if "description" in info:
                    title_place = info.find("description")
                    end_place = info[title_place:].find("}")
                    line_sub_description = info[title_place+28:title_place+end_place-1]


                if "websiteText" in info:
                    title_place = info.find("websiteText")
                    end_place = info[title_place:].find("}")
                    line_sub_website = info[title_place+28:title_place+end_place-1]



            with open(fname, "a", encoding="utf-8") as f:
                start = 100
                f.write(f"{l} |")
                f.write(f"{line_sub_title} | ")
                f.write(f"{line_sub_description} | ")
                f.write(f"{line_sub_website} \n")
                # f.write("-----------Below is the whole text-------------\n\n")

                # # while start <= len(info):
                # #     f.write(info[start-100:start])
                # #     f.write("\n")
                # #     start += 100
                # f.write(all_info)

            time.sleep(5)            
        except:
            continue
    driver.close() 