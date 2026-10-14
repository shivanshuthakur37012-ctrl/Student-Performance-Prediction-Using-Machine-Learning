# Student Performance Prediction using Machine Learning

A beginner-friendly first-year CSE project that estimates a student's exam score from study habits and academic indicators using **Linear Regression**.

> **Important:** The included CSV is a synthetic, illustrative dataset created for learning and demonstration. It is not real student data, and the predictions must not be used to grade, rank, admit, or make high-impact decisions about students.

## Features

- Loads a sample dataset from a CSV file.
- Trains a Linear Regression model using scikit-learn.
- Evaluates the model using MAE, RMSE, and R².
- Saves two charts in the `outputs/` folder.
- Predicts an example student's estimated score.
- Accepts custom student values from the command line.

## Project structure

```text
student_performance_prediction/
├── data/
│   └── student_performance.csv
├── outputs/                    # Charts are created here when you run the code
├── main.py
├── requirements.txt
├── README.md
└── PROJECT_REPORT.md
```

## Requirements

- Python 3.10 or newer recommended
- Internet access for the first installation of the Python libraries

## Setup and run

### 1. Download or clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/student-performance-prediction.git
cd student-performance-prediction
```

Or download the ZIP and extract it.

### 2. (Recommended) Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

The terminal prints model evaluation metrics and an example prediction. Two charts are saved in `outputs/`.

### 5. Predict for a hypothetical student

The command takes five values in this order:

1. Study hours per day
2. Attendance percentage
3. Previous exam score (out of 100)
4. Sleep hours per day
5. Extracurricular participation (`0` = No, `1` = Yes)

Example:

```bash
python main.py --predict 4 85 72 7 1
```

This example means 4 study hours/day, 85% attendance, previous score 72, 7 hours of sleep/day, and extracurricular participation = Yes.

## Dataset columns

| Column | Meaning | Example/range |
|---|---|---|
| `study_hours_per_day` | Average hours spent studying each day | 0.5–8 in sample |
| `attendance_percent` | Attendance percentage | 50–100 in sample |
| `previous_exam_score` | Previous exam score out of 100 | 30–95 in sample |
| `sleep_hours_per_day` | Average sleep hours each day | 4–9.5 in sample |
| `extracurricular_participation` | Whether the student participates in extracurricular activities | 0 or 1 |
| `exam_score` | Target value: sample exam score out of 100 | 0–100 |

The provided 240-row dataset is synthetic and generated with a fixed random seed so results are reproducible.

## How it works

1. **Load data:** pandas reads the CSV.
2. **Choose features and target:** the five input columns are features (`X`); `exam_score` is the target (`y`).
3. **Split data:** 80% for training and 20% for testing, using a fixed random seed.
4. **Train:** Linear Regression learns a relationship between the inputs and exam score.
5. **Evaluate:** MAE, RMSE, and R² summarize test-set performance.
6. **Visualize:** charts compare predicted and actual scores and show the relationship between study hours and score.
7. **Predict:** the trained model estimates a score for one hypothetical student.

## Metrics explained

- **MAE:** average absolute difference between predicted and actual scores, in marks. Lower is better.
- **RMSE:** similar to MAE but penalizes larger errors more strongly. Lower is better.
- **R²:** compares model performance with predicting the test-set mean. A value closer to 1 is generally better; it can be negative.

Metrics vary if you change the dataset or code. Because this is synthetic data, good scores do not demonstrate real-world validity.

## Limitations and responsible use

- The data is synthetic, not collected from students.
- Real student performance depends on many factors not included here.
- Correlation does not prove causation; this model cannot show that changing one input will cause a score change.
- Model outputs are estimates and can be wrong.
- Do not use the model for grading, admissions, discipline, scholarships, or any consequential decision.
- For real research, use appropriately consented, anonymized data and discuss fairness, privacy, and limitations with your instructor.

## Future improvements

- Compare Linear Regression with Decision Tree and Random Forest models.
- Use cross-validation and a larger, documented real dataset where permitted.
- Add a simple Streamlit interface.
- Analyze feature importance carefully and include fairness checks.

## Author

**Student Name:** Add your name  
**Course:** First-Year CSE / AI-ML  
**Project:** Student Performance Prediction using Machine Learning
