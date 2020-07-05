#Dependencies
from bs4 import BeautifulSoup
#import requests
import pandas as pd
from splinter import Browser
from datetime import datetime
import json


def scrapemarsNews():
    #Using Splinter - dynamic URL
    executable_path = {'executable_path': r'C:\Users\anagi\OneDrive\Desktop\Smu REAL\smu-dal-data-pt-03-2020-u-c\chromedriver_win32 (3)\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    #visit URL - Nasa Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    #soupify
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    #Pull the classes we want
    titles = soup.find_all(class_="content_title")
    texts = soup.find_all(class_="article_teaser_body")
    
    # Find the first title with an actual link.
    firstTitle = "" 
    for title in titles:
        if title.a: 
            firstTitle = title
            break
    
    # Parse information we want
    newsTitle = firstTitle.a.text.strip()
    newsLink = "https://mars.nasa.gov" + firstTitle.a['href']
    newsText = texts[0].text.strip()
    
    # NAVIGATE TO NEXT WEBSITE HERE
    #visit URL - Nasa Space Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    #grab images
    images = soup.find_all(class_="carousel_item")
    imageURL = 'https://www.jpl.nasa.gov' + images[0]["style"].split(" ")[1].split("'")[1]
    
    # NAVIGATE TO NEXT WEBSITE 
    #visit URL - Mars Twitter
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    #Get Weather
    allTweets_Maybe = soup.find_all("span")
    tweetText = ""
    for tweet in allTweets_Maybe:
        if tweet.text:
            if "InSight sol" in tweet.text:
                tweetText = tweet.text
                break
                
    allLinks_Maybe = soup.find_all("a")
    tweetLink = ""
    for link in allLinks_Maybe:
        if link['href']:
            if "status" in link["href"]:
                tweetLink = "https://www.twitter.com" + link["href"]
                break
    
    # NAVIGATE TO NEXT WEBSITE 
    #visit URL - Mars Facts
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    dfs = pd.read_html(html)
    stats = dfs[0]
    stats.columns = ["Attribute", "Value"]
    
    #format and save
    data_html = stats.to_html(index=False)
    data_stats = json.loads(stats.to_json(orient="records"))
     
    # close the browser
    #browser.quit()
  

    # GET NEW INFORMATION HERE    
    #visit URL - Hemesphire Images

    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)


    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items: 
        # Store title
        title = i.find('h3').text
    
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
    
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
    
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
    
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

        # Display hemisphere_image_urls
        hemisphere_image_urls

       # close the browser
        browser.quit()
    
        rtnDict = {
            "newsTitle": newsTitle,
            "newsLink": newsLink,
            "newsText": newsText,
            "featureImageURL": imageURL,
            "tweetWeatherURL": tweetLink,
            "tweetWeatherText": tweetText,
            "marsStatsHTML": data_html,
            "marsStats": data_stats,
            "hemisphere_image_urls": hemisphere_image_urls,
            "dateScraped": datetime.now()
        }
    
        return rtnDict