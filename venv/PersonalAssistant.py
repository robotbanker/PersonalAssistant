from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import gym_username, gym_pwd

booking_date= '16/07/2021'
booking_activity = '08:15 Gym Slot Male'

class PersonalAssistant():
    driver = webdriver.Chrome()

    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get('https://nuffieldhealthfcl.leisurecloud.net/Connect/memberHomePage.aspx')
        sleep (3)
        email_box= self.driver.find_elements_by_xpath('//*[@id="ctl00_MainContent_InputLogin"]')
        email_box[0].send_keys(gym_username)
        pwd_form= self.driver.find_elements_by_xpath('//*[@id="ctl00_MainContent_InputPassword"]')
        pwd_form[0].send_keys(gym_pwd)
        pwd_form[0].send_keys(Keys.ENTER)


    def browse_page (self):
        sleep (2)
        scroll_btn = self.driver.find_elements_by_xpath('//*[@id="search-panels"]/div[2]/div[1]/h3/span/i')
        scroll_btn[0].click()
        activity_btn = self.driver.find_elements_by_xpath('//*[@id="ctl00_MainContent__advanceSearchUserControl_ActivityGroups"]')
        activity_btn[0].send_keys('Gym + Changing Room')
        activity_btn[0].send_keys(Keys.TAB)
        sleep (3)
        #click search acrtivity bar:
        activity_bar_target= r'//*[@id="ctl00_MainContent__advanceSearchUserControl_Activities"]'
        activity_bar= self.driver.find_elements_by_xpath(activity_bar_target)
        activity_bar[0].click()
        # enter activity you wanna book
        activity_bar[0].send_keys(booking_activity)
        activity_bar[0].send_keys(Keys.ENTER)

        from_date= '//*[@id="ctl00_MainContent__advanceSearchUserControl_startDate"]'
        from_date_bx = self.driver.find_elements_by_xpath(from_date)
        from_date_bx[0].send_keys(booking_date)
#so far so good
        #search for activity selected:
        search= r'//*[@id="ctl00_MainContent__advanceSearchUserControl__searchBtn"]'
        search_btn=self.driver.find_elements_by_xpath(search)
        search_btn[0].click()

        #book activity:


        #activity_selector= r'//*[@id="ctl00_MainContent__advanceSearchUserControl_Activities"]'
        #activity_selector_bx = self.driver.find_elements_by_xpath(activity_selector)
        #activity_selector_bx[0].click()



        #try:
        #    book_selector= '//*[@id="ctl00_MainContent__advanceSearchUserControl__searchBtn"]'
        #    book_selector_bx = self.driver.find_elements_by_xpath(book_selector)
        #    book_selector_bx[0].send_keys(Keys.ENTER)
        #except Exception:
            #sleep (3)
            #slot_815 = r"//*[text()='08:15 Gym Slot Male']"
            #slot_815_btn = self.driver.find_elements_by_xpath(slot_815)
            #slot_815_btn[0].click()
            #sleep(2)


            #book_selector = '//*[@id="ctl00_MainContent__advanceSearchUserControl__searchBtn"]'
            #book_selector_bx = self.driver.find_elements_by_xpath(book_selector)
            #book_selector_bx[0].send_keys(Keys.ENTER)
            #selection_target= r'#ctl00_MainContent__advanceSearchResultsUserControl_Classes_ctrl8_lnkActivitySelect_xs'
            #selection_target_btn = self.driver.find_elements_by_css_selector(selection_target)
            #selection_target_btn[0].click()
            #sleep(2)

            #confirm_booking= r'#ctl00_MainContent_ClassStatus_ctrl0_btnBook'
            #confirm_booking_btn = self.driver.find_elements_by_css_selector(confirm_booking)
            #confirm_booking_btn[0].click()
            #sleep(1)
            #complete_booking=''


run = PersonalAssistant()

run.login()
run.browse_page()