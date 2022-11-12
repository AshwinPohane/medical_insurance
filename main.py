# from typing_extensions import Self
# from crypt import methods
from flask import Flask, jsonify, render_template, request
from model.utils import Medical_Insurance
import config

app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_flask():
    print('Welcome to Flask')
    return render_template('index.html')                                                              # 

@app.route('/medical-insurance-prediction', methods=['POST','GET'])
def get_prediction_model():

    if request.method == 'GET':
        print('In GET method')
        print('For git')
        # code for flask
        age= request.args.get('age')
        sex= request.args.get('sex')
        bmi= request.args.get('bmi')
        children= request.args.get('children')
        smoker= request.args.get('smoker')
        region = request.args.get('region')
        
        med_insurance = Medical_Insurance(age,sex,bmi,children,smoker,region)
        pred = med_insurance.get_prediction()
        print()
        print(f'Your Predicted Medical Insurance Price is :{pred}')

        # return render_template('index.html', med_pred = pred )
        return jsonify( {'Result':f'Medical insurance charges will be :${pred} /-'} )
    
    else:
        
        print('In POST method')

        # code for flask

        age= request.args.get('age')
        sex= request.args.get('sex')
        bmi= request.args.get('bmi')
        children= request.args.get('children')
        smoker= request.args.get('smoker')
        region = request.args.get('region')
        
        med_insurance = Medical_Insurance(age,sex,bmi,children,smoker,region)
        pred = med_insurance.get_prediction()
        print()
        print(f'Your Predicted Medical Insurance Price is :{pred}')

        return render_template('index.html', med_pred = pred )
        # return jsonify( {'Result':f'Medical insurance charges will be :${pred} /-'} )

if __name__ == '__main__':
    app.run(host='localhost', port= config.port_number, debug=True)