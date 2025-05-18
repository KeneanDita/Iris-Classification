import streamlit as st
import joblib
import numpy as np

models = {
    "Logistic Regression": joblib.load("Exported Models/Logistic_regression.joblib"),
    "K-Nearest Neighbors": joblib.load("Exported Models/KNN.joblib"),
    "Support Vector Machine": joblib.load("Exported Models/svm_model.joblib"),
    "Decision Tree": joblib.load("Exported Models/Decision_Tree.joblib")
}

class_names = ["Setosa", "Versicolor", "Virginica"]

st.set_page_config(page_title="🌸 Iris Flower Classifier", layout="centered")
st.title("🌸 Iris Flower Classifier")
st.write("Predict the type of Iris flower based on its features using different machine learning models.")

st.sidebar.header("🌱 Flower Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.0, 0.1)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 4.0, 0.1)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 1.0, 0.1)

model_name = st.sidebar.selectbox("Choose the model:", list(models.keys()))

if st.sidebar.button("Predict"):
    model = models[model_name]
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    predicted_class = class_names[int(prediction[0])]
    probability = model.predict_proba(features) if hasattr(model, "predict_proba") else None

    st.success(f"🌱 The predicted class is **{predicted_class}** using **{model_name}**!")


    if probability is not None:
        st.subheader("🔍 Confidence Scores:")
        for idx, score in enumerate(probability[0]):
            st.write(f"- **{class_names[idx]}**: {score:.2%}")

st.markdown("---")
st.caption("Copyright © 2025 Kenean Dita. All rights reserved.")
