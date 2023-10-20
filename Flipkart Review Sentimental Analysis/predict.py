import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def model_prediction(features):
    sid = SentimentIntensityAnalyzer()
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Flipkart Review Sentimental Analysis/model/FlipkartReview.pkl', 'rb'))
    Review = sid.polarity_scores(features)
    if Review['compound']>0:
        return "Review is Positive"
    elif Review['compound']<0:
        return "Review is Negative"
    else:
        return "review is Neutral"


review = input("Enter your Review: -")
print(model_prediction(review))