import requests
from bs4 import BeautifulSoup as bs

url ='https://www.weather-forecast.com/locations/Nyeri/forecasts/latest'
r=requests.get(url)

forecast=bs(r.content, 'lxml')

#wthr = forecast.findAll('div', {'class':'b-forecast__table-days-content'})
#for i in range(7):
 #   print(wthr[i].text)
#humidity
whtr1 = forecast.find('tr',{'class': 'b-forecast__table-humidity js-humidity'})
mywhtr2=whtr1.findAll('span',{'class':'b-forecast__table-value'})

for i in range(1,36):
    print(mywhtr2[i].text)

#high temperature
whtr2 = forecast.find("tr",{'class': 'b-forecast__table-max-temperature js-temp'})
mywhtr3 = whtr2.findAll('span',{'class': 'temp b-forecast__table-value'})

for i in range(1, 36):
    print(mywhtr3[i].text)