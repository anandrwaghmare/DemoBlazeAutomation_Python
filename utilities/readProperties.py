import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getName():
        name = config.get('common info', 'name')
        return name

    @staticmethod
    def getCountry():
        country = config.get('common info', 'country')
        return country

    @staticmethod
    def getCity():
        city = config.get('common info', 'city')
        return city

    @staticmethod
    def getCard():
        card = config.get('common info', 'card')
        return card

    @staticmethod
    def getMonth():
        month = config.get('common info', 'month')
        return month

    @staticmethod
    def getYear():
        year = config.get('common info', 'year')
        return year

