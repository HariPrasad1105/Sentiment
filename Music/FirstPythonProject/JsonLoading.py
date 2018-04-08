import nltk
from nltk.corpus import stopwords
import string
import re

t = re.compile(r'https?://')
string = string.punctuation.replace("@", "").replace("#", "")
stop = set(stopwords.words("english")).union(set(string))
slang_compile = re.compile(r"[\w<]+\b")
slang_word_compile = re.compile(r'\"([\w,\s\'-]+)\"')
retweet_compile = re.compile(r'^RT\s@[\w_]+\s')
emoticon__compile = re.compile("(positive|extremely-positive|negative|extremely-negative|neutral)")

slang, slang_meaning, slang_dict = [], [], {}

with open("E:\Hackathon\HackathonProject\Music\FirstPythonProject\static\slandwords.txt", "r") as f:
    for line in f:
        slang_match = slang_compile.search(line.lower()).group(0)
        slang_word_match = slang_word_compile.findall(line)
        slang.append(slang_match)
        slang_meaning += slang_word_match

emoticon_dict = {}
with open("E:\Hackathon\HackathonProject\Music\FirstPythonProject\static\qwerty.txt", "r") as f:
    for line in f:
        emoticon_match = emoticon__compile.search(line).group(0)
        for i in line.split("  "):
            emoticon_dict[i] = emoticon_match

# print(emoticon_dict)
for i, j in zip(slang, slang_meaning):
    slang_dict[i] = j

slang_list = slang_dict.keys()

emoticon_list = emoticon_dict.keys()


# print(emoticon_list)


def remove_excess_letter(list):
    result = []
    for st in list:
        res, count = '', 1
        for i, j in enumerate(st):
            if i + 1 < len(st):
                if st[i] == st[i + 1]:
                    count += 1
                    if count < 3:
                        res += st[i]
                else:
                    count = 1
                    res += st[i]
            else:
                res += st[i]
        result.append(res)

    return result


def retweets(string):
    if not string.startswith('rt @'):
        return string
    else:
        pass


def remove_slang(to_be_removed_slang_list):
    for i, j in enumerate(to_be_removed_slang_list):
        if j in slang_list:
            to_be_removed_slang_list[i] = slang_dict.get(j)

    return to_be_removed_slang_list


def remove_emoticons(list_contains_emoticons):
    for i, j in enumerate(list_contains_emoticons):
        if j in emoticon_list:
            list_contains_emoticons[i] = emoticon_dict.get(j)

    return list_contains_emoticons


def Preprocess(twt):
    #with open(filename, "r") as f:
        #with open("preprocessed.csv", "a") as output:
         #       csv_writer = csv.writer(output)
                try:
                    stripping_tweet = twt.strip()
                except AttributeError:
                    pass
                remove_retweet = retweets(stripping_tweet.lower())
                replace_url = re.sub("https?:[\w/_.-]+", "", str(remove_retweet))
                replace_username = re.sub("@[\w_]+", "", replace_url)
                replace_date = re.sub("[\d]+/[\d]+/[\d]+", "", replace_username)
                replace_hashtag = re.sub("#[\w_]+", "", replace_date)
                replace_additional_spaces = re.sub("[\s]+", " ", replace_hashtag)
                replace_numbers = re.sub(r"\b[0-9]+\b", "", replace_additional_spaces)
                list = [words for words in nltk.word_tokenize(replace_numbers) if words not in stop]
                replace_excess_words = remove_excess_letter(list)
                replace_slang_words = remove_slang(replace_excess_words)
                replace_emoticons = remove_emoticons(replace_slang_words)
                result = " ".join(replace_emoticons)
                return result
        #print("Completed preprocessing the data")



 #    for line in f:
        #        tweet_data = json.loads(line)
        #       data = tweet_data["text"]
