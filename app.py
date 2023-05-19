import os
from datetime import datetime
from post_tweet import post_tweet
import openai
import pytz
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route("/", methods=("GET", "POST"))
def index():
    try:
        if request.method == "POST":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=generate_prompt(),
                temperature=0.8,
            )
            post_tweet(response.choices[0].message.content[0:280])
            return redirect(url_for("index", result=response.choices[0].message.content))
        result = request.args.get("result")
        return render_template("index.html", result=result)
    except openai.error.APIError as e:
        return render_template("index.html", result=e)
    except Exception as e:
        return render_template("index.html", result=e)

def generate_prompt():
    timezone = pytz.timezone('America/Los_Angeles')
    date = datetime.now(tz=timezone)
    date = date.strftime("%B %d %Y")
    return [
        {"role": "system", "content": "You are a feminist activist who wants to educate citizens of the United States of America about abortion rights."},
        {"role": "user", "content": """Generate a text with 280 character limit that summarizes news on {} about abortion rights.""".format(date)},
        {"role": "assistant", "content": "Be very specific and keep under 280 characters. For example, you may include names of politicians, states, names of new law, etc."},
    ]