import sqlite3

import numpy as np
import pandas as pd


CSV_FILE = "data/students.csv"
DATABASE_FILE = "student_dashboard.db"
MARK_COLUMNS = ["math_marks", "science_marks", "english_marks"]


def load_student_data(csv_file):
    """
    Step 1:
    Read the student CSV file and return a pandas DataFrame.
    """
    student_data = pd.read_csv(csv_file)
    return student_data


def clean_student_data(student_data):
    """
    Step 2:
    Fill missing numeric values using the median of each column.
    """
    cleaned_data = student_data.copy()
    numeric_columns = ["attendance"] + MARK_COLUMNS

    for column_name in numeric_columns:
        median_value = cleaned_data[column_name].median()
        cleaned_data[column_name] = cleaned_data[column_name].fillna(median_value)

    return cleaned_data


def add_features(student_data):
    """
    Step 3:
    Create new columns that help with analysis.
    """
    data_with_features = student_data.copy()

    # Calculate the average marks across all subjects
    data_with_features["average_marks"] = data_with_features[MARK_COLUMNS].mean(axis=1)

    # Decide whether the student passed or failed
    data_with_features["result"] = np.where(
        data_with_features["average_marks"] >= 40,
        "Pass",
        "Fail",
    )

    return data_with_features


def classify_risk(student_data):
    """
    Step 4:
    Mark students as at-risk if marks are low or attendance is low.
    """
    data_with_risk = student_data.copy()

    risk_condition = (
        (data_with_risk["average_marks"] < 40)
        | (data_with_risk["attendance"] < 60)
    )

    data_with_risk["at_risk"] = np.where(risk_condition, "Yes", "No")
    return data_with_risk


def calculate_kpis(student_data):
    """
    Step 5:
    Calculate simple summary values for the dashboard.
    """
    kpi_data = {}

    kpi_data["average_marks"] = round(student_data["average_marks"].mean(), 2)
    kpi_data["pass_count"] = int((student_data["result"] == "Pass").sum())
    kpi_data["fail_count"] = int((student_data["result"] == "Fail").sum())
    kpi_data["at_risk_count"] = int((student_data["at_risk"] == "Yes").sum())

    subject_performance = {}
    for column_name in MARK_COLUMNS:
        subject_performance[column_name] = round(student_data[column_name].mean(), 2)

    kpi_data["subject_performance"] = subject_performance
    return kpi_data


def save_to_database(student_data, kpi_data, database_file):
    """
    Step 6:
    Save processed data and KPI tables into SQLite.
    """
    connection = sqlite3.connect(database_file)

    student_data.to_sql("processed_students", connection, if_exists="replace", index=False)

    summary_table = pd.DataFrame(
        [
            {
                "average_marks": kpi_data["average_marks"],
                "pass_count": kpi_data["pass_count"],
                "fail_count": kpi_data["fail_count"],
                "at_risk_count": kpi_data["at_risk_count"],
            }
        ]
    )
    summary_table.to_sql("summary_kpis", connection, if_exists="replace", index=False)

    subject_rows = []
    for subject_name, average_score in kpi_data["subject_performance"].items():
        subject_rows.append(
            {
                "subject_name": subject_name,
                "average_score": average_score,
            }
        )

    subject_table = pd.DataFrame(subject_rows)
    subject_table.to_sql("subject_performance", connection, if_exists="replace", index=False)

    connection.close()


def show_all_students(student_data):
    """
    Display all students in a clean table format.
    """
    columns_to_show = [
        "student_id",
        "name",
        "cohort",
        "math_marks",
        "science_marks",
        "english_marks",
        "attendance",
        "average_marks",
        "result",
        "at_risk",
    ]
    print("\nAll Students")
    print(student_data[columns_to_show].to_string(index=False))


def show_at_risk_students(student_data):
    """
    Display only the students marked as at-risk.
    """
    at_risk_students = student_data[student_data["at_risk"] == "Yes"]

    print("\nAt-Risk Students")
    if at_risk_students.empty:
        print("No at-risk students found.")
    else:
        print(at_risk_students.to_string(index=False))


def show_summary_statistics(kpi_data):
    """
    Display the main KPI values.
    """
    print("\nSummary Statistics")
    print(f"Average Marks: {kpi_data['average_marks']}")
    print(f"Pass Count: {kpi_data['pass_count']}")
    print(f"Fail Count: {kpi_data['fail_count']}")
    print(f"At-Risk Count: {kpi_data['at_risk_count']}")

    print("\nSubject-Wise Performance")
    for subject_name, average_score in kpi_data["subject_performance"].items():
        print(f"{subject_name}: {average_score}")


def run_dashboard(student_data, kpi_data):
    """
    Step 7:
    Show a simple menu so the user can explore the data.
    """
    while True:
        print("\nStudent Analytics Dashboard")
        print("1. View all students")
        print("2. View at-risk students")
        print("3. View summary statistics")
        print("4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            show_all_students(student_data)
        elif user_choice == "2":
            show_at_risk_students(student_data)
        elif user_choice == "3":
            show_summary_statistics(kpi_data)
        elif user_choice == "4":
            print("Exiting dashboard. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    student_data = load_student_data(CSV_FILE)
    student_data = clean_student_data(student_data)
    student_data = add_features(student_data)
    student_data = classify_risk(student_data)
    kpi_data = calculate_kpis(student_data)
    save_to_database(student_data, kpi_data, DATABASE_FILE)
    run_dashboard(student_data, kpi_data)


if __name__ == "__main__":
    main()
