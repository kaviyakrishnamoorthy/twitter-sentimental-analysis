
import pandas as pd
import numpy as np
import time
import re
import json
import fileinput
import string




tips=pd.read_csv('C:\\Users\\user\\Downloads\\dataset.csv','rb',error_bad_lines=False)
class listener(tips):
    
     def on_data(self, tips):
        try:
            tt = data.split(',"text":"')[1].split(',"source')[0]
            #from autocorrect import spell
            #spell(tweet)

            

            #def preprocess(tweet):
            tt=tt.lowertweet=re.sub(r'http\S+','',tt)
            
            tt = re.sub('[\s]+', ' ', ttt)
            
            
            tt = re.sub(r'[^\w\s]','',tweet)
            tt=re.sub(r'[0-9]+','',tt)
            tt = tt.strip('\'"')
            
            
          
          
            
            
          

            
                  
        except BaseException,e:
            print 'failed ondata,',str(e)
            time.sleep(5)


       



    
