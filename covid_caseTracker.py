
import requests
from bs4 import BeautifulSoup
import sys
from  requests.exceptions import HTTPError

#asks the users for the country
area = input("Enter in lowercase the country that you want to know the num of cases. if you want to know for the world, Enter 'world'. if the country is not one word, seperate by - (united-states):  ")

#form the url

if area =="united-states" :
	url = "https://www.worldometers.info/coronavirus/country/us/"
elif  area=="united-kingdom":
	url = "https://www.worldometers.info/coronavirus/country/uk/"
elif area == "hong-kong":
	url = "https://www.worldometers.info/coronavirus/country/china-hong-kong-sar/"
elif area == "world":
	url = "https://www.worldometers.info/coronavirus/"
else:
	url = "https://www.worldometers.info/coronavirus/country/" +"".join(area) + "/"

#download the page with request
try:
	res = requests.get(url)
	res.raise_for_status()
except HTTPError:
	print("check if the name of the country is not wrong and is as i described.")
	print("if the problem persist, sorry!! there is no info about this country")
	sys.exit()
#parse the data with beautiful soup 
soup = BeautifulSoup(res.text, features="html.parser")
data_wanted = soup.select(".maincounter-number span")
if data_wanted == []:
    print("no data found!! check again if the name of the country is well written and is as i explain")
    print("if the problem persist, sorry!! there is no info about this country")
    sys.exit()
else:
    num_of_case = data_wanted[0].text
    num_of_death = data_wanted[1].text
    num_of_recovery = data_wanted[2].text
#printing the num of cases

print(area.upper())
print("Coronavirus Cases : " + str(num_of_case))
print("Deaths : " + str(num_of_death))
print("Recovered: " + str(num_of_recovery))