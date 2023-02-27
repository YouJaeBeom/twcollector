import requests
from bs4 import BeautifulSoup

# Set up the search query
keyword = "bts"
url = f"https://twitter.com/search?q={keyword}&src=typed_query"

# Fetch the search results page
response = requests.get(url)

# Parse the HTML of the search results page
soup = BeautifulSoup(response.content, "html.parser")

# Collect the tweets from the search results
tweets = soup.find_all("div", {"class": "tweet"})

# Print out the tweets
for tweet in tweets:
    print(tweet.find("p", {"class": "tweet-text"}).text)