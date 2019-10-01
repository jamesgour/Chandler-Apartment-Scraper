
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
from time import sleep
import datetime
from bs4 import BeautifulSoup
import pynput.mouse as ms
import pynput.keyboard as kb

mouse = ms.Controller()
keyboard = kb.Controller()


# In[2]:


# Load Selenium Webdriver
driver = webdriver.Chrome(r'C:\Users\jcgou\Desktop\Apartment Scraper\Chrome Driver\chromedriver.exe')
print('Loading Selenium Webdriver')


# In[3]:


# Create CSV file for the pricing information
filename = 'Chandler Apartment Pricing.csv'
f = open(filename, 'a')
#headers = 'Date, Apartment Complex Name, Unit, Price\n'
#f.write(headers)


# In[4]:


# Record Today's date
date_object = datetime.date.today()
print("Today's date is: " + str(date_object))


# In[5]:


# Navigate to 1st Apartment website - San Brisas
san_brisas_url = 'https://www.sanbrisasapts.com/floor-plans.aspx'
driver.get(san_brisas_url)
driver.maximize_window()
print('Maximizing Chrome Driver')


# In[6]:


# Save HTML and extract portfolio recommendation information
san_brisas_html = driver.page_source
san_brisas_soup = BeautifulSoup(san_brisas_html, 'lxml')

# Extract apartment A2 price
san_brisas_a2_price = san_brisas_soup.find(id = 'fp_6830196_range').get_text()
print("The San Brisas A2 price is currently " + san_brisas_a2_price)
san_brisas_a2_price = san_brisas_a2_price.replace(',', '')


# In[7]:


# Write San Brisas prices to CSV file
f.write(str(date_object) + ',' + 'San Brisas' + ',' + 'A2' + ',' + str(san_brisas_a2_price) + '\n')
print('San Brisas prices written')


# In[8]:


# Navigate to 2nd apartment website
country_brook_url = 'https://countrybrook.mgproperties.com/brochure.aspx'
driver.get(country_brook_url)
print('Navigating to next apartment, Country Brook')


# In[9]:


# Save HTML and extract portfolio recommendation information
country_brook_html = driver.page_source
country_brook_soup = BeautifulSoup(country_brook_html, 'lxml')


# In[10]:


unit_list = []
price_list = []

table = country_brook_soup.table
table_rows = table.find_all('tr')
for tr in table_rows[1:7]:
    td = tr.find_all('td')
    row = [i.text for i in td]
    unit_list.append(row[1])
    price_list.append(row[5])
    #print(row)
    
final_unit_list = []
    
for i in unit_list:
    final_unit_list.append(i.strip())

country_brook_dict = dict(zip(final_unit_list, price_list))
print("The Country Brook prices are currently: ")
print(country_brook_dict)


# In[11]:


# Write Country Brook prices to CSV file

cb_a1_price = country_brook_dict['A1'].replace(',','')
cb_a2_price = country_brook_dict['A2'].replace(',','')
cb_a3_price = country_brook_dict['A3'].replace(',','')
cb_a4_price = country_brook_dict['A4'].replace(',','')
cb_b1_price = country_brook_dict['B1'].replace(',','')
cb_b2_price = country_brook_dict['B2'].replace(',','')

f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'A1' + ',' + str(cb_a1_price) + '\n')
f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'A2' + ',' + str(cb_a2_price) + '\n')
f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'A3' + ',' + str(cb_a3_price) + '\n')
f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'A4' + ',' + str(cb_a4_price) + '\n')
f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'B1' + ',' + str(cb_b1_price) + '\n')
f.write(str(date_object) + ',' + 'Country Brook' + ',' + 'B2' + ',' + str(cb_b2_price) + '\n')
print('Country Brook prices written')


# In[12]:


# Navigate to 3rd apartment website
san_tierra_url = 'https://www.liveatsantierra.com/floorplans'
driver.get(san_tierra_url)
print('Navigating to next apartment, San Tierra')


# In[13]:


# Save HTML and extract portfolio recommendation information
san_tierra_html = driver.page_source
san_tierra_soup = BeautifulSoup(san_tierra_html, 'lxml')


# In[14]:


# Extract apartment price 1 bed 1 bath 801 sqft
san_tierra_1x1_price = san_tierra_soup.find(id = '2391451').get_text()
san_tierra_1x1_price = san_tierra_1x1_price.split()
san_tierra_1x1_part_a = san_tierra_1x1_price[0:6]

san_tierra_1x1_part_a = "".join(san_tierra_1x1_price)[0:20]
print(san_tierra_1x1_part_a)

san_tierra_1x1_part_b = san_tierra_1x1_price[15]
print(san_tierra_1x1_part_b)
san_tierra_1x1_part_b = san_tierra_1x1_part_b.replace(',', '')
san_tierra_1x1_part_b = san_tierra_1x1_part_b.replace('.00', '')


# In[15]:


# Extract apartment price 2 bed 2 bath 1005 sqft
san_tierra_2x2a_price = san_tierra_soup.find(id = '2391452').get_text()
san_tierra_2x2a_price = san_tierra_2x2a_price.split()
san_tierra_2x2a_part_a = san_tierra_2x2a_price[0:6]

san_tierra_2x2a_part_a = "".join(san_tierra_2x2a_price)[0:20]
print(san_tierra_2x2a_part_a)

san_tierra_2x2a_part_b = san_tierra_2x2a_price[15]
print(san_tierra_2x2a_part_b)
san_tierra_2x2a_part_b = san_tierra_2x2a_part_b.replace(',', '')
san_tierra_2x2a_part_b = san_tierra_2x2a_part_b.replace('.00', '')


# In[16]:


# Extract apartment price 2 bed 2 bath 1050 sqft
san_tierra_2x2b_price = san_tierra_soup.find(id = '2391453').get_text()
san_tierra_2x2b_price = san_tierra_2x2b_price.split()
san_tierra_2x2b_part_a = san_tierra_2x2b_price[0:6]

san_tierra_2x2b_part_a = "".join(san_tierra_2x2b_price)[0:20]
print(san_tierra_2x2b_part_a)

san_tierra_2x2b_part_b = san_tierra_2x2b_price[15]
print(san_tierra_2x2b_part_b)
san_tierra_2x2b_part_b = san_tierra_2x2b_part_b.replace(',', '')
san_tierra_2x2b_part_b = san_tierra_2x2b_part_b.replace('.00', '')


# In[17]:


# Extract apartment price 2 bed 2 bath 1082 sqft
san_tierra_2x2c_price = san_tierra_soup.find(id = '2391454').get_text()
san_tierra_2x2c_price = san_tierra_2x2c_price.split()
san_tierra_2x2c_part_a = san_tierra_2x2c_price[0:6]

san_tierra_2x2c_part_a = "".join(san_tierra_2x2c_price)[0:20]
print(san_tierra_2x2c_part_a)

san_tierra_2x2c_part_b = san_tierra_2x2c_price[15]
print(san_tierra_2x2a_part_b)
san_tierra_2x2c_part_b = san_tierra_2x2c_part_b.replace(',', '')
san_tierra_2x2c_part_b = san_tierra_2x2c_part_b.replace('.00', '')


# In[18]:


# Write San Tierra prices to CSV file
f.write(str(date_object) + ',' + 'San Tierra' + ',' + str(san_tierra_1x1_part_a) + ',' + str(san_tierra_1x1_part_b) + '\n')
f.write(str(date_object) + ',' + 'San Tierra' + ',' + str(san_tierra_2x2a_part_a) + ',' + str(san_tierra_2x2a_part_b) + '\n')
f.write(str(date_object) + ',' + 'San Tierra' + ',' + str(san_tierra_2x2b_part_a) + ',' + str(san_tierra_2x2b_part_b) + '\n')
f.write(str(date_object) + ',' + 'San Tierra' + ',' + str(san_tierra_2x2c_part_a) + ',' + str(san_tierra_2x2c_part_b) + '\n')
print('San Tierra prices written')


# In[19]:


# Navigate to 4th apartment website
reflections_gilasprings_url = 'https://www.reflectionsatgilasprings.com/floorplans'
driver.get(reflections_gilasprings_url)
print('Navigating to next apartment, Reflections at Gila Springs')


# In[20]:


# Save HTML and extract portfolio recommendation information
reflections_gilasprings_html = driver.page_source
reflections_gilasprings_soup = BeautifulSoup(reflections_gilasprings_html, 'lxml')


# In[21]:


# Extract apartment price 1 bed 1 bath 824 sqft
reflections_1x1a_price = reflections_gilasprings_soup.find(id = '2421640').get_text()
reflections_1x1a_price = reflections_1x1a_price.split()
reflections_1x1a_part_a = reflections_1x1a_price[0:6]

reflections_1x1a_part_a = "".join(reflections_1x1a_price)[0:20]
print(reflections_1x1a_part_a)

reflections_1x1a_part_b = reflections_1x1a_price[14]
print(reflections_1x1a_part_b)
reflections_1x1a_part_b = reflections_1x1a_part_b.replace(',', '')
reflections_1x1a_part_b = reflections_1x1a_part_b.replace('.00', '')


# In[22]:


# Extract apartment price 1 bed 1 bath 949 sqft
reflections_1x1b_price = reflections_gilasprings_soup.find(id = '2421641').get_text()
reflections_1x1b_price = reflections_1x1b_price.split()
reflections_1x1b_part_a = reflections_1x1b_price[0:6]

reflections_1x1b_part_a = "".join(reflections_1x1b_price)[0:20]
print(reflections_1x1b_part_a)

reflections_1x1b_part_b = reflections_1x1b_price[14]
print(reflections_1x1b_part_b)
reflections_1x1b_part_b = reflections_1x1b_part_b.replace(',', '')
reflections_1x1b_part_b = reflections_1x1b_part_b.replace('.00', '')


# In[23]:


# Extract apartment price 2 bed 2 bath 1186 sqft
reflections_2x2a_price = reflections_gilasprings_soup.find(id = '2421643').get_text()
reflections_2x2a_price = reflections_2x2a_price.split()
reflections_2x2a_part_a = reflections_2x2a_price[0:6]

reflections_2x2a_part_a = "".join(reflections_2x2a_price)[0:20]
print(reflections_2x2a_part_a)

reflections_2x2a_part_b = reflections_2x2a_price[14]
print(reflections_2x2a_part_b)
reflections_2x2a_part_b = reflections_2x2a_part_b.replace(',', '')
reflections_2x2a_part_b = reflections_2x2a_part_b.replace('.00', '')


# In[24]:


# Extract apartment price 2 bed 2 bath 1156 sqft
reflections_2x2b_price = reflections_gilasprings_soup.find(id = '2421642').get_text()
reflections_2x2b_price = reflections_2x2b_price.split()
reflections_2x2b_part_a = reflections_2x2b_price[0:6]

reflections_2x2b_part_a = "".join(reflections_2x2b_price)[0:20]
print(reflections_2x2b_part_a)

reflections_2x2b_part_b = reflections_2x2b_price[14]
print(reflections_2x2b_part_b)
reflections_2x2b_part_b = reflections_2x2b_part_b.replace(',', '')
reflections_2x2b_part_b = reflections_2x2b_part_b.replace('.00', '')


# In[25]:


# Write Reflections prices to CSV file
f.write(str(date_object) + ',' + 'Reflections at Gila Springs' + ',' + str(reflections_1x1a_part_a) + ',' + str(reflections_1x1a_part_b) + '\n')
f.write(str(date_object) + ',' + 'Reflections at Gila Springs' + ',' + str(reflections_1x1b_part_a) + ',' + str(reflections_1x1b_part_b) + '\n')
f.write(str(date_object) + ',' + 'Reflections at Gila Springs' + ',' + str(reflections_2x2a_part_a) + ',' + str(reflections_2x2a_part_b) + '\n')
f.write(str(date_object) + ',' + 'Reflections at Gila Springs' + ',' + str(reflections_2x2b_part_a) + ',' + str(reflections_2x2b_part_b) + '\n')
print('Reflections at Gila Springs prices written')


# In[26]:


# Navigate to 5th apartment website
the_ventura_url = 'https://www.theventuraapts.com/Floor-plans.aspx'
driver.get(the_ventura_url)
print('Navigating to last apartment, The Ventura')


# In[27]:


# Save HTML and extract portfolio recommendation information
the_ventura_html = driver.page_source
the_ventura_soup = BeautifulSoup(the_ventura_html, 'lxml')


# In[28]:


# Extract apartment A1 price 1 bed 1 bath 798 sqft
ventura_1x1_price = the_ventura_soup.find(id = 'floorplan_7459888').get_text()
ventura_1x1_price = ventura_1x1_price.split()
ventra_1x1_part_a = ventura_1x1_price[1:8]

ventura_1x1_part_a = "".join(ventura_1x1_price)[12:33]
print(ventura_1x1_part_a)

ventura_1x1_part_b = ventura_1x1_price[10:13]
ventura_1x1_part_b = "".join(ventura_1x1_part_b)
ventura_1x1_part_b = ventura_1x1_part_b.replace(',','')
print(ventura_1x1_part_b)


# In[29]:


# Extract apartment B2 price 1 bed 1 bath 1039 sqft
ventura_2x2_price = the_ventura_soup.find(id = 'floorplan_7459889').get_text()
ventura_2x2_price = ventura_2x2_price.split()
ventra_2x2_part_a = ventura_2x2_price[1:10]

ventura_2x2_part_a = "".join(ventura_2x2_price)[12:35]
ventura_2x2_part_a = ventura_2x2_part_a.replace(',','')
print(ventura_2x2_part_a)

ventura_2x2_part_b = ventura_2x2_price[10]
ventura_2x2_part_b = ventura_2x2_part_b.replace(',', '')
print(ventura_2x2_part_b)


# In[30]:


# Write Ventura prices to CSV file
f.write(str(date_object) + ',' + 'The Ventura' + ',' + str(ventura_1x1_part_a) + ',' + str(ventura_1x1_part_b) + '\n')
f.write(str(date_object) + ',' + 'The Ventura' + ',' + str(ventura_2x2_part_a) + ',' + str(ventura_2x2_part_b) + '\n')
print('The Ventura prices written')


# In[31]:


print("Finished!")
exit()

