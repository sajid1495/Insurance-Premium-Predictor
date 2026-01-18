import pickle
import pandas as pd
from schema.user_input import UserInput


#import them ml model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f) 

MODEL_VERSION = "1.0.0"


#class lebels from model
class_lebels = model.classes_.tolist()


def predict_output(user_input: dict):
    df = pd.DataFrame(user_input) 

    #predict class
    predicted_class = model.predict(df)[0]

    #get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    #create mapping of class lebels to probabilities
    class_probs = dict(zip(class_lebels, map(lambda p: round(p, 4), probabilities)))


    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }