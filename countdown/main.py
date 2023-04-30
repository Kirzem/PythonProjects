# From Bing chat 04/28/23: Display real time countdown clock to date/time specified in config.txt
# output to a web page

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    with open('config.txt') as f:
        date_str = f.readline().strip()
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    diff = date - now
    return render_template('index.html', diff=diff)
    print("Time remaining:", diff)
if __name__ == '__main__':
    app.run(debug=True)
#index()