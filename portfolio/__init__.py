from flask import Flask,     rendertemplate

app = Flask(__name__)

@app("/")
def home ():
    return rendertemplate("home.html")

@app("/about")
def about ():
    return rendertemplate("about.html")

@app("/contact")
def contact ():
    return rendertemplate("contact.html")