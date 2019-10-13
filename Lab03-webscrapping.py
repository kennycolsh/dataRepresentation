import requests
import csv

from bs4 import BeautifulSoup 

url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
page = requests.get(url)
soup1 = BeautifulSoup(page.content,'html.parser')

home_file = open('home_file.csv',mode='w')
home_writer = csv.writer(home_file, delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)

listings = soup1.findAll("div",class_ = "PropertyListingCard")

for listing in listings:
    entryList = []

    price = listing.find(class_ = "PropertyListingCard__Price").text
    entryList.append(price)

    address = listing.find(class_ = "PropertyListingCard__Address").text
    entryList.append(address)

    home_writer.writerow(entryList)


home_file.close()



#print(page)
print("-------------------")
#print(page.content)



print("-------------------------")
#print(soup1.prettify())

with open("../week2/View_Cars.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print("-------------------------")
#print(soup.prettify())
print("-------------------------")
#print(soup.tr) 
rows= soup.findAll("tr")
for row in rows:
    print("--------")
    print(row)
    print("---------")
    dataList =[]
    cols = row.findAll("td")
    
    for col in cols:
        dataList.append(col.text)
    
    print(dataList)


employee_file = open('employee_file.csv',mode='w')
employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['kenny colsh','IT','June'])
employee_writer.writerow(['Ann colsh,','IT','may'])

employee_file.close()

##Scrap live page


