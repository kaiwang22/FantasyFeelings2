from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import ssl
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import urljoin
from urllib.request import Request, urlopen
import requests
import pandas as pd
import datetime


def scrape_news(player_name):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )
    # specify url to scrape
    root = 'https://www.google.com/'
    query = player_name
    encoded_query = quote(query)
    link = f'https://news.google.com/search?q={encoded_query}&hl=en-US&gl=US&ceid=US%3Aen'

    req = Request(link, headers={'User-Agent': user_agent})
    webpage = urlopen(req, context=ssl_context).read()
    
    scraped_titles = []
    scraped_date = []

    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        for item in soup.find_all("h3", attrs={'class': 'ipQwMb ekueJc RD0gLb'}):
            text = item.get_text()
            text = text.replace(",", " ")
            scraped_titles.append(text)
    
        for time in soup.find_all('time', class_='WW6dff uQIVzc Sksgp slhocf'):
            datetime_value = time.get('datetime')
            scraped_date.append(datetime_value)

    df = pd.DataFrame({'Titles' : scraped_titles, 'Times' : scraped_date})

    analyzer = SentimentIntensityAnalyzer()

    score = []

    for n in range(df.shape[0]):
        title = df.iloc[n,0]
        title_analyzed = analyzer.polarity_scores(title)
        score.append(title_analyzed['compound'])

    df['Score'] = score
    df['Times'] = pd.to_datetime(df['Times'])

    return(df)

def current_feeling(df):
    current_datetime = datetime.datetime.now(datetime.timezone.utc)
    recent = current_datetime - datetime.timedelta(days=3)
    recent_df = df[df['Times'] > recent]
    mean_current_sentiment = recent_df['Score'].mean()

    return(mean_current_sentiment)