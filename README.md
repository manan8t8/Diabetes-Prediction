# Diabetes-Prediction
Explanation of Data Processing
✔ load_dataset()

Reads your CSV file. Very simple, returns df.

✔ replace_zero_with_median()

In PIMA dataset, some values like Glucose, BP, BMI cannot be 0.
They actually mean missing.
So we replace 0 with the median of that column.

✔ remove_outliers()

Uses IQR method to remove extreme values.

✔ split_features_labels()

X = Input features
y = Output (Outcome column)
