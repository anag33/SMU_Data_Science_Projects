
def scrapemarsNews():
   
    # using splinter - dynamic url
    executable_path = {'executable_path': r'C:\Users\anagi\OneDrive\Desktop\Smu REAL\smu-dal-data-pt-03-2020-u-c\chromedriver_win32 (3)\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # visit url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
      #soupify
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    # pull the titles and articles using class 
    titles = mars.find_all(class_="content_title")
    articles = mars.find_all(class_="article_teaser_body")
    
    # find first title with link 
    first_title = ""
    for title in titles:
        if title.a:
            first_title = title
            break
            
    # Parse data       
    news_title = first_title.a.text.strip()
    news_link = "https://mars.nasa.gov" + first_title.a['href']
    news_article = articles[0].text.strip()
    
    
    
    #visit next URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
      #grab images
    images = soup.find_all(class_="carousel_item")
    imageURL = 'https://www.jpl.nasa.gov' + images[0]["style"].split(" ")[1].split("'")[1]
    
    
    # NAVIGATE TO NEXT WEBSITE 
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    #Get Weather
    allLinks_tweet = soup.find_all("span")
    tweetText = ""
    for tweet in allLinks_tweet:
        if tweet.text:
            if "InSight sol" in tweet.text:
                tweetText = tweet.text
                break
                
    allLinks_tweet = soup.find_all("a")
    tweetLink = ""
    for link in allLinks_tweet:
        if link['href']:
            if "status" in link["href"]:
                tweetLink = "https://www.twitter.com" + link["href"]
                break
    
    # NAVIGATE TO NEXT WEBSITE 
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    dfs = pd.read_html(html)
    stats = dfs[0]
    stats.columns = ["Attribute", "Value"]
    
    #format and save
    data_html = stats.to_html(index=False)
    data_stats = json.loads(stats.to_json(orient="records"))

    # Get Hemesphire Images 
    #visit URL
    executable_path = {'executable_path': r'C:\Users\anagi\OneDrive\Desktop\Smu REAL\smu-dal-data-pt-03-2020-u-c\chromedriver_win32 (3)\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False) 
    
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    hemisphere_urls = []
    
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        
        hemisphere = {}
    
        # Find Element on Each Loop to Avoid a Stale Element Exception
        browser.find_by_css("a.product-item h3")[item].click()
    
        # Find Sample Image Anchor Tag & Extract <href>
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
    
        # Get Hemisphere Title
        hemisphere["title"] = browser.find_by_css("h2.title").text
    
        # Append Hemisphere Object to List
        hemisphere_urls.append(hemisphere)
    
        # Navigate Backwards
        browser.back() 
    
    # close the browser
    browser.quit()
    
    # create rnt dictionary
    rtnDict = {
        "news_title": news_title,
        "news_link": news_link,
        "news_article": news_article,
        "featureImageURL": imageURL,
        "tweetWeatherURL": tweetLink,
        "tweetWeatherText": tweetText,
        "marsStatsHTML": data_html,
        "marsStats": data_stats,
        "dateScraped": datetime.now(),
        "hemispheres": hemisphere_urls
    }
    
    return rtnDict
    
    #close browser
    #browser.quit()