
from pathlib import Path

import joblib
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "mercari_price_model_v1.joblib"


def prepare_features(data):
    """Create the structured features expected by the saved model."""
    data = data.copy()

    required_columns = [
        "name",
        "category_name",
        "brand_name",
        "item_condition_id",
        "shipping",
        "item_description",
    ]

    missing = [col for col in required_columns if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    data["name"] = data["name"].fillna("").astype(str)
    data["item_description"] = (
        data["item_description"].fillna("").astype(str)
    )
    data["category_name"] = data["category_name"].fillna("Missing").astype(str)
    data["brand_name"] = data["brand_name"].fillna("Missing").astype(str)

    data["name_length"] = data["name"].str.len()
    data["description_length"] = data["item_description"].str.len()
    data["category_depth"] = data["category_name"].str.count("/") + 1

    return data[
        [
            "category_name",
            "brand_name",
            "item_condition_id",
            "shipping",
            "name_length",
            "description_length",
            "category_depth",
        ]
    ]


def predict_csv(input_csv, output_csv):
    model = joblib.load(MODEL_PATH)
    listings = pd.read_csv(input_csv)

    features = prepare_features(listings)
    listings["predicted_price"] = model.predict(features).clip(min=0)

    listings.to_csv(output_csv, index=False)
    print(f"Predictions saved to: {output_csv}")


if __name__ == "__main__":
    input_file = PROJECT_DIR / "new_listings.csv"
    output_file = PROJECT_DIR / "predictions.csv"

    predict_csv(input_file, output_file)
