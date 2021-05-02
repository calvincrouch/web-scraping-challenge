import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)

    listings = {}

    # Iterate through most recent news articles
    for x in range(1):
    
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')        
        list_text = soup.find_all('div', class_='list_text')

        for list_ in list_text:
        
            title = list_.find("div", {"class": "content_title"}).get_text()
            paragraph = list_.find("div", {"class": "article_teaser_body"}).get_text()
            time.sleep(1)
            break

    print(f'{title}')
    print(f'{paragraph}')

    listings["article_title"] = title
    listings["paragraph"] = paragraph
   ################# 
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    time.sleep(1)

    
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find('img', class_='headerimage')

    # Retrieve src element
    src = (images['src'])

    featured_image_url = f"{jpl_url}{src}"

    print(f'{featured_image_url}')

    listings["featured_image_url"] = featured_image_url
  ##################  
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    time.sleep(1)

    # Read all tables using pandas
    tables = pd.read_html(facts_url)

    df = tables[0]

    df.columns = ['Description', 'Mars', 'Earth']

    # Generate HTML table string 
    html_table = df.to_html()

    html_table = html_table.replace('\n', '')

    print(f'{html_table}')

    listings["html_table"] = html_table
    
    ###################
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    time.sleep(1)

    html2 = browser.html
    # Parse HTML with Beautiful Soup
    soup2 = BeautifulSoup(html2, 'html.parser')
    divs = soup2.find_all('div', class_='item')

    href_list = []

    # Iterate through each div item
    for div in divs:        
        a = div.find('a')
        href = a['href']
        href_list.append(href)
    
    # Use href_list to scrape
    all_titles = []
    all_src = []
    for x in href_list:
    
        base_url = "https://marshemispheres.com/"
        urlH = f"{base_url}{x}"
        browser.visit(urlH)
    
        html3 = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html3, 'html.parser')
        anchors = soup.find_all('img', class_='wide-image')
        titles = soup.find_all('h2', class_='title')
    
        for ti in titles:
            title2 = ti.get_text()
            all_titles.append(title2)
            print('-----------')
            print(title2)
    
        # Iterate through each anchor
        for anchor in anchors:
            src = anchor['src']
            img_url = base_url + src
            all_src.append(img_url)
            print(f'{img_url}')
            

    # Create a dictionary using title and img_url lists
    hemisphere_image_urls = []
    for i, j in zip(all_titles, all_src):
        hemisphere_image_urls.append({"title": i, "img_url": j})

    print(f'{hemisphere_image_urls}')

    listings["hemisphere_image_urls"] = hemisphere_image_urls

    browser.quit()

    return listings
results = scrape()
print(results['hemisphere_image_urls'])
