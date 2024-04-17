import sys
import pandas as pd
import joblib

def model_prediction(sqft_living, sqft_living15, grade, zipcode_class):
    print('model_prediction_1')
    model = joblib.load('app_model/96308_knn_model.pkl')
    print('model_prediction_2')
    # with open('app/app_model/best_rf_model.pkl', 'rb') as f:
    #     model = pickle.load(f)

    X_test = pd.DataFrame({'sqft_living'     : [sqft_living],
                       'sqft_living15'       : [sqft_living15],
                       'grade'               : [grade],
                       'zipcode_class'       : [zipcode_class],
                       })

    return [model.predict(X_test)] # , model.predict_proba(X_test)

def error_message():
    print("""Il faut entrer en ligne de commande in the King County area, Washington State :
        python script.py age(float range[1-120]) hypertension(int 1=True) avg_glucose_level(float range [50 300]) heart_disease(int 1=True) smoking_status(str smokes - formerly smoked - never smoked)""")
    return

def main():
    print("in the main")

    if len(sys.argv) == 5:
        sqft_living = float(sys.argv[1])
        sqft_living15 = int(sys.argv[2])
        grade = int(sys.argv[3])
        zipcode_class = int(sys.argv[4])



    else :
        error_message()
        return

    prediction = model_prediction(sqft_living, sqft_living15, grade, zipcode_class)

    if prediction:
        return print(f"Your house is estimated to be worth {prediction[0][0]}")
    else:
        return print("Invalid prediction")

if __name__ == "__main__":
    main()
