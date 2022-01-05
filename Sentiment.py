import pandas as pd
from matplotlib import pyplot as plt


def polarity(tweets):
    return (tweets['sentiment'] > .25).sum(), (tweets['sentiment'] < -.25).sum(), (
        tweets['sentiment'].between(-.25, .25)).sum()


def polarity1(tweets1):
    return (tweets1['sentiment'] > .25).sum(), (tweets1['sentiment'] < -.25).sum(), (
        tweets1['sentiment'].between(-.25, .25)).sum()


def display_graph(p, n, neu):
    labels = ['positive', 'negative', 'neutral']
    values = [p, n, neu]
    plt.title('Sentiment Analysis')
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.show()


def display_graph1(p1, n1, neu1):
    labels1 = ['positive', 'negative', 'neutral']
    values1 = [p1, n1, neu1]
    plt.title('Sentiment Analysis')
    plt.pie(values1, labels=labels1, autopct='%1.1f%%')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('output.csv')
    df1 = pd.read_csv('output1.csv')
    df.set_index('id', inplace=True)
    df1.set_index('id1', inplace=True)
    positive, negative, neutral = polarity(df)
    positive1, negative1, neutral1 = polarity1(df1)
    display_graph(positive, negative, neutral)
    display_graph1(positive1, negative1, neutral1)
