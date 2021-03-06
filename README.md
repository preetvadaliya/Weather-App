<h1 align="center">
    W E A T H E R &nbsp;&nbsp; A P P
    <br>
    <img src="https://img.shields.io/static/v1?label=Made%20with&message=Python&color=red&logo=python&logoColor=white" />
    <img src="https://img.shields.io/static/v1?label=Python&message=3.7.7&color=red&logo=python&logoColor=white" />
    <img src="https://img.shields.io/static/v1?label=Use%20of&message=Web%20Scraping&color=red&logo=google-chrome&logoColor=white" />
    <img src="https://img.shields.io/static/v1?label=Made%20with&message=BeautifulSoup&color=red" />
</h1>
<p align="center">Simple python program to get real time weather data of your location.</p>

<br>
<br>

### How to use?
Download **WeatherApp.py** file and add into your project.

<br>

## E X A M P L E
```python

from WeatherApp import WeatherApp
app = WeatherApp("Your User Agent")

```

<br>

## M E T H O D S

### getLocation( )
Get your current location.
```python

app.getLocation()

```

<br>

### getTime( )
Get current time.
```python

app.getTime()

```

<br>

### getTemperature( )
Get temperature in C.
```python

app.getTemperature()

```

<br>

### getTemperatureInFahrenheit( )
Get temperature in F.
```python

app.getTemperatureInFahrenheit()

```

<br>

### getWeatherType( )
Get current weather type.
```python

app.getWeatherType()

```

<br>

### getPrecipitation( )
Get current precipitation.
```python

app.getPrecipitation()

```

<br>

### getHumidity( )
Get current humidity.
```python

app.getHumidity()

```

<br>

### getWindSpeed( )
Get current wind speed.
```python

app.getWindSpeed()

```

<br>