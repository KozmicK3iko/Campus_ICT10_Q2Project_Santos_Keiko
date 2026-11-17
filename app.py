from flask import Flask, render_template, jsonify

app = Flask(__name__)


CONTENT_DATA = {
    "creator": {
        "title": "MEET THE CREATOR",
        "text": "Welcome to my Sonic-themed web app! Built with Python (Flask), HTML, and CSS."
    },
    "club": {
        "title": "CLUB CHECKER",
        "text": "Welcome to the Speed Club! Enter your Python club-checking logic here."
    },
    "facts": {
        "title": "SONIC FUN FACTS",
        "text": "Sonic's original code name was 'Mr. Needlemouse', and he was designed to run faster than the speed of sound!"
    },
    "element": {
        "title": "ELEMENT CHECKER",
        "text": "Ready to inspect elements! Connect your Python element lookup script here."
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info/<topic>")
def get_info(topic):
    return jsonify(CONTENT_DATA.get(topic, {"title": "Info", "text": "No details found."}))

if __name__ == "__main__":
    app.run(debug=True)