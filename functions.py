import joblib
import os

from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_regression, f_classif, chi2



def save_model_if_best(new_score, pipeline, model_name):
    # joblib model only, could add a param joblib/pickle options
    files = os.listdir('app/app_model')
    previously_used_models = []

    if files:
        for f in files:
            previously_used_models.append(f.split('_')[1])
            if model_name == f.split('_')[1] and int(f.split('_')[0]) > new_score:
                joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")
                print(new_score)
                # could be moved to a backup dir instead of deleting it
                os.remove(f"app/app_model/{f}")
                return True

            # if we arrive there it means score was too low or the model of this name haven't been saved yet.
            # if a new model algorythm is used we save it.
            if  model_name not in previously_used_models:
                joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")
    # if no model has been saved yet save it.
    else:
        joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")

def load_best_model(model_name=False, path='app/app_model/'):
    # joblib model only, could add a param joblib/pickle options
    files = os.listdir(path)
    score_dict = {}

    if files:
        for f in files:
            if f.split('_')[1] == model_name:
                return joblib.load(f"{path}{int(f.split('_')[0])}_{f.split('_')[1]}_model.pkl")
            else :
                score_dict[f.split('_')[1]] = int(f.split('_')[0])

        return joblib.load(f"{path}{score_dict[min(score_dict, key=score_dict.get)]}_{min(score_dict, key=score_dict.get)}_model.pkl")


# price_column is a str name of the numeric column
def iqr_range_price_filter(df, price_column):
    q3 = df.price.describe()['75%']
    q1 = df.price.describe()['25%']
    iqr_range = q3-q1
    new_df = df[(df[price_column] > q1-iqr_range*1.5) & (df[price_column] < q3+(iqr_range*1.5))]
    print("old number of rows", df.shape[0])
    print("new number of rows", new_df.shape[0])
    return new_df



def variance_threshold_selector(data, threshold=0.2):
    selector = VarianceThreshold(threshold)
    selector.fit(data)
    new_df = data[data.columns[selector.get_support(indices=True)]]
    dropped_features = [feature for feature in data.columns if feature not in new_df.columns]
    if dropped_features:
        print('columns dropped :', dropped_features)
    else :
        print('no features dropped')
    return new_df

# k is number of feature to keep
def KBest_selector(data, target_name, k=1, score_function = 'f_regression'):
    # Create and fit selector
    if score_function == 'f_regression':
        selector = SelectKBest(f_regression, k=k)
    elif score_function == 'f_classif':
        selector = SelectKBest(f_classif, k=k)
    else :        
        selector = SelectKBest(chi2, k=k)
        print('using chi2')
        
    selector.fit(data.drop(columns=[target_name]), data[target_name])
    # Get columns to keep and create new dataframe with those only
    cols_idxs = selector.get_support(indices=True)
    new_df = data.iloc[:,cols_idxs]
    
    # display the names of dropped columns
    dropped_features = [feature for feature in data.columns if feature not in new_df.columns].remove(target_name)
    if dropped_features:
        print('columns dropped :', dropped_features)
    else :
        print('no features dropped')
        
    new_df.loc[:,target_name] = data.loc[:, target_name]
    return new_df
