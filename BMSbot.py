import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class BmsBot ():
    def __init__(self) :
        self.driver = webdriver.Chrome ("C:/Users/hrush/Documents/chromedriver.exe")
        self.driver.get("https://www.bookmyshow.com/hyderabad")
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id ("wzrk-cancel").click ()

    '''def seat_select(self,nticks):
        self.nticks=nticks
        total = len(self.driver.find_elements_by_xpath ("//tr//td[@class='SRow1']//div//a[contains(@class,'available)]"))
        print(total)
        for i in range(1,total):
            self.x = self.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a[contains(@class,'available)])["+str(i)+"]")
            self.row = self.x.find_element_by_xpath("//parent::div//parent::td//preceding-sibling::td//div").text
            print(self.row)
            if all ([self.x.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a[contains(@class,'available)])["+str(i)+"]//parent::div//parent::td//preceding-sibling::td//div").text==self.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a)["+str(i+t2)+"]//parent::div//parent::td//preceding-sibling::td//div").text for t2 in range(1,int(nticks))]):
                    if all([self.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a)["+str(i+t)+"]").text!='1' and self.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a)["+str(i+t)+"]").get_attribute('class')!="_blocked" for t in range(1,int(nticks))]) :
                        try:
                            if any([self.driver.find_element_by_xpath("(//tr//td[@class='SRow1']//div//a)["+str(i+t1)+"]//parent::div//following-sibling::div").text=='\u00A0' for t1 in range(1,int(nticks))]) :
                                continue
                            else:
                                print (x.text)
                                x.click ()
                        except NoSuchElementException:
                              print (x.text)
                              x.click ()'''
    def seat_select(self,nticks):
        self.nticks=nticks
        row=len(self.driver.find_elements_by_xpath("(//tr//td[@class='SRow1'])"))
        for i in range(1,row+1):
            seat=len(self.driver.find_elements_by_xpath("(//tr//td[@class='SRow1'])["+str(i)+"]//div"))
            for j in range(1,seat-int(nticks)):
                nl=self.driver.find_elements_by_xpath("//tr//td[@class='SRow1']//div[text()='\u00A0']")
                if self.driver.find_element_by_xpath ("(//tr//td[@class='SRow1'])[" + str (i) + "]//div[" + str (j) + "]//a").get_attribute('class')!="_blocked" :
                        print(self.driver.find_element_by_xpath ("(//tr//td[@class='SRow1'])[" + str (i) + "]//div[" + str (j) + "]//a").text)
                    #if all([self.driver.find_element_by_xpath("(//tr//td[@class='SRow1'])["+str(i)+"]//div["+str(j+t1)+"]") not in nl for t1 in range(0,int(nticks))]):
                     #   book = self.driver.find_element_by_xpath ("(//tr//td[@class='SRow1'])[" + str (i) + "]//div[" + str (j) + "]//a")
                      #if all([self.driver.find_element_by_xpath("(//tr//td[@class='SRow1'])["+str(i)+"]//div["+str(j+t)+"]//a").get_attribute('class') != "_blocked" for t in range(0,int(nticks))]) :
                       #     book.click()
                        #    print(book.text)

        '''self.driver.find_element_by_id ('btmcntbook').click ()
        self.driver.find_element_by_id ('shmticket').click ()
        print (self.driver.find_element_by_id ('TickCat').text)
        print (self.driver.find_element_by_id ('audiInfo').text)'''

    def movie_search(self, mov,date,show,nticks):
        self.mov=mov
        self.date=date
        self.show=show
        self.nticks=nticks
        self.driver.find_element_by_xpath("//input[contains(@placeholder, \"Search for Movies\")]").send_keys(mov)
        time.sleep(1)
        self.driver.find_element_by_xpath ("//div[contains(@class,'tt-selectable')]").click ()
        t="//ul[@id='showDates']//div//li/a//div[contains(text(),'"+date+"')]"
        self.driver.find_element_by_xpath (t).click ()
        shows = self.driver.find_elements_by_xpath ("//li[contains(@data-name,'Asian CineSquare')]//div[contains(@class,'showtime-pill-container')]//a")
        for s in shows:
            if s.get_attribute('data-showtime-filter-index')==show :
                s.click()
                break
        self.driver.find_element_by_xpath ("//a[contains(text(),'Accept')]").click ()
        self.driver.find_element_by_id ("pop_"+nticks).click ()
        self.driver.find_element_by_id ("proceed-Qty").click ()
        self.seat_select(nticks)



'''


'''
'''driver.find_element_by_xpath (
    "//a[contains(@href,'discoraja')]//ancestor::div[contains(@class,'listing-info')]//following-sibling::div[contains(@class,'body')]//div[contains(@class,'showtime-pill')]//a[contains(@onclick,'10:35 PM')]").click ()




nele = driver.find_elements_by_xpath ("((//tr//td[@class='SRow1']//div[text()='\u00A0'])//preceding-sibling::div[1]//a)")
#if x.find_element_by_xpath ("//parent::div//parent::td//preceding-sibling::td//div[@class='seatR Setrow1']").text == s[
 #   s.index (x) + 1].find_element_by_xpath (
  #      "//parent::div//parent::td//preceding-sibling::td//div[@class='seatR Setrow1']").text:

for x in s:
    if x not in nele:
        if x.get_attribute ('class') != "_blocked":
            if s[s.index (x) + 1].get_attribute ('class') != "_blocked" :
                    print (x.text)
                    x.click ()

#driver.find_element_by_id ('btmcntbook').click ()
#driver.find_element_by_id ('shmticket').click ()
#print (driver.find_element_by_id ('TickCat').text)
#print (driver.find_element_by_id ('audiInfo').text)'''

'''driver.find_element_by_id('prePay').click()
driver.find_element_by_id('txtEmail').send_keys("hrushyang.adloori69@gmail.com")
driver.find_element_by_id('txtMobile').send_keys("7702455539")
driver.find_element_by_xpath("//div[contains(@data-auto,'more-payment-options')]").click()
driver.find_element_by_xpath("//div[@id='dSecPayOpts_Temp']//div[@class='pm-list']//ul[@id='dPayTabs']//li[@id='dTUPI']").click()
driver.find_element_by_xpath("//img[contains(@alt,'PhonePe')]").click()
driver.find_element_by_id("txtUPIId").send_keys("7702455539")
driver.find_element_by_id("dUPIVPADrop").send_keys("ybl")
driver.find_element_by_xpath("//div[@id='errDivUPI']//following-sibling::button[contains(@onclick,'pay.fnPayUPI')]").click()'''





except:
self.driver.find_element_by_xpath ("//button//span[@aria-label='Load more comments']").click ()

i = 1
        while (1):
            try:
                t = self.driver.find_element_by_xpath ("(//ul[@class='Mr508']//h3//a)[" + str (i) + "]")
                print (str (i) + ".", t.text)
                i += 1
            except:
                t1=self.driver.find_element_by_xpath ("//button//span[@aria-label='Load more comments']")
                b = ActionChains (self.driver)
                b.move_to_element (t1).perform ()
                self.driver.find_element_by_xpath ("//button//span[@aria-label='Load more comments']").click()

r = []
for i in range (len (n) - 10):
    t = n[i:i + 10]
    s = n[i + 10:]
    if s.find (t) == -1:
        continue
    else:
        if t not in r:
            r.append (t)
for i in r:
    print (i)
