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

```project-structure
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

```sample_output
The predicted class is Setosa using Logistic Regression!
```

Confidence Scores:

* Setosa: 97.3%
* Versicolor: 2.6%
* Virginica: 0.1%

Author: [Kenean Dita](https://github.com/keneandita/)# 🌸 Iris Flower Classifier
