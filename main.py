from data_processing import load_dataset, replace_zero_with_median, remove_outliers, split_features_labels
from model_training import scale_data, train_model, evaluate_model
from fuzzy_logic import fuzzy_risk_from_glucose

def main():
    # 1. Load dataset
    df = load_dataset("diabetes.csv")
    print("Dataset loaded successfully!")
    print(df.head())

    # 2. Replace zeros with median
    df = replace_zero_with_median(df)

    # 3. Remove outliers
    df = remove_outliers(df)

    # 4. Split into X and y
    X, y = split_features_labels(df)

    # 5. Scale + Train + Evaluate
    X_train, X_test, y_train, y_test = scale_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    # 6. Fuzzy Logic Example
    risk = fuzzy_risk_from_glucose(150)
    print("\nFuzzy Diabetes Risk for glucose=150:", risk)

if __name__ == "__main__":
    main()
