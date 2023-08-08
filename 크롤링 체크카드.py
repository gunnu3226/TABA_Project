#필요한 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

#f2 = open('/Users/gunnu/Desktop/크롤링/card_data.csv','w',encoding = 'CP949', newline='')
#benefit_data = csv.writer(f2)

#데이터로 저장할 파일 생성, 접근
with open('/Users/gunnu/Desktop/크롤링/check_card_data.csv', 'w', encoding='utf-8', newline='') as f:
    card_data = csv.writer(f)
    
    #데이터 테이블 열 이름 저장
    card_data.writerow(['card_id','card_name','card_brand','card_in_out','card_record','card_summary','card_image','card_section'])
    
    #카드 식별자 번호부여를 위한 변수 생성
    card_id = 0  

    #크롬으로 고릴라 신용카드 목록 접속    
    driver = webdriver.Chrome()
    driver.get('https://card-gorilla.com/search/card?cate=CHK')
    
    #더보기 6번 클릭으로 카드 70개 띄우기
    for _ in range(2):
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="q-app"]/section/div[1]/section/div/article[1]/article/a').click()
        WebDriverWait(driver, 30)#로딩 대기
        time.sleep(3)
    
    #카드상세 보기를 새탭으로 열기
    for i in range(1,31):
            # 수집하고자 하는 카드로 스크롤 이동
            time.sleep(7)
            target_element = driver.find_element(By.XPATH, '//*[@id="q-app"]/section/div[1]/section/div/article[1]/article/ul/li[{}]/div'.format(i))
            actions = ActionChains(driver)
            actions.move_to_element(target_element).perform()
            time.sleep(5)
            #클릭하여 카드 정보 페이지로 이동
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/section/div[1]/section/div/article[1]/article/ul/li[{}]/div/div[2]/div[2]/a'.format(i)))).click()
            time.sleep(5)
            
            #여기에 크롤링 작업
            try:
                driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')
            
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
                card_in_out = card_in_out.text
            
                #카드 전월 실적 조건
                card_record = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.bnf2 > dl:nth-child(2)')
                card_record = card_record.text
            
                #카드 대표혜택 요약 3가지
                card_summary = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf1')
                card_summary = card_summary.text
            
                #데이터 csv파일로 저장
                card_data.writerow([card_id,card_name,card_brand,card_in_out,card_record,card_summary,card_image,'체크카드'])
            except:
                continue
            #크롤링 로딩 대기시간
            time.sleep(5)
            #카드 목록 페이지로 뒤로가기
            driver.back()
            WebDriverWait(driver, 30)