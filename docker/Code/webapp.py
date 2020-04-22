import os 
from flask import Flask
from flask import render_template
app = Flask(__name__)

color = 'red'

@app.route('/')
def main():
    print(color)
    return color

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "8080")