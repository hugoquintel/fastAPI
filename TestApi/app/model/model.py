from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f"{BASE_DIR}/model.pkl", "rb") as f:
    clf = pickle.load(f)

def predict(precipitation, temp_max, temp_min, wind, month_1, month_2, 
            month_3, month_4, month_5, month_6, month_7, month_8, 
            month_9, month_10, month_11, month_12):
    input = [precipitation, temp_max, temp_min, wind, month_1, month_2, 
            month_3, month_4, month_5, month_6, month_7, month_8, 
            month_9, month_10, month_11, month_12]
    return clf.predict([input])[0]

