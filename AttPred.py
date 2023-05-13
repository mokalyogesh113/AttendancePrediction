import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics 

class attPred():
    def __init__(self) :
        pass
    
    def train_data(self,file_path):
        self.data = pd.read_csv(file_path)
        # self.data["Display Name"]  = self.data["Display Name"].str.lower()
        # for i  in range(self.data.shape[0]):
        #     self.data.iloc[i]['Display Name'] = self.data.iloc[i]['Display Name'].lower()

        X = self.data[['TeSem1mon1', 'TeSem1mon2','TeSem2mon1','TeSem2mon2']]
        y = self.data['TeTermend_sem 1']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        self.mse = metrics.mean_squared_error(y_test, y_pred)
        self.r2 = metrics.r2_score(y_test, y_pred)

        X_sem2 = self.data[['TeSem1mon1', 'TeSem1mon2','TeSem2mon1','TeSem2mon2']]
        sem2_y_pred= self.model.predict(X_sem2)

        self.df_pred = pd.DataFrame({'Name': self.data.iloc[X.index]['Display Name'].str.lower(), 'sem2_pred': sem2_y_pred})


    def predict(self,name):
        name_lower = name.lower()

        # print(name_lower , " ", self.df_pred['Name'][2] , name_lower in self.df_pred['Name'])

        for i in range(len(self.df_pred)):
            if name_lower== self.df_pred['Name'][i]:
                row = [name, self.df_pred['sem2_pred'][i]]
                return row
        
        return None
    