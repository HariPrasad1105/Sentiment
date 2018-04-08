import pandas as pd
import csv

df = pd.read_json("static\Cell_Phones_and_Accessories_5.json", lines=True)
Sentiment, Tweet, string = list(df["overall"]), list(df["reviewText"]), ""
count = 0


with open("static\newstanford.csv", "w", newline='') as f:
	writer = csv.writer(f, delimiter=',')
	pos_count, neu_count, neg_count = 0, 0, 0
	for i, j in zip(Sentiment, Tweet):
		# if i >= 4:
		# 	pos_count += 1
		# 	if pos_count <= 3000:
		# 		string = "\t" + j
		# 		writer.writerow([4, string])
		if i >= 2 and i < 4:
			neu_count += 1
			if neu_count <= 2500:
				string = "\t" + j
				writer.writerow([2, string])
		if i < 2:
			neg_count += 1
			if neg_count <= 1500:
				string = "\t" + j
				writer.writerow([0, string])
