import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics
import seaborn as sns
from sklearn import tree
import warnings
import matplotlib.pyplot as plt
import pickle
import requests
from bs4 import BeautifulSoup
# import request, json
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# apikey="98a710b9366f51a9193e73a9b2fdb60f"
# baseurl=""

city = "Velachery"
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
temp = temp[:1]



d = pd.read_csv('Data/crop_recommendation.csv')

features = d[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = d['label']
labels = d['label']

acc = []
model = []


Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)


RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
# print("RF's Accuracy is: ", x)

# print(classification_report(Ytest,predicted_values))
score = cross_val_score(RF,features,target,cv=5)


RF_pkl_filename = 'model/RandomForest.pkl'
RF_Model_pkl = open(RF_pkl_filename, 'wb')
pickle.dump(RF, RF_Model_pkl)
RF_Model_pkl.close()

data = np.array([[30,5, 80, int(temp), 60.3, 3.7, 140.91]])  
prediction = RF.predict(data)
print(prediction)