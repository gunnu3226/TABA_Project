#필요한 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException
import csv

#크롤링 전 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach",True) #브라우저 꺼짐 방지
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']) # 불필요한 에러 메세지 없애기
chrome_options.add_argument('--start-maximized') #브라우저 최대화 상태로 실행
chrome_options.add_argument('disable-inforbars')

driver = webdriver.Chrome(options=chrome_options)

f = open('/Users/gunnu/Desktop/크롤링/card_data.csv','w',encoding='utf-8', newline='')
card_data = csv.writer(f)

#f2 = open('/Users/gunnu/Desktop/크롤링/card_data.csv','w',encoding = 'CP949', newline='')
#benefit_data = csv.writer(f2)

card_id = 0
for i in range(2300,2305):
    try:
        driver.get(f'https://www.card-gorilla.com/card/detail/{i}')
        
        driver.excute_script('document.querySelector("#q-app > header").style.visibility="hidden";')
        
        card_id += 1
        
        #카드 이름
        card_name = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > strong')
        card_name = card_name.text
        
        #카드 브랜드(ex.롯데카드)
        card_brand = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > p')
        card_brand = card_brand.text
        
        #카드 이미지
        card_image = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.plate_area > div > img')
        card_image = card_image.get_attribute('src')
        
        #국내/해외
        card_in_out = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.bnf2 > dl:nth-child(1) > dd.in_out')
        card_int_out = card_brand.text
        
        #카드 전월 실적 조건
        card_record = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.bnf2 > dl:nth-child(2)')
        card_record = card_brand.text
        
        #카드 대표혜택 요약 3가지
        card_summary = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf1')
        card_summary = card_summary.text
        
        #데이터 csv파일로 저장
        card_data.writerow([card_id,card_name,card_brand,card_in_out,card_record,card_summary,card_image])
        
    except:
        continue
driver.quit()
            
        

