import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings
import pickle
warnings.filterwarnings("ignore")

data=pd.read_csv("KCT ECE.csv")
data.isnull().sum()
data.drop(['Application ID'],axis=1, inplace = True)
X = data.drop(['Result'], axis= 1)
Y = data["Result"]

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=2)

regr = RandomForestRegressor(n_estimators = 100, random_state = 0)
regr.fit(x_train, y_train)
y_pred_R=regr.predict(x_test)
y_pred_r=regr.predict(x_train)
x = np.array([[1043,195,2022,197,179]])
y = regr.predict(x)
# print(x,y)

filename = 'kct_ece_model.pkl'
pickle.dump(regr,open(filename,'wb'))
loaded_model = pickle.load(open(filename,'rb'))
