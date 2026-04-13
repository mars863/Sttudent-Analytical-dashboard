# Student Analytics Dashboard

This is a beginner-friendly Python project that:

- Reads student data from a CSV file
- Cleans missing values using the median
- Creates simple new features such as average marks
- Finds at-risk students
- Calculates KPI values
- Stores results in SQLite
- Shows a simple CLI dashboard

## Project Structure

```text
student_analytics_dashboard/
|-- data/
|   |-- students.csv
|-- main.py
|-- requirements.txt
|-- student_dashboard.db   # created after running the program
```

## How to Run

1. Open a terminal in the `student_analytics_dashboard` folder.
2. Install packages:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

## Menu Options

- View all students
- View at-risk students
- View summary statistics
- Exit

## Beginner Improvements

1. Add a menu option to filter students by cohort.
2. Export at-risk students to a new CSV file.
