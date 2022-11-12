import pandas as pd
import numpy as np
import json
import pickle
import config                                                                        #### comment to run only utils file,  uncomment for postman / html

class Medical_Insurance():
    def __init__(self,age,sex,bmi,children, smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker

        self.region = 'region_' + region

    def load_model(self):

        # with open ('model\json_label_med_dataset.json', 'r') as f:                     # without config.py
        with open (config.json_file_path, 'r') as f:                                 #### comment to run only utils file,  uncomment for postman / html
            self.json_data = json.load(f)

        # with open ('model\pickle_med_dataset.pkl', 'rb') as f:                         # without config.py
        with open (config.model_file_path, 'rb') as f:                               #### comment to run only utils file,  uncomment for postman / html
            self.model = pickle.load(f)
        
    def get_prediction(self):

        self.load_model()                                                          # calling model

        self.region_index = self.json_data['col_names'].index(self.region)         # get index of column of region which user has requested

        array = np.zeros(len(self.json_data['col_names']))            # Empty array

        array[0] = self.age
        array[1] = self.json_data['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data['smoker'][self.smoker]

        array[self.region_index] = 1

        med_pred = self.model.predict([array])[0]

        # print('Test array -->', array)
        # print('Predicted Medical Insurance Charges: ', med_pred)

        return np.around(med_pred, 2)

if __name__ == '__main__':

    age = 11
    sex = 'male'
    bmi = 32.6
    children = 2
    smoker = 'no'
    region = 'southwest'

    med_insurance = Medical_Insurance(age,sex,bmi,children,smoker,region)
    pred = med_insurance.get_prediction()
    print()
    print(f'Your Predicted Medical Insurance Charges are : ${pred} /-')