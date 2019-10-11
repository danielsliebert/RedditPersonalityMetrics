![Amazon Logo](https://i.imgur.com/FkTNPN8.png)

# RedditPersonalityMetrics

RedditPersonalityMetrics is a tool for analyzing a Reddit user's personality by feeding scraping and feeding their comments into IBM Watson Personality Insights api. Personality Insights returns various dimensions of personality analyzed from the text like extroversion, openness, conscientious, and neuroticism.

Ordinarily IBM Watson Insights requires you manually copy and paste a length page of text in order to get an accurate understanding of the user's personality. This tool expands the capabilities by letting you reference a user's complete Reddit comment history as a source of their personality metrics. The process is extremely simple and performed with a single command.


# Usage

python commentScrape.py [username] 

(Analysis can be found in [username].text) 
