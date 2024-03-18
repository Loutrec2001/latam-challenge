import pandas as pd

def q1_time(file_path: str):
    
    dataframe = pd.read_json(file_path, lines=True)
    dataframe['date'] = pd.to_datetime(dataframe['date']).dt.date
    
    dataframe['username'] = [user.get('username', None) for user in dataframe['user']]
    
    dataframe = dataframe[['date', 'username']]
    
    grouped_data = dataframe.groupby(['date', 'username']).size().reset_index(name='tweet_count')
    
    top_10_dates = grouped_data.groupby('date')['tweet_count'].sum().nlargest(10)
    
    formatted_result = []
    
    for date in top_10_dates.index:
        date_data = grouped_data[grouped_data['date'] == date]
        top_user = date_data.loc[date_data['tweet_count'].idxmax()]
        formatted_result.append((date, top_user['username']))
    
   
    return formatted_result

