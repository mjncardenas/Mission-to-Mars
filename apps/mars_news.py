def mars_news():
    #Visit the mars news site
    url = 'https://mars.nasa.gov/news/'
    browse.visit(url)

    #Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('ul.item_list li.slide')
    slide_elem.find("div", class_='content_title')

    # Use the parent element to find the first <a> tag and save it as  `news_title`
    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

return news_title, news_p
    # Add try/except for error handling
try:
    slide_elem = news_soup.select_one("ul.item_list li.slide")
    # Use the parent element to find the first 'a' tag and save it as 'news_title'
    news_title = slide_elem.find("div", class_="content_title").get_text()
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
except AttributeError:
    return None, None
def featured_image(browser):
  return img_url
try:
    img_url_rel = img_soup.select_one('figure.lede a img').get("src)

except AttributeError:
    return None