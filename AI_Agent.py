import os
from openai import OpenAI  # type: ignore
import tweepy  # type: ignore
from dotenv import load_dotenv

load_dotenv()
print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_post(prompt):
    """Generate a social media post using OpenAI's GPT-3.5-turbo."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative social media assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def post_to_twitter(text):
    """Post the generated text to Twitter using Tweepy."""
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)

    try:
        api.update_status(status=text)
        print("✅ Successfully posted to Twitter.")
    except Exception as e:
        print(" Failed to post:", e)

def main():
    prompt = "Write a short tweet about how AI can boost productivity for students."
    post = generate_post(prompt)
    print("Generated Post:\n", post)
    post_to_twitter(post)

if __name__ == "__main__":
    main()
