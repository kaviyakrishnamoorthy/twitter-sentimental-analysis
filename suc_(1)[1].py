from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
import json
import fileinput
import string






ckey = '2DQICe4Oa7nDGyLwByWmA3vJW'
csecret = 'C7cBHlSGvTYF9ZrM6zhLu35pmWpCjfAZIhKGfGVoOqaScmDZv9'
atoken = '906191155762610176-kJhw8vLmAOj4g8X6tNbfzQ2bWo8y4LA'
asecret = 'AFGR93XjEQv7rkKWCQuvnFOnJJIT5lz7cIkL1ylbuB4tu'




class listener(StreamListener):
    
     def on_data(self, data):
        try:
            tweet = data.split(',"text":"')[1].split(',"source')[0]
            #split the left and right side so that it displays only the right half of the texts.
            #It removes all those id's and text
            
            tweet=tweet.lower()
            #it converts http and www to URL
            tweet=re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
            tweet=re.sub(r'http\S+','',tweet)
            #converts @user to AT_USER
            tweet = re.sub('@[^\s]+','AT_USER',tweet)
            #removes additional white spaces.
            tweet = re.sub('[\s]+', ' ', tweet)
            #it replaces #any_word with any_word
            tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
            tweet = re.sub(r'[^\w\s]','',tweet)
            #it removes numbers
            tweet=re.sub(r'[0-9]+','',tweet)
            #it trims the tweet i.e any spaces after or before.
            tweet = tweet.strip('\'"')
            unicodeString=tweet
            print(unicodeString.encode("ascii", "ignore"))
            #print tweet
            
            saveFile=open('temp.csv','a')
            saveFile.write(tweet)
            saveFile.write('\n')
            saveFile.close()
            return True
          
            
            
          

            
                  
        except BaseException,e:
            print 'failed ondata,',str(e)
            time.sleep(5)


        def on_error(self,status):
            print status



        

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(languages=["en"],track=["obama"])



    
