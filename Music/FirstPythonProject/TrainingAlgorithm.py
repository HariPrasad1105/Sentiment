import pandas as pd
import svm as svm
from sklearn import cross_validation
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer


# import numpy as np
# from sklearn.feature_extraction import SelectPercentile, f_classif
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt


class Algorithm:

    def __init__(self, string):
        self.string1 = string
        df = pd.read_csv("E:\Hackathon\HackathonProject\Music\FirstPythonProject\static\TrainDataSet.csv", sep="\t")
        senti, twt = list(df["Sentiment"]), list(df["Tweet"])

        path = "E:\Hackathon\HackathonProject\Music\FirstPythonProject\static\\" + self.string1

        df1 = pd.read_csv(path, header=None, names=["sentiment"])
        tweets, self.stringTweets = list(df1["sentiment"]), str(df1["sentiment"])
        tf = TfidfVectorizer(min_df=0, max_df=1.0, stop_words='english', ngram_range=(1, 1))

        features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(twt, senti,
                                                                                                     train_size=0.90,
                                                                                                     random_state=42)
        features_train_transform = tf.fit_transform(features_train, labels_train)
        features_test_transform = tf.transform(tweets)

        # selector = SelectPercentile(f_classif, percentile=50)
        # selector.fit(features_train_transform, labels_train)
        # selector.transform(features_test_transform)
        # features_train_transform = selector.transform(features_train_transform).toarray()
        # features_test_transform = selector.transform(features_test_transform).toarray()
        #
        # mnb = MultinomialNB()
        # mnb.fit(features_train_transform, labels_train)
        # prediction = mnb.predict(features_test_transform)
        # print("Accuracy Using sklearn metrics : {}".format(accuracy_score(prediction, labels_test)))

        svm_ = svm.SVC(gamma=1, C=100)
        svm_.fit(features_train_transform, labels_train)
        predictionsvm = svm_.predict(features_test_transform)

        # print(prediction)2
        print(predictionsvm)
        # print("Accuracy Using sklearn metrics for SVM : {}".format(accuracy_score(predictionsvm, labels_test)))
        resultList = list(predictionsvm)
        self.pos, self.neg, self.neu, self.worcloud = resultList.count('4'), resultList.count('0'), resultList.count('2'), str(df1["sentiment"])

    def result(self):
        print(self.pos, self.neg, self.neu, self.stringTweets)
        return self.pos, self.neg, self.neu, self.stringTweets

        #
        # print("Positive : {}".format(pos))
        # print("Neutral : {}".format(neu))
        # print("Negative : {}".format(neg))

        # pos_pos, neg_neg, neg_pos, pos_neg, neu_neu, neu_neg, neu_pos, pos_neu, neg_neu = 0, 0, 0, 0, 0, 0, 0, 0, 0

        # prediction_list = list(prediction)

        # for i, j in zip(prediction_list, labels_test):
        # 	if i == '0' and j == '0':
        # 		neg_neg += 1
        # 	if i == '4' and j == '4':
        # 		pos_pos += 1
        # 	if i == '4' and j == '0':
        # 		neg_pos += 1
        # 	if i == '0' and j == '4':
        # 		pos_neg += 1
        # 	if i == '2' and j == '2':
        # 		neu_neu += 1

        # print("neg_neg : {}, pos_pos : {}, neg_pos : {}, pos_neg : {}, neu_neu : {}".format(neg_neg, pos_pos, neg_pos, pos_neg, neu_neu))
        # actual = np.array(labels_test)
        # prediction_listsvm = list(predictionsvm)

        # for i, j in zip(prediction_listsvm, labels_test):
        # 	if i == '0' and j == '0':
        # 		neg_neg += 1
        # 	if i == '4' and j == '4':
        # 		pos_pos += 1
        # 	if i == '4' and j == '0':
        # 		neg_pos += 1
        # 	if i == '0' and j == '4':
        # 		pos_neg += 1
        # 	if i == '2' and j == '2':
        # 		neu_neu += 1
        # 	if i == '2' and j == '0':
        # 		neg_neu += 1
        # 	if i == '4' and j == '2':
        # 		neu_pos += 1
        # 	if i == '0' and j == '2':
        # 		neu_neg += 1
        # 	if i == '2' and j == '4':
        # 		pos_neu += 1

        # print("neg_neg : {}, pos_pos : {}, neg_pos : {}, pos_neg : {}, neu_neu : {}, neu_pos : {}, neu_neg : {},
        # pos_neu : {}".format(neg_neg, pos_pos, neg_pos, pos_neg, neu_neu, neu_pos, neu_neg, pos_neu))

        # labels = ['Positive', "Negative", 'Neutral']
        # sizes = [pos, neg, neu]
        # colors = ['lightskyblue', 'lightcoral', 'lightgreen']
        #
        # plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=250)
        # plt.title("Tweets Sentiment", fontname='Times New Roman', fontweight='bold', fontsize=30)
        # plt.axis('equal')
        # plt.legend()
        # plt.show()

        # print(len(labels_test))
        # count = 0

        # for i in range(len(prediction)):
        # 	if prediction[i] == actual[i]:
        # 		count += 1
        # print(count)

        # print("accuracy : {} ".format(count/len(labels_test)))
