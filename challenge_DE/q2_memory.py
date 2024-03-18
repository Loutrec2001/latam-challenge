import pandas as pd
import emoji
import regex as re
from memory_profiler import profile

@profile
def q2_memory(file_path: str):
    dataframe = pd.read_json(file_path, lines=True)
    text = dataframe['content']
    emoji_counts = {}

    for tweet in text:
        emojis = re.findall(r'\X', tweet)
        for emoji_char in emojis:
            if emoji_char in emoji.UNICODE_EMOJI['en']:
                if emoji_char in emoji_counts:
                    emoji_counts[emoji_char] += 1
                else:
                    emoji_counts[emoji_char] = 1

    emoji_df = pd.DataFrame(list(emoji_counts.items()), columns=['Emoji', 'Count'])
    top_10_emojis = emoji_df.sort_values(by='Count', ascending=False).head(10)

    formatted_result = [(row['Emoji'], row['Count']) for _, row in top_10_emojis.iterrows()]
    
    return formatted_result

if __name__ == "__main__":
    file_path = '/Users/edwardguzman/Documents/Documentos/latam-challenge/challenge_DE/farmers-protest-tweets-2021-2-4.json'
    result = q2_memory(file_path)
    print(result)
