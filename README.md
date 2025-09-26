🧹 Employee Dataset Cleaning with NumPy & Pandas
📌 Project Overview

This project focuses on cleaning and preprocessing a messy employee dataset using NumPy and Pandas.
The dataset contained issues such as missing values, inconsistent data types, outliers, and infinite values.
The goal was to transform the raw dataset into a clean, structured, and analysis-ready format.

⚙️ Data Cleaning Steps

🔹 Handling Null & Missing Values

Identified columns with missing data
Filled or removed null values depending on the context

🔹 Handling Outliers (💰 Salary Column)

Detected extreme outliers using IQR & Z-score methods
Removed or corrected unrealistic salary values

🔹 Fixing Data Types

Converted columns to appropriate types (int, float, datetime, category)
Ensured dataset consistency

🔹 Fixing Infinite Values ♾️

Replaced infinite values with NaN or meaningful defaults
Dropped affected records when necessary

🔹 Final Touches ✨

Standardized text/categorical fields
Prepared dataset for analysis or ML tasks

🛠️ Tools & Libraries

🐍 Python 3
🔢 NumPy
🐼 Pandas

📂 Project Structure
employee-dataset-cleaning/
│-- data/
│   ├── employee_dataset.csv     # Original messy dataset
│   ├── employee_cleaned_dataset.csv   # Cleaned dataset (final output)
│
│-- notebooks/
│   ├── data_cleaning.py  # Jupyter notebook with step-by-step cleaning
│
│-- README.md                # Project documentation

🚀 How to Run

Clone this repository

git clone https://github.com/Krishna111972/Employee-dataset-cleaning.git
cd employee-dataset-cleaning


Install dependencies

pip install pandas numpy


Run the Jupyter notebook or Python script to reproduce the cleaning steps

📊 Results

✅ No null or infinite values
✅ Salary column cleaned of outliers
✅ Correct data types applied
✅ Dataset ready for analysis & visualization

🔮 Future Improvements

🔁 Automate cleaning with reusable functions
📈 Add visualizations for outlier detection
⚡ Build a pipeline for large datasets
