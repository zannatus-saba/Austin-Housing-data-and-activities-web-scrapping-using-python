
@author: zanna
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
import os
os.chdir('C:/Users/zanna/OneDrive/Documents/MSIS/twitter')
directory= 'C:/Users/zanna/OneDrive/Documents/MSIS/twitter'


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time  
from selenium.webdriver.edge.service import Service

import seaborn as sb # visualization
from termcolor import colored as cl # text customization

driver = webdriver.Edge(executable_path=r'C:\Users\zanna\OneDrive\Documents\MSIS-5193\edgedriver_win32\msedgedriver.exe')

housing_url = 'https://www.recenter.tamu.edu/data/housing-activity/#!/activity/County/Austin_County'
driver.get(housing_url)

people=driver.find_elements(By.CSS_SELECTOR, 'td.ng-binding.ng-scope')
people[0].text
temp_list=[]
for i in people:
    temp_list.append(i.text)

df11 = pd.DataFrame(temp_list)
df11=df11.drop(df11.index[0:48])
print(df11)


people1=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(2)')
people1[0].text
temp_list1=[]
for i in people1:
    temp_list1.append(i.text)
    
df12 = pd.DataFrame(temp_list1)    
df12=df12.drop(df12.index[0:48])
print(df12)


people2=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(3)')
people2[0].text
temp_list2=[]
for i in people2:
    temp_list2.append(i.text)
    
df13 = pd.DataFrame(temp_list2)     
df13=df13.drop(df13.index[0:48])
print(df13)

people3=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(4)')
people3[0].text
temp_list3=[]
for i in people3:
    temp_list3.append(i.text)
    
df14 = pd.DataFrame(temp_list3)  
df14=df14.drop(df14.index[0:48])
print(df14)


people4=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(4)')
people4[0].text
temp_list4=[]
for i in people4:
    temp_list4.append(i.text)
    
df15 = pd.DataFrame(temp_list4)  
df15=df15.drop(df15.index[0:48])
print(df15)




people5=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(6)')
people5[0].text
temp_list5=[]
for i in people5:
    temp_list5.append(i.text)
    
df16 = pd.DataFrame(temp_list5) 
df16=df16.drop(df16.index[0:48])
print(df16)

people6=driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope>td:nth-child(7)')
people6[0].text
temp_list6=[]
for i in people6:
    temp_list6.append(i.text)
    
df17 = pd.DataFrame(temp_list6) 
df17=df17.drop(df17.index[0:48])
print(df17)

result = pd.concat([df11, df12, df13, df14, df15], axis=1, join='inner')
result.columns =['Date', 'Sale', 'Dollar Volume', 'Average Price', 'Median Price']



df8 = pd.concat([df16, df17], axis=1, join='inner')
df8.columns=['Total listing', 'Months inventory']
df8 = df8.join(result["Date"])
extracted_col = df8["Total listing"]
extracted_col1 = df8["Months inventory"]
result = result.join(extracted_col)
result = result.join(extracted_col1)
result=result.set_index('Date')
result.columns


####Saving file as "austindata.csv"

result.to_csv(r'C:\Users\zanna\OneDrive\Documents\MSIS\twitter\austindata.csv')
os.chdir('C:/Users/zanna/OneDrive/Documents/MSIS/twitter')
directory= 'C:/Users/zanna/OneDrive/Documents/MSIS/twitter'

data1 = pd.read_csv("austindata.csv")
data1.columns
print(data1.dtypes)


#Converting object to float (remove commas)
data1['Dollar Volume']=data1['Dollar Volume'].str.replace(',', '').astype(float)
data1['Average Price']=data1['Average Price'].str.replace(',', '').astype(float)
data1['Median Price']=data1['Median Price'].str.replace(',', '').astype(float)

data1.head()
#data1=data1.set_index('Date')

data1.columns
data1.describe()


#visualize average price

from datetime import datetime
from matplotlib import pyplot as plt, dates as mdates
x=data1['Date']
y=data1['Average Price']
plt.plot(x,y)
fig = plt.gcf()
fig.set_size_inches(20.5, 15.5)
fig.set_dpi(80)
plt.xticks(rotation=90)
plt.title('Average Price')
plt.xlabel('date')
plt.ylabel('Avg price')
plt.show()


#visualize listing counts

x=data1['Date']
m=data1['Total listing']
plt.bar(x,m)
fig = plt.gcf()
fig.set_size_inches(20.5, 15.5)
fig.set_dpi(80)
plt.xticks(rotation=90)
plt.title('House listing counts')
plt.xlabel('date')
plt.ylabel('Listing counts')
plt.show()
