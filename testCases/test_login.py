from selenium import webdriver

from pageObjects.pageLogin import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    name = ReadConfig.getName()
    country = ReadConfig.getCountry()
    city = ReadConfig.getCity()
    card = ReadConfig.getCard()
    month = ReadConfig.getMonth()
    year = ReadConfig.getYear()
    logger=LogGen.loggen()
    def test_0001_login(self,setup):
        self.driver = setup
        self.driver=webdriver.Chrome()
        self.logger.info("****test_0001_login****")
        self.logger.info('****Launching Chrome****')
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.driver.implicitly_wait(5)
        self.lp.clickLogin()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.logger.info('****Entering Username****')
        self.lp.setUsername(self.username)
        self.driver.implicitly_wait(5)
        self.logger.info('****Entering Password****')
        self.lp.setPassword(self.password)
        self.driver.implicitly_wait(5)

        self.lp.clickLoginButton()
        self.driver.implicitly_wait(5)
        self.logger.info('****Successful Log In****')

        self.logger.info('****Clicking On Samsung****')
        self.lp.clickSamsung()
        self.driver.implicitly_wait(5)

        self.lp.clickAddToCart()
        self.driver.implicitly_wait(5)

        self.lp.acceptPopup()
        self.driver.implicitly_wait(5)
        self.logger.info('****Adding Samsung To The Cart****')

        self.lp.clickHome()
        self.driver.implicitly_wait(5)

        self.logger.info('****Clicking On Laptops****')
        self.lp.clickLaptops()
        self.driver.implicitly_wait(5)

        self.logger.info('****Clicking On Macbook****')
        self.lp.clickMacbook()
        self.driver.implicitly_wait(5)

        self.lp.clickAddToCart()
        self.driver.implicitly_wait(5)

        self.lp.acceptPopup1()
        self.driver.implicitly_wait(5)

        self.logger.info('****Adding Macbook To The Cart****')

        self.lp.clickCart()
        self.driver.implicitly_wait(10)

        self.logger.info('****Placing Order****')
        self.lp.clickPlaceOrder()
        self.driver.implicitly_wait(5)

        self.logger.info('****Entering Customer Details****')
        self.lp.setName(self.name)
        self.driver.implicitly_wait(5)

        self.lp.setCountry(self.country)
        self.driver.implicitly_wait(5)

        self.lp.setCity(self.city)
        self.driver.implicitly_wait(5)

        self.lp.setCard(self.card)
        self.driver.implicitly_wait(5)

        self.lp.setMonth(self.month)
        self.driver.implicitly_wait(5)

        self.lp.setYear(self.year)
        self.driver.implicitly_wait(5)

        self.lp.clickButtonPurchase()
        self.driver.implicitly_wait(5)
        self.logger.info('****Order Successfully placed****')
        self.driver.save_screenshot('.\\screenshots\\screenshot.png')

        self.lp.printParagraph()
        self.driver.implicitly_wait(5)
        self.logger.info('****Printing Customer Order Details****')

        self.lp.clickOK()
        self.driver.implicitly_wait(5)

        self.driver.close()














































































