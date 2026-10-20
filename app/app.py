
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Mercari Price Predictor",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Mercari Price Predictor")
st.write("Estimate the selling price of a second-hand product.")

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "mercari_price_model_v1.joblib"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()

with st.form("product_form"):
    name = st.text_input("Product name")
    category = st.text_input(
        "Product category",
        placeholder="e.g. Women/Tops"
    )
    brand = st.text_input("Brand", placeholder="Enter Missing if unknown")
    condition = st.selectbox("Item condition", [1, 2, 3, 4, 5])
    shipping = st.selectbox(
        "Shipping paid by",
        ["Seller", "Buyer"]
    )
    description = st.text_area("Product description")

    submitted = st.form_submit_button("Predict Price")

if submitted:
    if not name.strip() or not category.strip() or not description.strip():
        st.warning("Please enter the product name, category, and description.")
    else:
        input_data = pd.DataFrame([{
            "category_name": category.strip(),
            "brand_name": brand.strip() or "Missing",
            "item_condition_id": condition,
            "shipping": 1 if shipping == "Seller" else 0,
            "name_length": len(name),
            "description_length": len(description),
            "category_depth": category.count("/") + 1
        }])

        try:
            prediction = float(model.predict(input_data)[0])
            st.success(f"Estimated selling price: ${max(0, prediction):.2f}")
            st.caption("This is an estimate, not a guaranteed selling price.")
        except Exception as error:
            st.error(f"Prediction failed: {error}")
