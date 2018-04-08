import csv
import pandas as pd
from JsonLoading import Preprocess


df = pd.read_json("static\Cell_Phones_and_Accessories_5.json", lines=True)
Sentiment, Tweet, string = list(df["overall"]), list(df["reviewText"]), ""
count = 0


# with open("stanfordcsv.txt", "a") as f:
# 	for i, j in zip(Sentiment, Tweet):
# 		if i >= 4:
# 			count += 1
# 			if count <= 15:
# 				f.write(4)
# 				f.write(Preprocess(j))


with open("static\stanfordcsv.csv", "a") as f:
    writer = csv.writer(f)
    for i, j in zip(Sentiment, Tweet):
        count += 1
        if count <= 10:
            preprocessed_stanford = Preprocess(str(Tweet))
            writer.writerow((str(i)), '\t', preprocessed_stanford)
            writer.writerow("\n")
