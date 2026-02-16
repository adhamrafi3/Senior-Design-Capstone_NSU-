import pandas as pd
from sklearn.impute import SimpleImputer
from joblib import load
import pandas as pd
import streamlit as st
from joblib import load
from sklearn.impute import SimpleImputer

# Load the model and scaler
model_path = r'_meta_model.pkl'
scaler_path = r'scaler.pkl'
model = load(model_path)
scaler = load(scaler_path)


def preprocess_input(input_dict):
    expected_columns = [
        'SC_AGE_YEARS', 'sex_2122', 'allergies_2122', 'asthma_2122',
        'headache_2122', 'anxiety_2122', 'depress_2122', 'behavior_2122',
        'GeneticScr_2122', 'BrainInjTold_2122', 'ACE2more6HH_2122',
        'famstruct5_2122', 'fruit_2122', 'vegetables_2122', 'Cond2more_2122',
        'CSHCNtype_2122', 'ChHlthSt_2122', 'ExBrstFd_2122', 'DevDelay_2122',
        'learning_2122', 'autism_2122', 'BedTime_2122', 'ACE1more4Com_2122',
        'ACEincome_2122', 'ACE2more11_2122'
    ]

    mappings = {
        'sex_2122': {'Male': 1, 'Female': 2},
        'allergies_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                           'Currently has condition': 3},
        'asthma_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                        'Currently has condition': 3},
        'headache_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                          'Currently has condition': 3},
        'anxiety_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                         'Currently has condition': 3},
        'depress_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                         'Currently has condition': 3},
        'behavior_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                          'Currently has condition': 3},
        'GeneticScr_2122': {'Never had condition': 1, 'Ever told, not identified by test': 2,
                            'Ever told, identified by test': 3},
        'BrainInjTold_2122': {'Never thought child has injury': 1, 'Ever thought, not confirmed': 2,
                              'Ever had injury confirmed by doctor': 3},
        'ACE2more6HH_2122': {'No ACEs': 1, '1 ACE': 2, '2 or more ACEs': 3},
        'famstruct5_2122': {'Two parents, married': 1, 'Two parents, not married': 2, 'Single parent': 3,
                            'Grandparent household': 4, 'Other family type': 5},
        'fruit_2122': {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Regularly': 4, 'Often': 5, 'Always': 6},
        'vegetables_2122': {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Regularly': 4, 'Often': 5, 'Always': 6},
        'Cond2more_2122': {'None': 1, 'One condition': 2, 'Multiple conditions': 3},
        'CSHCNtype_2122': {'None': 0, 'Functional limitations': 1, 'Prescription medication only': 2,
                           'Above-routine use of services': 3, 'Medication and above-routine services': 4},
        'ChHlthSt_2122': {'Excellent': 1, 'Good': 2, 'Fair or Poor': 3},
        'ExBrstFd_2122': {'Never': 1, 'Less than 6 months': 2, '6 months regular not exclusively': 3,
                          '6 months exclusively': 4},
        'DevDelay_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                          'Currently has condition': 3},
        'learning_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                          'Currently has condition': 3},
        'autism_2122': {'Does not have condition': 1, 'Ever told, does not currently have': 2,
                        'Currently has condition': 3},
        'BedTime_2122': {'Always': 1, 'Usually': 2, 'Sometimes': 3, 'Rarely or never': 4},
        'ACE1more4Com_2122': {'No ACEs': 1, '1 or more ACEs': 2},
        'ACEincome_2122': {'No ACEs': 1, 'Rarely': 2, 'Often': 3, 'Very Often': 4},
        'ACE2more11_2122': {'No Aces': 1, 'Single Ace': 2 , 'Multiple Aces':3},
    }

    processed_dict = {col: (mappings[col][input_dict[col]] if col in mappings else input_dict[col]) for col in
                      expected_columns}

    input_df = pd.DataFrame([processed_dict], columns=expected_columns)

    imputer = SimpleImputer(strategy='most_frequent')
    input_df = pd.DataFrame(imputer.fit_transform(input_df), columns=expected_columns)

    if input_df.isnull().any().any():
        raise ValueError("NaN values detected after imputation.")

    return input_df


def predict(input_dict):
    # Preprocess the input data to ensure it matches the model's expectations
    input_df = preprocess_input(input_dict)

    # Scale the data
    scaled_data = scaler.transform(input_df)

    # Predict using the model
    prediction = model.predict(scaled_data)

    result = "ADHD Positive" if prediction[0] == 1 else "ADHD Negative"
    print(f"Prediction: {result}")
    return result