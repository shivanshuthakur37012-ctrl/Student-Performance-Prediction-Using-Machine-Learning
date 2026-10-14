"""
Student Performance Prediction
Beginner-friendly regression project using scikit-learn.

Run:
    python main.py
    python main.py --predict 4 85 72 7 1

Prediction arguments:
    study hours/day, attendance %, previous exam score, sleep hours/day,
    extracurricular participation (0 = No, 1 = Yes)
"""
from pathlib import Path
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "student_performance.csv"
OUTPUT_DIR = ROOT / "outputs"
FEATURES = [
    "study_hours_per_day",
    "attendance_percent",
    "previous_exam_score",
    "sleep_hours_per_day",
    "extracurricular_participation",
]
TARGET = "exam_score"


def load_data():
    """Load the sample CSV and check that required columns exist."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. Make sure the data folder is included."
        )
    data = pd.read_csv(DATA_PATH)
    missing = set(FEATURES + [TARGET]) - set(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {sorted(missing)}")
    return data


def train_model(data):
    """Split the data, train a Linear Regression model, and report metrics."""
    X = data[FEATURES]
    y = data[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print("\n=== Student Performance Prediction ===")
    print(f"Dataset rows: {len(data)}")
    print(f"Training rows: {len(X_train)} | Testing rows: {len(X_test)}")
    print("\nEvaluation on held-out test data:")
    print(f"MAE  (lower is better): {mae:.2f} marks")
    print(f"RMSE (lower is better): {rmse:.2f} marks")
    print(f"R²   (closer to 1 is generally better): {r2:.3f}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    make_plots(y_test, predictions, data)
    print(f"\nCharts saved in: {OUTPUT_DIR}")
    return model


def make_plots(actual, predicted, data):
    """Save a prediction comparison chart and a study-hours scatter plot."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(7, 5))
    plt.scatter(actual, predicted, alpha=0.75)
    plt.plot([0, 100], [0, 100], linestyle="--")
    plt.xlabel("Actual exam score")
    plt.ylabel("Predicted exam score")
    plt.title("Actual vs Predicted Exam Scores")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "actual_vs_predicted.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 5))
    plt.scatter(data["study_hours_per_day"], data[TARGET], alpha=0.65)
    plt.xlabel("Study hours per day")
    plt.ylabel("Exam score")
    plt.title("Study Hours vs Exam Score (Sample Dataset)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_score.png", dpi=150)
    plt.close()


def predict_one(model, values):
    """Print a prediction for one hypothetical student."""
    study, attendance, previous, sleep, extra = values
    if not (0 <= study <= 24):
        raise ValueError("Study hours must be between 0 and 24.")
    if not (0 <= attendance <= 100):
        raise ValueError("Attendance must be between 0 and 100.")
    if not (0 <= previous <= 100):
        raise ValueError("Previous exam score must be between 0 and 100.")
    if not (0 <= sleep <= 24):
        raise ValueError("Sleep hours must be between 0 and 24.")
    if extra not in (0, 1):
        raise ValueError("Extracurricular participation must be 0 (No) or 1 (Yes).")

    row = pd.DataFrame([{
        FEATURES[0]: study,
        FEATURES[1]: attendance,
        FEATURES[2]: previous,
        FEATURES[3]: sleep,
        FEATURES[4]: extra,
    }])
    result = float(model.predict(row)[0])
    result = max(0.0, min(100.0, result))
    print("\nPrediction for the entered example:")
    print(f"Estimated exam score: {result:.1f}/100")
    print("Note: This is an educational estimate, not a reliable judgment of a student.")


def main():
    parser = argparse.ArgumentParser(description="Predict a student's exam score.")
    parser.add_argument(
        "--predict", nargs=5, type=float, metavar=("STUDY", "ATTENDANCE", "PREVIOUS", "SLEEP", "EXTRA"),
        help="Predict score: study hours, attendance percent, previous score, sleep hours, extracurricular (0/1)."
    )
    args = parser.parse_args()

    data = load_data()
    model = train_model(data)

    if args.predict:
        predict_one(model, args.predict)
    else:
        print("\nExample prediction:")
        predict_one(model, [4, 85, 72, 7, 1])


if __name__ == "__main__":
    main()
