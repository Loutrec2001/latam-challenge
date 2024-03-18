from collections import Counter
import pandas as pd
import regex as re

def q3_time(file_path: str):
    
    dataframe = pd.read_json(file_path, lines=True)
    tweets = dataframe['content']
    
    mention_counts = Counter()
    for tweet in tweets:
        mentions = re.findall(r'@(\w+)', tweet)
        mention_counts.update(mentions)
    
    top_10_mencionados = mention_counts.most_common(10)
   
    return top_10_mencionados

