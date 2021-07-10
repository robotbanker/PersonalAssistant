from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import gym_username, gym_pwd
from Dates import test, next_day_formatted, next_day_string

from Messanger import mail_sender

booking_date= next_day_formatted
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

    def select_activity (self):
        sleep (2)
        scroll_btn = self.driver.find_elements_by_xpath('//*[@id="search-panels"]/div[2]/div[1]/h3/span/i')
        scroll_btn[0].click()
        activity_btn = self.driver.find_elements_by_xpath('//*[@id="ctl00_MainContent__advanceSearchUserControl_ActivityGroups"]')
        activity_btn[0].send_keys('Gym + Changing Room')
        activity_btn[0].send_keys(Keys.TAB)
        sleep (1)
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
        to_date = r'//*[@id="ctl00_MainContent__advanceSearchUserControl_endDate"]'
        to_date_bx = self.driver.find_elements_by_xpath(to_date)
        to_date_bx[0].send_keys(booking_date)

        #search for activity selected:
        search= r'//*[@id="ctl00_MainContent__advanceSearchUserControl__searchBtn"]'
        search_btn=self.driver.find_elements_by_xpath(search)
        search_btn[0].click()

        sleep(3)
        slot_815 = '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Classes_ctrl0_lnkActivitySelect_lg"]'
        slot_815_btn = self.driver.find_elements_by_xpath(slot_815)
        slot_815_btn[0].click()
        #confirm booking
        sleep(2)
        confirm = '//*[@id="ctl00_MainContent_ClassStatus_ctrl0_btnAvaliable"]'
        confirm_btn = self.driver.find_elements_by_xpath(confirm)
        confirm_btn[0].click()
        #complete booking
        sleep (2)
        complete = '//*[@id="ctl00_MainContent_btnBasket"]'
        complete_btn = self.driver.find_elements_by_xpath(complete)
        complete_btn[0].click()


if test == True:
    try:
        run = PersonalAssistant()
        run.login()
        run.select_activity()
        subject = 'Gym booked for ' f'{next_day_string}' + f' {next_day_formatted}'
        message = f"""\
        <html>
          <body>
            <p>Hi, Davide,<br> <br> 
               I'm happy to confirm that I booked the gym for you on <b>{next_day_string}  {next_day_formatted}</b>.<br>
               <br>
               Have a great day &#10084;&#65039 <br>
               Samantha <br> xx
            </p>
          </body>
        </html>
        """
        print('gym successfully booked')

    except Exception:
        try:
            print ('First excution failed, I will try again...')
            run = PersonalAssistant()
            run.login()
            run.select_activity()
            subject = f'Your booking confirmation: Failed to book for ' f'{next_day_string}' + f' {next_day_formatted}'
            message = f"""\
                    <html>
                      <body>
                        <p>Hi, Davide,<br> <br> 
                           I'm happy to confirm that I booked the gym for you on <b>{next_day_string}  {next_day_formatted}</b>.<br>
                           Just as an FYI, today the website didn't respond on the first attempt.
                           <br><br>
                           Have a great day &#10084;&#65039 <br>
                           Samantha <br> xx
                        </p>
                      </body>
                    </html>
                    """
        except Exception:
            print('both booking attepmts failed. Sending disappointing email...')
            subject = f'Failed to book for ' f'{next_day_string}' + f' {next_day_formatted}'
            message = f"""\
                            <html>
                              <body>
                                <p>Hi Davide,<br> <br> 
                                   I tried to book the gym for you on <b>{next_day_string}  {next_day_formatted}</b>.<br>
                                   Unfortunately the website failed to respond on both first and second attempt.
                                   <br><br>
                                   I hope this won't ruin your day &#10084;&#65039 <br>
                                   Samantha <br>
                                </p>
                              </body>
                            </html>
                            """
else:
    subject = 'No booking is required today'
    message = """\
    <html>
      <body>
        <p>Hi, Davide,<br> <br> 
           I checked your agenda and no booking is required for your upcoming session.
           <br><br>
           Have a great day, <br>
           Samantha <br> xx
        </p>
      </body>
    </html>
    """
    PersonalAssistant().driver.close()

mail_sender(text= message,mail_subject= subject )


