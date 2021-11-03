import pickle
import json
import numpy
import sklearn

__location = None
__data_column = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_column.index(location.lower())
    except:
        loc_index = -1

    X = numpy.zeros(len(__data_column))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >=0:
        X[loc_index] = 1

    return round(__model.predict([X])[0],2)

def get_location():
    return __location

def load_saved():
    print("Load Saved")
    global __data_column
    global __location
    global __model

    with open ("./model/columns.json",'r') as f:
        __data_column=json.load(f)['data_columns']
        __location = __data_column[3:]

    with open("./model/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)


if __name__=='__main__':
    load_saved()
    print(get_location())
    print(get_estimated_price("whitefield",1000,3,3))
    print(get_estimated_price("hsr layout",2000,5,4))
    print(sklearn.__version__)