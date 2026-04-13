import numpy as np
import os
import joblib  

def model_prediction_HHV(Ndata):
    names = list(Ndata.keys())
    features = np.array(list(Ndata.values()), dtype=float)

    predictions_list = []
    MODEL_PATHS = ["models/HHV"]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl') and "TabPFN" in model_file:
                file_path = os.path.join(model_path, model_file)
                print(f"Loading HHV model: {file_path}")
                model = joblib.load(file_path)
                preds = model.predict(features)
                predictions_list.append(preds)

    print(f"Number of HHV models used: {len(predictions_list)}")
    avg_predictions = np.mean(predictions_list, axis=0)

    results = {names[i]: avg_predictions[i] for i in range(len(names))}
    return results


def model_prediction_Yield(Ndata):
    names = list(Ndata.keys())
    features = np.array(list(Ndata.values()), dtype=float)

    predictions_list = []
    MODEL_PATHS = ["models/Yield"]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl') and "TabPFN" in model_file:
                file_path = os.path.join(model_path, model_file)
                print(f"Loading Yield model: {file_path}")
                model = joblib.load(file_path)
                preds = model.predict(features)
                predictions_list.append(preds)

    print(f"Number of Yield models used: {len(predictions_list)}")
    avg_predictions = np.mean(predictions_list, axis=0)

    results = {names[i]: avg_predictions[i] for i in range(len(names))}
    return results


def model_prediction_CER(Ndata):
    names = list(Ndata.keys())
    features = np.array(list(Ndata.values()), dtype=float)

    predictions_list = []
    MODEL_PATHS = ["models/CER"]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl') and "TabPFN" in model_file:
                file_path = os.path.join(model_path, model_file)
                print(f"Loading CER model: {file_path}")
                model = joblib.load(file_path)
                preds = model.predict(features)
                predictions_list.append(preds)

    print(f"Number of CER models used: {len(predictions_list)}")
    avg_predictions = np.mean(predictions_list, axis=0)

    results = {names[i]: avg_predictions[i] for i in range(len(names))}
    return results


def get_prediction(data, target_type="HHV"):
    Ndata = {k: v for k, v in data.items()}  # no drop last element if needed

    if target_type == "HHV":
        return model_prediction_HHV(Ndata)
    elif target_type == "Yield":
        return model_prediction_Yield(Ndata)
    elif target_type == "CER":
        return model_prediction_CER(Ndata)
    else:
        raise ValueError("Invalid target_type. Choose from 'HHV', 'Yield', 'CER'.")