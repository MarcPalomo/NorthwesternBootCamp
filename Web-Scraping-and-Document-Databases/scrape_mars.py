#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver
from urllib.parse import urlsplit

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_data = {}

    Mars_NASA = "https://mars.nasa.gov/news/"
    browser.visit(Mars_NASA)
    time.sleep(2)

    html = browser.html
    soup = bs(html,"html.parser")

    #scrape the latest News Title and Paragraph Text into variables
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    
    #JPL Mars Space Images - Featured Image: Mars
    #visiting the next page
    url_mars_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_mars_image)
    
    #Getting the base url in order to get the path for this particular page
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_mars_image))
    
    #Design an xpath selector to grab the image. This will allow
    #for me to direct to the same first picture in the search
    #even if the picture changes. Used inspector to locate pathway.
    xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"
    
    #Use splinter to click on the mars featured image
    #to bring the full resolution image
    results = browser.find_by_xpath(xpath)
    mars_img = results[0]
    mars_img.click()
    time.sleep(2)

    #get image url using BeautifulSoup
    html_image = browser.html
    soup = bs(html_image, "html.parser")
    mars_img_url = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url = base_url + mars_img_url
    
    
    mars_data["featured_image"] = featured_image_url
    
    #Mars Weather Twitter Account

    #get mars weather's latest tweet from the website
    url_mars_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_mars_weather)
    time.sleep(2)
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather_tweet = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_data["mars_weather"] = mars_weather_tweet

    #Mars Facts

    url_mars_facts = "https://space-facts.com/mars/"
    time.sleep(2)
    facts_table = pd.read_html(url_mars_facts)
    facts_table[0]

    
    mars_facts_df = facts_table[0]
    mars_facts_df.columns = ["Parameter", "Values"]
    mars_facts_df.set_index(["Parameter"])

    
    mars_html_table = mars_facts_df.to_html(index=False)
    mars_html_table = mars_html_table.replace("\n", "")
    mars_data["mars_facts_table"] = mars_html_table

    #Mars Hemispheres

    url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_hemispheres)
    time.sleep(1)

    #Getting the base url
    hemispheres_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_mars_hemispheres))
    hemispheres_dict = []


    #Cerberus Hemisphere

    #navigate to the large picture image and display the soup results to find picture
    #use random time.sleep to mimic human clicks
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    
    #identify the picture url and save as a variable
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemispheres_base_url + cerberus_url
    
    #identify the picture title and save as a variable
    cerberus_title = soup.find("h2",class_="title").text
    #append the dictionary to add the image title and the image url
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemispheres_dict.append(cerberus)


    #Schiaparelli Hemisphere
    #select and go to the next website
    url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_hemispheres)
    time.sleep(1)
    
    #navigate to the large picture image and display the soup results to find picture
    #use random time.sleep to mimic human clicks
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    
    #identify the picture url and save as a variable
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemispheres_base_url + schiaparelli_url
    
    #identify the picture title and save as a variable
    schiaparelli_title = soup.find("h2",class_="title").text
    
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemispheres_dict.append(schiaparelli)
    
    

    # #### Syrtis Major Hemisphere

    #select and go to the next website
    url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_hemispheres)

    #navigate to the large picture image and display the soup results to find picture
    #use random time.sleep to mimic human clicks
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")

    #identify the picture url and save as a variable
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemispheres_base_url + syrtis_major_url
    
    #identify the picture title and save as a variable
    syrtis_major_title = soup.find("h2",class_="title").text
    
    #append the dictionary to add the image title and the image url
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemispheres_dict.append(syrtis_major)

    # #### Valles Marineris Hemisphere

    #select and go to the next website
    url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_hemispheres)

    #navigate to the large picture image and display the soup results to find picture
    #use random time.sleep to mimic human clicks
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    
    #identify the picture url and save as a variable
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemispheres_base_url + syrtis_major_url
    
    #identify the picture title and save as a variable
    valles_marineris_title = soup.find("h2",class_="title").text

    #append the dictionary to add the image title and the image url
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemispheres_dict.append(valles_marineris)

    mars_data["hemisphere_img_url"] = hemispheres_dict

    # Close the browser after scraping
    browser.quit()

    return mars_data