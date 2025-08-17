# 🌸 Iris Intel

An interactive **Streamlit web app** for predicting the type of Iris flower based on its features.
This project uses multiple machine learning models trained on the classic [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

## Features

* Interactive **web interface** powered by Streamlit.
* Supports multiple ML models:

  * Logistic Regression
  * K-Nearest Neighbors (KNN)
  * Support Vector Machine (SVM)
  * Decision Tree
* User-friendly sliders to input flower measurements.
* Displays the **predicted class** along with **confidence scores**.
* Clean and responsive UI.

## Models

All models are pre-trained and stored as `.joblib` files inside the `Exported Models/` folder:

* `Logistic_regression.joblib`
* `KNN.joblib`
* `svm_model.joblib`
* `Decision_Tree.joblib`


## 🛠 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/keneandita/iris-intel.git
   cd iris-intel
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/Mac
   .\venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run Stream.py
   ```

---

## 📂 Project Structure

```
Iris-Intel/
│── Exported Models/
│   ├── Logistic_regression.joblib
│   ├── KNN.joblib
│   ├── svm_model.joblib
│   ├── Decision_Tree.joblib
│
│── Iris_Classification.ipynb   # ML training notebook 
│── Stream.py              # Main Streamlit app
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Demo

**Input example**:

* Sepal Length: `5.1 cm`
* Sepal Width: `3.5 cm`
* Petal Length: `1.4 cm`
* Petal Width: `0.2 cm`

**Output**:

```
The predicted class is Setosa using Logistic Regression!
```

Confidence Scores:

* Setosa: 97.3%
* Versicolor: 2.6%
* Virginica: 0.1%

Author: [Kenean Dita](https://github.com/keneandita/)# 🌸 Iris Flower Classifier

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
