# Project Report
## Student Performance Prediction Using Machine Learning

**Student Name:** ____________________  
**Roll Number:** ____________________  
**Department:** Computer Science and Engineering  
**Course/Year:** First-Year CSE  
**Submitted to:** ____________________  
**Date:** ____________________

---

## 1. Abstract

This project demonstrates how a basic machine-learning model can estimate a student's exam score from a small set of study and academic indicators. A Linear Regression model is trained using Python and scikit-learn. The input variables are daily study hours, attendance percentage, previous exam score, sleep hours, and extracurricular participation. The dataset supplied with the project is synthetic and is used only for educational demonstration. The model is evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²).

## 2. Introduction

Machine learning uses examples to learn patterns that can be used to make predictions on new inputs. In this project, regression is used because the output—an estimated exam score—is numerical. The project provides a small, reproducible example of the typical ML workflow: preparing data, splitting it into training and testing sets, fitting a model, evaluating it, and generating a prediction.

This is a learning demonstration, not a tool for assessing real students.

## 3. Problem Statement

Build a beginner-friendly program that accepts selected student-related indicators and estimates an exam score using a supervised machine-learning algorithm.

## 4. Objectives

1. Understand the difference between features and a target variable.
2. Load tabular data using pandas.
3. train a regression model using scikit-learn.
4. Evaluate predictions on held-out test data.
5. Plot actual-versus-predicted values and study-hours-versus-score data.
6. Document limitations and responsible use.

## 5. Tools and Technologies

- **Language:** Python
- **Libraries:** pandas, NumPy, scikit-learn, Matplotlib
- **Data format:** CSV
- **Algorithm:** Linear Regression
- **Development environment:** VS Code, PyCharm, Jupyter-supported Python environment, or terminal

## 6. Dataset Description

The included CSV contains 240 synthetic rows. It was generated for this project with a fixed random seed and does not contain real or identifiable student records.

| Variable | Description |
|---|---|
| Study hours per day | Average daily study time |
| Attendance percentage | Percentage of classes attended |
| Previous exam score | Earlier score out of 100 |
| Sleep hours per day | Average daily sleep duration |
| Extracurricular participation | Binary input: 0 = No, 1 = Yes |
| Exam score | Target value to estimate, out of 100 |

The input features are not exhaustive. Many factors that affect learning are absent, and the sample data should not be treated as evidence about real student populations.

## 7. Methodology

### Step 1: Data loading
The program reads `data/student_performance.csv` using pandas and checks that required columns exist.

### Step 2: Feature and target selection
The five explanatory columns are assigned to `X`, and `exam_score` is assigned to `y`.

### Step 3: Train-test split
The dataset is split into 80% training data and 20% testing data. A fixed random state makes the split reproducible.

### Step 4: Model training
Linear Regression is fitted to the training examples. It learns coefficients that minimize squared prediction errors on the training set.

### Step 5: Evaluation
The trained model predicts scores for the held-out test examples. MAE, RMSE, and R² are calculated to summarize performance.

### Step 6: Visualization and example prediction
The program saves two charts in `outputs/` and demonstrates a prediction for a hypothetical student.

## 8. System Workflow

```text
Start
  |
Read CSV dataset
  |
Select input features and target
  |
Split into training and testing sets
  |
Train Linear Regression model
  |
Predict test-set scores
  |
Calculate MAE, RMSE, and R²
  |
Save charts
  |
Predict an example student score
  |
End
```

## 9. Evaluation Metrics

- **Mean Absolute Error (MAE):** the average absolute difference between predicted and actual test scores. Lower values indicate smaller average errors.
- **Root Mean Squared Error (RMSE):** the square root of the average squared error. It gives extra weight to larger errors. Lower values are preferred.
- **R² score:** measures performance relative to predicting the mean target value. A value closer to 1 is generally better, while a negative value can indicate poor performance.

### Results

Run `python main.py` to calculate the metrics for the included dataset. Record the actual output from your own run here before submitting:

| Metric | Your run's value |
|---|---|
| MAE | ____________________ |
| RMSE | ____________________ |
| R² | ____________________ |

Results are intentionally not hard-coded in this report; they are computed when the program runs.

## 10. How to Run

1. Install Python 3.10 or newer.
2. Open a terminal in the project directory.
3. Install libraries using `python -m pip install -r requirements.txt`.
4. Run `python main.py`.
5. Review the metrics and the two PNG charts in `outputs/`.
6. To try a custom example, run `python main.py --predict 4 85 72 7 1`.

The example values mean 4 study hours per day, 85% attendance, previous score 72, 7 sleep hours, and extracurricular participation = Yes.

## 11. Expected Output

The program prints the number of rows, train/test sizes, three evaluation metrics, the paths where charts are saved, and an example estimated score. Exact values are produced by the code and should be copied from the student's own run.

## 12. Limitations and Ethical Considerations

1. The dataset is synthetic and cannot validate real-world performance.
2. The model may be inaccurate for individuals or for data that differs from the sample.
3. A model association does not establish causation.
4. Student-related data can be sensitive; real data should only be used with appropriate permission, privacy safeguards, and instructor approval.
5. Predictions should not be used for grading, admissions, discipline, scholarships, or other high-impact decisions.
6. Model results must be interpreted with human judgment and awareness of uncertainty.

## 13. Future Scope

- Test additional algorithms such as Decision Tree Regression and Random Forest Regression.
- Evaluate with cross-validation.
- Add a simple web interface.
- Use a larger, documented dataset with appropriate permission.
- Study model errors and fairness before any real-world research use.

## 14. Conclusion

This project demonstrates a complete introductory regression workflow: loading a dataset, selecting features, splitting data, training Linear Regression, measuring prediction error, visualizing results, and predicting an example value. It is suitable for learning the foundations of machine learning and for further experimentation. Because the dataset is synthetic, the model should be regarded strictly as an educational prototype.

## 15. References

1. scikit-learn documentation: https://scikit-learn.org/stable/
2. pandas documentation: https://pandas.pydata.org/docs/
3. NumPy documentation: https://numpy.org/doc/
4. Matplotlib documentation: https://matplotlib.org/stable/
