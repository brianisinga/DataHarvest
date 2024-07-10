import requests
from bs4 import BeautifulSoup as bs

url ='https://www.weather-forecast.com/locations/Nyeri/forecasts/latest'
r=requests.get(url)

forecast=bs(r.content, 'lxml')

#wthr = forecast.findAll('div', {'class':'b-forecast__table-days-content'})
#for i in range(7):
 #   print(wthr[i].text)

whtr1 = forecast.find('tr',{'class': 'b-forecast__table-humidity js-humidity'})
mywhtr2=whtr1.findAll('span',{'class':'b-forecast__table-value'})

print(mywhtr2[0].text)
