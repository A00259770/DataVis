from flask import Flask, render_template, request
from Vader import get_vader_tweets
from Sentiment import polarity, polarity1
from Textblob import get_blob_tweets
import tweepy as tp
from twitter_auth import *

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/both', methods=['GET'])
def page():
    return render_template('Both.html')


@app.route('/about', methods=['GET'])
def aboutpage():
    return render_template('about.html')


@app.route('/tweets', methods=['POST'])
def tweetspage():  # put application's code here
    title = 'Vader Analysis'
    desc = 'visualising sentiment'
    query = request.form.get('search')
    df = get_vader_tweets(query)
    pos, neg, nue = polarity(df)
    labels = ['positive', 'negative', 'neutral']
    values = [pos, neg, nue]
    data = zip(labels, values)
    list = []
    for label, value in data:
        list.append({'name': label, 'y': value})
    return render_template('index.html', title=title, description_text=desc, chart_name='Pie', data=list)


@app.route('/tweets1', methods=['POST'])
def tweetspage1():  # put application's code here
    title1 = 'Textblob Analysis'
    desc1 = 'visualising sentiment'
    query = request.form.get('search')
    df1 = get_blob_tweets(query)
    pos1, neg1, nue1 = polarity1(df1)
    labels1 = ['positive1', 'negative1', 'neutral1']
    values1 = [pos1, neg1, nue1]
    data1 = zip(labels1, values1)
    list1 = []
    for label1, value1 in data1:
        list1.append({'name': label1, 'y': value1})
    return render_template('index.html', title=title1, description_text=desc1, chart_name='Pie', data=list1)


@app.route('/tweets2', methods=['POST'])
def tweetspage2():  # put application's code here
    title = 'Vader Analysis'
    desc = 'visualising sentiment'
    query = request.form.get('search1')
    df = get_blob_tweets(query)
    pos, neg, nue = polarity(df)
    labels = ['positive', 'negative', 'neutral']
    values = [pos, neg, nue]
    data = zip(labels, values)
    list = []
    for label, value in data:
        list.append({'name': label, 'y': value})
    title1 = 'Textblob Analysis'
    desc1 = 'visualising sentiment'
    query = request.form.get('search')
    df1 = get_blob_tweets(query)
    pos1, neg1, nue1 = polarity1(df1)
    labels1 = ['positive1', 'negative1', 'neutral1']
    values1 = [pos1, neg1, nue1]
    data1 = zip(labels1, values1)
    list1 = []
    for label1, value1 in data1:
        list1.append({'name': label1, 'y': value1})
    return render_template('Both.html', title=title1, title1=title, description_text=desc1, description_text1=desc,
                           chart_name='Pie', chart_name1='Pie',
                           data=list1, data1=list)


if __name__ == '__main__':
    app.run()
