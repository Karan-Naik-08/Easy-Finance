import pickle
import numpy as np

# Load the trained model from the .pkl file
with open('Car_trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

def give_pred1(inpt):
    predictin=int(loaded_model.predict(inpt))
    predictin=predictin*83
    return predictin

