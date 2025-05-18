# 🌸 Iris Flower Classifier

A simple and interactive web application built with **Streamlit** that predicts the type of Iris flower based on user-defined features using different machine learning models.

## Project Structure

```

IRIS CLASSIFICATION/
├── Exported Models/
│   ├── Decision\_Tree.joblib
│   ├── KNN.joblib
│   ├── Logistic\_regression.joblib
│   └── svm\_model.joblib
├── Classifier\_UI.py
├── Iris\_Classification.ipynb
├── Iris.csv
└── .gitignore

````

- `Classifier_UI.py`: Streamlit web app interface.
- `Exported Models/`: Directory containing the trained machine learning models saved using `joblib`.
- `Iris_Classification.ipynb`: Notebook used for model training and export.
- `Iris.csv`: Dataset file used for training.
- `.gitignore`: Specifies files to ignore in version control.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/keneandita/iris-classification.git
cd iris-classification
````

### 2. Install Dependencies

Make sure you have Python 3.7+ and install required packages:

```bash
pip install streamlit scikit-learn joblib numpy
```

### 3. Run the Streamlit App

```bash
streamlit run Classifier_UI.py
```

---

## Dataset

The dataset used is the famous [Iris Flower Dataset](https://www.kaggle.com/datasets/uciml/iris), which contains 150 records with four features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

And three classes:

* Setosa
* Versicolor
* Virginica

---

## How It Works

1. Models are pre-trained and saved in the `Exported Models` directory.
2. `Classifier_UI.py` loads these models using `joblib`.
3. User inputs the feature values using Streamlit sliders.
4. The selected model predicts the flower type and displays the result instantly.

---

Created by [Kenean Dita](https://github.com/KeneanDita).
