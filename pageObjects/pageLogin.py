from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login:
    link_login_id = "login2"
    textbox_username_id="loginusername"
    textbox_password_id="loginpassword"
    button_login_xpath="//*[@id='logInModal']/div/div/div[3]/button[2]"
    linktext_samsung_text="Samsung galaxy s6"
    button_addTOCart_text="Add to cart"
    link_home_xpath="//*[@id='navbarExample']/ul/li[1]/a"
    linktext_laptops_text = "Laptops"
    linktext_macbook_text = "MacBook air"
    linktext_cart_text = "Cart"
    button_placeOrder_xpath="//*[@id='page-wrapper']/div/div[2]/button"
    textbox_name_id="name"
    textbox_country_id = "country"
    textbox_city_id = "city"
    textbox_card_id ="card"
    textbox_month_id = "month"
    textbox_year_id = "year"
    button_purchase_xpath = "//*[@id='orderModal']/div/div/div[3]/button[2]"
    paragraph_placedOrder_xpath = "/html/body/div[10]/p"
    button_ok_xpath = "/html/body/div[10]/div[7]/div/button"

    def __init__(self,driver):
        self.driver=driver

    def clickLogin(self):
        self.driver.find_element(By.ID,self.link_login_id).click()
    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def setPassword(self,paassword):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(paassword)
    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def clickSamsung(self):
        self.driver.refresh()
        # define a wait with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)

        try:
            # find the element
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT,self.linktext_samsung_text)))
            # do something with the element
            element.click()
        except StaleElementReferenceException:
            # if the element is stale, find it again
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT,self.linktext_samsung_text)))
            # do something with the element
            element.click()

        # self.driver.find_element(By.LINK_TEXT,self.linktext_samsung_text).click()
    def clickAddToCart(self):
        self.driver.find_element(By.LINK_TEXT,self.button_addTOCart_text).click()
    def acceptPopup(self):
        try:
            # wait for the alert to be present
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # accept the alert
            alert.accept()
        except TimeoutException:
            print("Timed out waiting for alert")
        except NoAlertPresentException:
            print("No alert is present on the page")

        # self.value=self.driver.switch_to.alert
        # self.value.accept()

        print('SAMSUNG ADDED')
    def clickHome(self):
        self.driver.find_element(By.XPATH,self.link_home_xpath).click()
    def clickLaptops(self):
        self.driver.find_element(By.LINK_TEXT,self.linktext_laptops_text).click()
    def clickMacbook(self):
        self.driver.find_element(By.LINK_TEXT,self.linktext_macbook_text).click()
    def acceptPopup1(self):
        try:
            # wait for the alert to be present
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # accept the alert
            alert.accept()
        except TimeoutException:
            print("Timed out waiting for alert")
        except NoAlertPresentException:
            print("No alert is present on the page")

        print('MACBOOK ADDED')


        # self.driver.switch_to.alert.accept()
    def clickHome1(self):
        self.driver.find_element(By.XPATH,self.link_home_xpath).click()
    def clickCart(self):
        self.driver.find_element(By.LINK_TEXT,self.linktext_cart_text).click()

    def clickPlaceOrder(self):
        self.driver.find_element(By.XPATH,self.button_placeOrder_xpath).click()

    def setName(self,name):
        self.driver.find_element(By.ID,self.textbox_name_id).send_keys(name)

    def setCountry(self,country):
        self.driver.find_element(By.ID,self.textbox_country_id).send_keys(country)

    def setCity(self,city):
        self.driver.find_element(By.ID,self.textbox_city_id).send_keys(city)

    def setCard(self,card):
        self.driver.find_element(By.ID,self.textbox_card_id).send_keys(card)

    def setMonth(self,month):
        self.driver.find_element(By.ID,self.textbox_month_id).send_keys(month)
    def setYear(self,year):
        self.driver.find_element(By.ID,self.textbox_year_id).send_keys(year)

    def clickButtonPurchase(self):
        self.driver.find_element(By.XPATH,self.button_purchase_xpath).click()

    def printParagraph(self):
        para_text=self.driver.find_element(By.XPATH,self.paragraph_placedOrder_xpath).text
        print(para_text)

    def clickOK(self):
        self.driver.find_element(By.XPATH,self.button_ok_xpath).click()
