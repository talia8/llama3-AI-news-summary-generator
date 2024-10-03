from groq import Groq
from newsapi import NewsApiClient
from datetime import datetime
from newspaper import Article, Config

client = Groq(
    api_key = <your_api_key>
)

newsapi = NewsApiClient(<your_api_key>)

# Set up a config with a user-agent
config = Config()
config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

def summarize(news_articles):
    summary_response = ""
    
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "As a professional summarizer, "
                + "summarize each of the following news articles in a maximum of 1 bullet point for each article."
                + news_articles 
                + "Adhere to these principles:"
                + "Don't use markdown, just a plain text."
                + "Craft a summary that is detailed and concise,"
                + "Incorporate main ideas and essential information, "
                + "Eliminate extraneous language and focusing on critical aspects."
                + "Rely strictly on the provided text, without including external information."
                + "Format the summary in bullet points starting each bullet point with '*' for easy understanding."
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )
    
    # Iterate over the response chunks
    for chunk in completion:
        # Append the chunk content to the summary response
        summary_response += (chunk.choices[0].delta.content or "")
    
    # Return the complete summary as a string
    return summary_response

def process_news(top_headlines):
    text=""
    if top_headlines['status'] == 'ok' and top_headlines['articles']:
            articles = top_headlines['articles']
            articles = articles[:5]
            for article in articles:
                url = article['url']
                try:
                    article = Article(url, config=config)
                    article.download()
                    article.parse()
                    text += article.text
                except Exception as e:
                    print(f"Error: {e}")
                    pass
    else:
        print("no news found.")
        print(top_headlines)
    return text    
    
def create_news_summary(query):
    now = datetime.now().strftime("%Y-%m-%d")
    
    top_headlines = newsapi.get_everything(q=query, 
                                        from_param='2024-09-03',
                                        to=now,
                                        language='en',
                                        sort_by='relevancy',
                                        page=1)
    
    articles = process_news(top_headlines)
    
    if articles:
        return summarize(articles)
    
    else:
        return 'no news found'
     