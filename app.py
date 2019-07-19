from flask import Flask, render_template, url_for, redirect, request
import json


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    try:
        data = open("data.json", "r")
        words = json.load(data)
        word = request.form["word"]
        if word in words:
            result = words[word]
            return render_template("index.html", result=result, word=word)
        elif word.upper() in words:
            result = words[word.upper()]
            return render_template("index.html", result=result, word=word)
        elif word.title() in words:
            result = words[word.title()]
            return render_template("index.html", result=result, word=word)
        elif word.upper() not in words:
            result = words[word.lower()]
            return render_template("index.html", result=result, word=word)



    except:
        message = "Word does not exist, try another word!"
        return render_template("index.html", message=message)
    welcome = "Please enter a word to get a meaning "
    return render_template("index.html", welcome=welcome)


if __name__ == "__main__":
    app.run(debug=True)
