#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install selenium


# In[7]:


from selenium import webdriver


# In[8]:


from time import sleep


# In[9]:


from selenium.webdriver.common.by import By


# In[71]:


val=str(input("Enter Name of artist and song"))


# In[72]:


browser=webdriver.Chrome()
browser.get("https://www.ultimate-guitar.com/")
browser.maximize_window()
sleep(5)
button=browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/p[2]/form/button")
searchbar=browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/p[2]/form/div/input")
searchbar.send_keys(val)
sleep(2)
button.click()
tabbutton=browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/section/nav/div[1]/nav/a[3]')
tabbutton.click()
linktotabs=browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/section/article/div/div[4]/div[2]/header/span/span/a')
linktotabs.click()
tuning=browser.find_element(By.ID, "tuning")
print(tuning.text)

