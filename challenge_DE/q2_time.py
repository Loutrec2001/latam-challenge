import pandas as pd
import emoji
import regex as re


def q2_time(file_path: str):

    dataframe = pd.read_json(file_path, lines=True)

    emoji_counts = {}
    grouped_praying_hands_emojis = {'🙏', '🙏🏻', '🙏🏼', '🙏🏽', '🙏🏾', '🙏🏿'}

    for tweet in dataframe['content']:
        emojis = re.findall(r'\X', tweet)
        for emoji_char in emojis:
            if emoji_char in grouped_praying_hands_emojis:
                emoji_base = '🙏'  
            elif emoji_char in emoji.UNICODE_EMOJI['en']:
                emoji_base = emoji_char
            else:
                continue
            emoji_counts[emoji_base] = emoji_counts.get(emoji_base, 0) + 1

    emoji_df = pd.DataFrame(emoji_counts.items(), columns=['Emoji', 'Count'])
    top_10_emojis = emoji_df.nlargest(10, 'Count')

   
    return top_10_emojis
