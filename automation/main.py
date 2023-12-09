from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, request
import random
app = Flask(__name__)


userid = ""
password = ""
final_list=[]
total_hours_lost=0
profile_picture=""
name=""
images=["https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1",
        "https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif",
        "https://i0.wp.com/www.galvanizeaction.org/wp-content/uploads/2022/06/Wow-gif.gif?fit=450%2C250&ssl=1",
        "https://s.yimg.com/ny/api/res/1.2/nITV.ukee6aggZzc0jasiQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTY0MA--/https://s.yimg.com/os/creatr-uploaded-images/2023-06/dfe6ff10-19ca-11ee-8d5b-8f954b8ec342",
        "https://www.wired.com/wp-content/uploads/2015/03/855.gif",
        "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/tenor_1.gif",
        "https://cdn.vox-cdn.com/thumbor/iaVMlcV5rj0OuPejZ7HyqYslLZk=/0x0:800x333/1400x788/filters:focal(334x72:462x200):format(gif)/cdn.vox-cdn.com/uploads/chorus_image/image/55278741/gatsby.0.gif",
        "https://images.wondershare.com/filmora/article-images/what-is-gif.gif"
        ]
def scrape_web_page():
    global final_list
    final_list=[]
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.rajagiritech.ac.in/stud/ktu/student/")
    driver.find_element(By.NAME, "Userid").send_keys(userid)
    driver.find_element(By.NAME, "Password").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[3]/td/p/input").click()
    driver.get("https://www.rajagiritech.ac.in/stud/ktu/Student/Leave.asp?code=2023S5CU")
    global profile_picture
    global name
    name=str(driver.find_elements(By.XPATH, "//div[@class='scroller']")[0].text)[36:]
    print(profile_picture)

    table_rows = driver.find_elements(By.XPATH, '//*[@id="text"]/table[2]/tbody/tr')
    list1 = []
    for i in range(2, len(table_rows) + 1):
        for j in range(2, 9):
            try:
                list1.append(driver.find_element(By.XPATH,
                                                  '//*[@id="text"]/table[2]/tbody/tr[' + str(i) + ']/td[' + str(
                                                      j) + ']').text)
            except:
                pass

    from collections import defaultdict
    dict1 = defaultdict(int)

        #This is set for S5 CSBS, Change this data for other branches(available in rsms sessional mark page)
    sub_map_data = """1	101009/IT500A	 SOFTWARE DESIGN WITH UML
    2	101009/IT500B	 COMPILER DESIGN
    3	101009/MS500C	 FUNDAMENTALS OF MANAGEMENT
    4	101009/MS500D	 BUSINESS STRATEGY
    5	101009/EN500E	 BUSINESS COMMUNICATION & VALUE SCIENCE III
    6	101009/IT503F	 MACHINE LEARNING
    7	101009/IT522G	 COMPILER DESIGN LAB (LEX & YACC)
    8	100004/IT501H	 WIRELESS COMMUNICATION
    9	101009/IT522S	 MACHINE LEARNING LAB
    10	101009/IT522T	 MINI PROJECT"""
    sub_map_dict = dict()
    for _ in sub_map_data.split("\n"):
        sub_map_dict[str(_.split("\t")[1])] = str(_.split("\t")[2])

    for _ in list1:
        if _ != "":
            dict1[_] += 1
        else:
            pass


    for _ in sub_map_dict:
        if _ not in dict1:
            dict1[_] = 0

    dict1 = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
    for i, j in dict1.items():
        final_list.append([sub_map_dict[i],i,j])
    global total_hours_lost
    total_hours_lost=sum(dict1.values())

    driver.quit()


@app.route('/', methods=['GET', 'POST'])
def index():
    global final_list
    global userid, password
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        scrape_web_page()
        

        return render_template('profile.html',data=final_list,total_hours_lost=total_hours_lost,name=name,image=random.choice(images))
        
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
