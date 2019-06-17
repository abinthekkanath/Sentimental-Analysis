import tweepy 
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk 

consumer_key = 'cClpYpPkmZxj5Uxrz4qmvD6EB'                                                                                                                                     

consumer_secret = 'DrILtiKK7sWG8Cm3iLWX2982VdGCdu33qo932FEQaqNvWPfKip'                                                                                                         

access_token = '992046254661058560-TsdvodXULMY8IlTNnAZKlFVd1p213zF'                                                                                                            

access_token_secret = 'RQXZxbGZDPBMg6CjfSxVOPkudAvf5RwyfcUhpEoDrjMYm'                                                                                                          

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)                                                                                                                     

auth.set_access_token(access_token, access_token_secret)                                                                                                                      

api = tweepy.API(auth)                                                                                                                                                        

tweets = api.search('Artificial Intelligence', count=200)

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets']) 

nltk.download('vader_lexicon') 

sid = SentimentIntensityAnalyzer() 
   
   
listy = [] 

for index, row in data.iterrows(): 
	ss = sid.polarity_scores(row["Tweets"]) 
	listy.append(ss) 
 
se = pd.Series(listy) 
data['polarity'] = se.values 

print(data.head(100)) 

