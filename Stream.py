import streamlit as st
import joblib
import numpy as np

# Load trained models
models = {
    "Logistic Regression": joblib.load("Exported Models/Logistic_regression.joblib"),
    "K-Nearest Neighbors": joblib.load("Exported Models/KNN.joblib"),
    "Support Vector Machine": joblib.load("Exported Models/svm_model.joblib"),
    "Decision Tree": joblib.load("Exported Models/Decision_Tree.joblib"),
}

# Consistent class names
class_names = ["Setosa", "Versicolor", "Virginica"]

# Mapping in case models return scikit-learn style labels like "Iris-setosa"
label_map = {
    "Iris-setosa": "Setosa",
    "Iris-versicolor": "Versicolor",
    "Iris-virginica": "Virginica",
}

st.set_page_config(page_title="🌸 Iris Flower Classifier", layout="centered")
st.title("🌸 Iris Flower Classifier")
st.write(
    "Predict the type of Iris flower based on its features using different machine learning models."
)

# Sidebar inputs
st.sidebar.header("🌱 Flower Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.0, 0.1)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 4.0, 0.1)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 1.0, 0.1)

# Model selection
model_name = st.sidebar.selectbox("Choose the model:", list(models.keys()))

if st.sidebar.button("Predict"):
    model = models[model_name]
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)

    raw_pred = prediction[0]

    # Handle numeric or string predictions
    if isinstance(raw_pred, (int, np.integer)):
        predicted_class = class_names[raw_pred]
    else:
        predicted_class = label_map.get(raw_pred, raw_pred)

    # Probabilities if available
    probability = (
        model.predict_proba(features) if hasattr(model, "predict_proba") else None
    )

    # Show result
    st.success(
        f"🌱 The predicted class is **{predicted_class}** using **{model_name}**!"
    )

    if probability is not None:
        st.subheader("🔍 Confidence Scores:")
        for idx, score in enumerate(probability[0]):
            st.write(f"- **{class_names[idx]}**: {score:.2%}")

st.markdown("---")
st.caption("Copyright © 2025 Kenean Dita. All rights reserved.")
