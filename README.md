# FantasyFeelings
## A site to track sentiment of NFL Players for Fantasy Football purposes!

Ever wondered when to trade or trade for a player in fantasy football? With FantasyFeelings, you can see the current public opinion of any NFL player and use that information to help inform your decision making througout the course of your NFL season!

FantasyFeelings works by scraping news articles of NFL players from GoogleNews and then runs the titles through a sentiment analysis model. It then displays all of the historical sentiment data in a graph that is easy-to-read!

Demo Video:[FantasyFeelingsDemo.zip](https://github.com/kaiwang22/FantasyFeelings/files/12448648/FantasyFeelingsDemo.zip)

Technologies used: 

- Beautiful Soup to scrape GoogleNews articles and all current NFL players
- Django for the backend (store all players and their corresponding teams, positions, and sentiment entries)
- React for the frontend (React Router and components)
- DJango Rest framework and axios to connect Django to React with an API
- Chart Js to create the sentiment graphs
- Vader Sentiment (pretrained) for generating sentiment scores for each news article

For the future:
- Fix player detail search bar loading bugs
- Style the website
- Add loading animations
- Explore other sentiment analysis models
- Explore scraping other options to provide a better picture of public opinion (Reddit, Instagram, TikTok, etc)
- Implement an AI to provide an analysis on whether or not users should trade/trade for a specific player

time spent: 15-20 hours (started this as a side project before the technical assessment)
