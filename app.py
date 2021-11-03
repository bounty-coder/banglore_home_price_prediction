from pickle import TRUE
from flask import Flask, request, jsonify
from flask.templating import render_template
import predict
import sklearn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_location',methods=['GET'])
def get_location():
    response = jsonify({
        'locations': predict.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': predict.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__=="__main__":
    print("STARTING...")
    predict.load_saved()
    app.run()