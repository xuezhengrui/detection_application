from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# crawler to trace the propagation path of fake images
class traceCrawler(object):
    def __init__(self, url):
        self.url = url
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def dateTranslate(self, date):
        temp1 = date.split(' ')
        time = temp1[1]
        temp2 = temp1[0].split('月')
        month = temp2[0]
        temp3 = temp2[1].split('日')
        day =  temp3[0]
        return month+'.'+day+' '+time

    def parse_data(self):
        time.sleep(8)
        data_list = []

        for i in range(0,45):
            try:
                temp = {}
                if i % 5 == 0 and i != 0:
                    update_ele = self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]")
                    self.driver.execute_script("arguments[0].scrollIntoView();",update_ele)
                    time.sleep(2)
                try:
                    temp['date'] = self.dateTranslate(self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]/div[2]/div[2]/div[2]/a").text)
                except:
                    temp['date'] = self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]/div[2]/div[2]/div[2]/a").text
                temp['user_link'] = self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]/div[2]/div[1]/a").get_attribute('href')
                temp['text'] = self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]/div[2]/div[1]/span").text
                temp['tweet_link'] = self.driver.find_element_by_xpath("//div[@node-type='feed_list']/div["+str(i+1)+"]/div[2]/div[2]/div[2]/a").get_attribute('href')
            except:
                break
            data_list.append(temp)

        return data_list

    def run(self):
        self.driver.get(self.url)
        data_list = self.parse_data()
        self.driver.quit()
        return data_list

