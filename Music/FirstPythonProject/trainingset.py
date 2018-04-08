import csv
import re
import nltk
from nltk.corpus import stopwords
import string

t = re.compile(r'https?://')
string = string.punctuation.replace("@", "").replace("#", "")
stop = set(stopwords.words("english")).union(set(string))
stop.remove("not")
stop.remove("no")
slang_compile = re.compile(r"[\w<]+\b")
slang_word_compile = re.compile(r'\"([\w,\s\'-]+)\"')
retweet_compile = re.compile(r'^RT\s@[\w_]+\s')
emoticon__compile = re.compile("(positive|extremely-positive|negative|extremely-negative|neutral)")


slang, slang_meaning, slang_dict = [], [], {}

with open("static\slandwords.txt", "r") as f:
    for line in f:
        slang_match = slang_compile.search(line.lower()).group(0)
        slang_word_match = slang_word_compile.findall(line)
        slang.append(slang_match)
        slang_meaning += slang_word_match

# print(slang_meaning)

emoticon_dict = {}
with open("static\qwerty.txt", "r") as f:
    for line in f:
        emoticon_match = emoticon__compile.search(line).group(0)
        for i in line.split("  "):
            emoticon_dict[i] = emoticon_match

# print(emoticon_dict)
for i, j in zip(slang, slang_meaning):
    slang_dict[i] = j

slang_list = slang_dict.keys()

emoticon_list = emoticon_dict.keys()
# print(len(emoticon_list))

expand1 = re.compile(r"\s\s\"[\w\s]*\"")
expand2 = re.compile(r"\"[\w\s']*\"\s\s")
expandnew = re.compile(r"\"[a-z]+\"\s\s")

expand = {}
with open("static\processedexpand.txt", "r") as f:
    with open("static\processedexpand1.txt", "r") as f1:
        for line, line1 in zip(f, f1):
            match = expand1.search(line.lower()).group(0)
            match1 = expand2.search(line.lower()).group(0)
            matchnew = expandnew.search(line1.lower()).group(0)
            expand[match1.strip().replace("\"", "")] = match.strip().replace("\"", "")
            expand[matchnew.strip()] = match.strip()


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


def remove_contradictions(txt):
    templist = txt.split()
    for i, j in enumerate(templist):
        if j in expand.keys():
            templist[i] = expand.get(j)
    return " ".join(templist)


def remove_slang(to_be_removed_slang_list):
    for i, j in enumerate(to_be_removed_slang_list):
        if j in slang_list:
            to_be_removed_slang_list[i] = slang_dict.get(j)

    return " ".join(to_be_removed_slang_list)


def remove_emoticons(list_contains_emoticons):
    txt = list_contains_emoticons.split()
    for i, j in enumerate(txt):
        if j in emoticon_list:
            txt[i] = emoticon_dict.get(j)

    return " ".join(txt)


def removeHi(txt):
    if txt.startswith("hi") == False:
        return txt
    else:
        return "None"


def preprocess(txt):
    stripping_tweet = txt.strip()
    remove_retweet = retweets(stripping_tweet.lower())
    # remove_hi = removeHi(remove_retweet)
    replace_url = re.sub("https?:[\w/_.-]+", "", str(remove_retweet))
    replace_username = re.sub("@[\w_]+", "", replace_url)
    replace_date = re.sub("[\d]+/[\d]+/[\d]+", "", replace_username)
    replace_hashtag = re.sub("#[\w_]+", "", replace_date)
    # replace_additional_spaces = re.sub("[\s]+", " ", replace_hashtag)
    replace_contradictions = remove_contradictions(replace_hashtag)
    replace_numbers = re.sub(r"\b[0-9]+\b", "", replace_contradictions)
    replace_emoticons = remove_emoticons(replace_numbers)
    list = [words for words in nltk.word_tokenize(replace_emoticons) if words not in stop]
    replace_start_num = [item for item in list if not item[0].isdigit()]
    replace_excess_words = remove_excess_letter(replace_start_num)
    replace_slang_words = remove_slang(replace_excess_words).replace("'s", "").replace(".", "").replace("-", "").replace("'", "").replace("`", "")
    replace_additional_spaces = re.sub("[\s]+", " ", replace_slang_words)
    return replace_additional_spaces


with open("static\iphone6-negative.csv", "r") as f:
    csv_reader = csv.reader(f)
    with open("static\PreprocessedTrainingData.txt", "w") as output:
        for i in csv_reader:
            twt = i[0]
            writedata = preprocess(twt)
            if writedata != "None":
                output.write(preprocess(twt))
                output.write("\n")


startnumcompile = re.compile(r"\d+")

# with open("PreprocessedTrainingData.txt", "r") as f:
# 	with open("PreprocessedTrainingData1.txt" , "w") as output:




# import pandas as pd
# # from JsonLoading import *

# df = pd.read_csv("NegativeLabeled.csv", header = None, names = ["Sentiment", "Tweet"])
# sentiment, tweet = df["Sentiment"], df["Tweet"]

# # senti = df["Sentiment"]
# # senti.to_csv("PreprocessedTrainingData.csv")
# def preprocess(twt):
# 	return "Hello"


# for twt in zip(tweet):
# 	tweet_after_preprocess = preprocess(twt)
# 	tweet_after_preprocess.to_csv("PreprocessedTrainingData.csv", mode = "a")

# # neutral = df["Sentiment"] == 2
# # df[neutral].to_csv("NeutralLabeled.csv", mode = "a")

# # negative = df["Sentiment"] == 0
# # df[negative].to_csv("NegativeLabeled.csv", mode = "a")

# # positive = df["Sentiment"] == 4
# # df[positive].to_csv("PositiveLabeled.csv", mode = "a")

# # for twt,senti in zip(tweet, sentiment):
# # 	if senti == 0:
# # 		df.to_csv("NegativeLabeled.csv", columns = ["Sentiment", "Tweet"])

# # neutral = df["Sentiment"] == 2
# # for i in neutral:
# # 	if i == True:


# # negative = df["Sentiment"] == 0
# # for i in negative:
# # 	if i == True:
# # 		pass


# # positive = df["Sentiment"] == 4
# # for i in positive:
# # 	if i == True:
# # 		pass
