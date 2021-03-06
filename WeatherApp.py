import requests
from bs4 import BeautifulSoup


class WeatherApp:

    def __init__(self, user_Agent):
        """
        Create Weather object.
        ---
        user_Agent: your browser aget.\n
        search into chrom for your agent.
        """
        self.url = "https://rb.gy/eepurb"
        self.header = {"User-Agent": user_Agent}
        content = requests.get(self.url, headers=self.header).content
        self.pageSource = BeautifulSoup(content, "html.parser")

    def getLocation(self):
        """
        Get your current location.
        """
        return self.pageSource.find(id="wob_loc").get_text()

    def getTime(self):
        """
        Get current time
        """
        return self.pageSource.find(id="wob_dts").get_text()

    def getTemperature(self):
        """
        Get temperature in C.
        """
        return self.pageSource.find(id="wob_tm").get_text()

    def getTemperatureInFahrenheit(self):
        """
        Get temperature in F.
        """
        return self.pageSource.find(id="wob_ttm").get_text()

    def getWeatherType(self):
        """
        Get current weather type.\n
        ex. cloudy
        """
        return self.pageSource.find(id="wob_dc").get_text()

    def getPrecipitation(self):
        """
        Get current precipitation.
        """
        return self.pageSource.find(id="wob_pp").get_text()

    def getHumidity(self):
        """
        Get current humidity.
        """
        return self.pageSource.find(id="wob_hm").get_text()

    def getWindSpeed(self):
        """
        Get current wind speed.
        """
        return self.pageSource.find(id="wob_ws").get_text()
