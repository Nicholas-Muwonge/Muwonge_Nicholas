import tweepy
import os
import schedule
import time
import logging
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

logging.basicConfig(level=logging.INFO)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, OPENAI_API_KEY]):
    logging.error("One or more environment variables are missing. Check your .env file.")
    exit()

auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
twitter_api = tweepy.API(auth)

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_tweet():
    prompt = "What is the impact of AI on today's learning and studies?"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        content = response.choices[0].message.content.strip()
        logging.info("Generated tweet: " + content)
        if len(content) > 280:
            logging.warning("Tweet too long, trimming to 280 characters.")
            content = content[:277] + "..."
        return content
    except Exception as e:
        logging.error("Error generating tweet:", exc_info=True)
        return "Stay curious. AI is shaping the future."

def post_tweet():
    tweet = generate_tweet()
    try:
        twitter_api.update_status(tweet)
        logging.info("Tweet posted successfully.")
    except Exception as e:
        logging.error("Failed to post tweet:", exc_info=True)

schedule.every().day.at("10:00").do(post_tweet)
schedule.every().day.at("18:00").do(post_tweet)

if __name__ == "__main__":
    logging.info("AI Social Poster started...")

    post_tweet()

    while True:
        schedule.run_pending()
        time.sleep(30)
