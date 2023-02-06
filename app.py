from flask import Flask, render_template
import os
import json

app = Flask(__name__)

# list of michael scott gifs
images = [
    "https://media.tenor.com/jRMy1IcB8agAAAAM/michael-scott-the-office.gif",
    "https://media.tenor.com/cmoCqxPpUMMAAAAM/michael-scott-the-office.gif",
    "https://media.tenor.com/3tkW6cG_0oQAAAAM/clearish-the-office.gif",
    "https://media.tenor.com/VUZSCMV2EkwAAAAM/the-office-what.gif",
    "https://media.tenor.com/ymuP54ZyMMkAAAAC/brave-face-the-office.gif",
    "https://media.tenor.com/M1a8cbcCmEgAAAAM/the-office-welcome.gif",
    "https://media.tenor.com/bUOrNPAXcMEAAAAd/the-office-michael-scott.gif",
    "https://media.tenor.com/YENRE_WSZMAAAAAC/the-office-michael.gif",
    "https://media.tenor.com/3iu27yMZvtsAAAAM/the-office-you-are-fired.gif",
    "https://media.tenor.com/bxzjcDX3fMQAAAAM/the-office.gif",
    "https://media.tenor.com/VM9vrNa18S4AAAAC/the-office-the.gif",
    "https://media.tenor.com/mKfeCtD5EukAAAAC/the-office-the.gif",
    "https://media.tenor.com/OYSc73yVxBIAAAAC/the-the-office.gif",
    "https://media.tenor.com/kWejy2kDcTwAAAAC/office.gif",
]

@app.route("/")
def index():
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
