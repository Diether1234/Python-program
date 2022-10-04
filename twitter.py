from tkinter.tix import Tree
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("twitter_sentiment_data.csv")
df["formatted"] = (
    df["mssage"]
    .str.replace(r"^https?:\/\/.*", " ", regex=True)
    .replace(r"@[A-Za-z0-9_]+", " ", regex=True)
    .replace(r"#[A-Za-z0-9_]+", " ", regex=True)
)
X_train, X_test, y_train, y_test = train_test_split(
    df ["formatted"], df["sentiment"], test_size=0.20,random_state=1
)
    



count_vector = CountVectorizer()
training_data = count_vector.fit_transform(X_train)
testing_data = count_vector.transform(X_test)
model = LogisticRegression(random_state = 0, max_iter=10000)
predictions = model.fit(training_data)

print("Accuracy score: {}".format(accuracy_score(y_test, predictions)))

con_inp = input("Enter a message : ")
inp = np.array(con_inp)
inp = np.reshape(inp, (1, -1))
inp_conv = count_vector.transform(inp.ravel())
result = model.predict(inp_conv)

for element in result:
    if result[0] == 0:
        print("Neutral")
    elif result[0] == -1:
        print("Negative")
    elif result[0] == 1:
        print("Positive")
    else:
        print("News")
        