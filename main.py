from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def home():
    render_template('home.html')