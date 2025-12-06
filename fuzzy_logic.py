import numpy as np
import skfuzzy as fuzz
def glucose_membership(glucose_value):
    # Universe of discourse
    x_glucose = np.arange(0, 201, 1)

    # Fuzzy sets
    low = fuzz.trimf(x_glucose, [0, 0, 100])
    normal = fuzz.trimf(x_glucose, [80, 120, 160])
    high = fuzz.trimf(x_glucose, [140, 200, 200])

    # Calculate membership
    low_val = fuzz.interp_membership(x_glucose, low, glucose_value)
    normal_val = fuzz.interp_membership(x_glucose, normal, glucose_value)
    high_val = fuzz.interp_membership(x_glucose, high, glucose_value)

    return {
        "Low": low_val,
        "Normal": normal_val,
        "High": high_val
    }
def fuzzy_risk_from_glucose(glucose_value):
    membership = glucose_membership(glucose_value)

    # Simple fuzzy rules
    low = membership["Low"]
    normal = membership["Normal"]
    high = membership["High"]

    # Defuzzified risk score (simple weighted sum)
    risk_score = (low * 20) + (normal * 50) + (high * 90)

    return risk_score
