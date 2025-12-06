# Diabetes-Prediction
**Explanation of Data Processing**

load_dataset()

Reads your CSV file. Very simple, returns df.

replace_zero_with_median()

In PIMA dataset, some values like Glucose, BP, BMI cannot be 0.
They actually mean missing.
So we replace 0 with the median of that column.

remove_outliers()

Uses IQR method to remove extreme values.

split_features_labels()

X = Input features
y = Output (Outcome column) 

**Explanation (What will we do in Model Training)**

LogisticRegression → our machine learning model

train_test_split → divides data (80% train, 20% test)

StandardScaler → scales numeric features

accuracy_score, classification_report → check how good model is

Split dataset: 80% for training, 20% for testing

Scale the values for better model performance

Return all 4 parts

Create a Logistic Regression model

max_iter=1000 → helps avoid convergence issues

Train the model with training data

predict() → model guesses diabetes (0 or 1)

Accuracy = % correct predictions

Classification report shows:

Precision

Recall

F1-score

**Creat Fuzzy Logic**
numpy → for numeric range

skfuzzy → fuzzy membership functions + fuzzy rules

Universe of discourse:
Glucose values between 0–200

Membership functions:

Low glucose

Normal glucose

High glucose

interp_membership() tells how much the input belongs to each fuzzy set.

Example:
If glucose = 150
→ Might be 0.2 Normal
→ Might be 0.7 High

This is the beauty of fuzzy logic.

If glucose is low → risk score is low

If glucose is normal → medium risk

If glucose is high → high risk

Risk score will be between 20 to 90 depending on membership levels.

**Main.py(for full output)**






