from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re

def check_attendence(userid,password,dict1):
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()


    driver.get("https://www.rajagiritech.ac.in/stud/ktu/student/")
    driver.find_element(By.NAME, "Userid").send_keys(userid)
    driver.find_element(By.NAME, "Password").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[3]/td/p/input").click()
    driver.get("https://www.rajagiritech.ac.in/stud/ktu/Student/Leave.asp?code=2023S5CU")

    table_rows = driver.find_elements(By.XPATH, '//*[@id="text"]/table[2]/tbody/tr')
    list1 = []
    for i in range(2, len(table_rows) + 1):
        for j in range(1, 9):
            try:
                list1.append(driver.find_element(By.XPATH,
                                                  '//*[@id="text"]/table[2]/tbody/tr[' + str(i) + ']/td[' + str(
                                                      j) + ']').text)
            except:
                pass
    result_list = []
    current_sublist = []

    for item in list1:
        if re.match(r'\d{1,2}-[a-zA-Z]{3}-\d{4}', item):
            if current_sublist:
                result_list.append(current_sublist)
            current_sublist = [item]
        else:
            current_sublist.append(item)

    if current_sublist:
        result_list.append(current_sublist)

    #print(result_list)
    dict1=dict_insert(result_list,dict1)
    return dict1


def dict_insert(result_list,dict1):
    for i in result_list:
        for j in range(7):
            try:
                dict1[i[0]][j]=i[1:][j] if dict1[i[0]][j]==0 or dict1[i[0]][j]==""  else dict1[i[0]][j]
            except:
                pass
    print("+"*16)
    print(result_list)
    print('*'*16)
    print(dict1)
    print("*"*16)
    return dict1

            