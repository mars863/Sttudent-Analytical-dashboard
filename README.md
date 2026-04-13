# Student Analytical Dashboard

## Overview

Student Analytical Dashboard is a Python-based command-line analytics project that processes student academic records and turns raw CSV data into actionable insights. The application cleans incomplete data, calculates academic performance metrics, identifies at-risk students, and stores the processed results in a SQLite database for further analysis.

This project demonstrates practical skills in data processing, feature engineering, business logic design, and lightweight data persistence using Python.

## Problem Statement

Educational teams often collect student performance data in spreadsheets, but raw records alone do not make it easy to identify patterns, measure outcomes, or intervene early when students begin to struggle.

Without a structured analytics workflow, it becomes difficult to:

- handle missing or incomplete student records
- measure overall academic performance consistently
- identify students who may need intervention
- generate quick summaries for decision-making
- preserve cleaned and processed data for later reporting

## Solution

This project solves the problem by building a simple end-to-end analytics pipeline:

1. Student data is loaded from a CSV file.
2. Missing numeric values are cleaned using median-based imputation.
3. New analytical fields are generated, including average marks and pass/fail status.
4. Students are flagged as at-risk based on low average marks or poor attendance.
5. Key performance indicators are calculated for overall and subject-wise performance.
6. Processed data is saved into a SQLite database for structured storage.
7. A menu-driven CLI dashboard allows users to explore student records and summary insights.

## Features

- Loads student data from a CSV source
- Cleans missing values in marks and attendance columns
- Calculates average marks across Math, Science, and English
- Classifies students as `Pass` or `Fail`
- Flags at-risk students using performance and attendance rules
- Generates summary KPIs such as average marks, pass count, fail count, and at-risk count
- Computes subject-wise average performance
- Stores processed output in SQLite tables
- Provides a simple command-line dashboard for exploring results

## Tech Stack

- Python
- Pandas
- NumPy
- SQLite

## Project Structure

```text
student_analytics_dashboard/
|-- data/
|   |-- students.csv
|-- main.py
|-- requirements.txt
|-- student_dashboard.db
|-- README.md
```

## Installation

### Prerequisites

- Python 3.x
- `pip`

### Setup Steps

```bash
git clone https://github.com/mars863/Sttudent-Analytical-dashboard.git
cd Sttudent-Analytical-dashboard/student_analytics_dashboard
pip install -r requirements.txt
```

## How To Run

Run the project from inside the `student_analytics_dashboard` folder:

```bash
python main.py
```

After execution starts, the CLI dashboard will display a menu:

```text
Student Analytics Dashboard
1. View all students
2. View at-risk students
3. View summary statistics
4. Exit
```

## Example Output

Using the sample dataset included in `data/students.csv`, choosing option `3` shows summary statistics similar to the following:

```text
Summary Statistics
Average Marks: 56.83
Pass Count: 7
Fail Count: 3
At-Risk Count: 4

Subject-Wise Performance
math_marks: 56.6
science_marks: 58.4
english_marks: 55.5
```

Choosing option `2` lists the students identified as at-risk. In the current sample dataset, students are marked as at-risk if:

- their average marks are below `40`, or
- their attendance is below `60`

This means the dashboard not only highlights students who are failing academically, but also students who may still be passing while showing attendance-related risk.

## Database Output

When the program runs, it writes processed results to `student_dashboard.db` and creates or refreshes these tables:

- `processed_students`
- `summary_kpis`
- `subject_performance`

This makes the project useful not only as a CLI dashboard, but also as a foundation for future reporting or visualization layers.

## Why This Project Stands Out

This project is a strong portfolio example because it demonstrates:

- data cleaning and preprocessing
- analytical thinking and KPI design
- rule-based student risk classification
- structured data persistence with SQLite
- practical Python programming for real-world use cases

## Future Improvements

- Add cohort-wise filtering and comparison
- Build a web dashboard using Streamlit, Flask, or Django
- Add charts for trends and subject performance
- Export reports to CSV or PDF
- Add configurable risk thresholds
- Include automated tests for the analytics pipeline
- Support larger datasets and more subjects

## Conclusion

Student Analytical Dashboard is a compact but practical analytics project that shows how Python can be used to transform raw academic data into meaningful insights. It is well suited for demonstrating foundational skills in data analysis, backend logic, and problem solving in an education-focused use case.
