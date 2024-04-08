import joblib
import os

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
