import qiskit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dimod
import requests
from io import StringIO,BytesIO
from dwave.system import DWaveSampler, EmbeddingComposite


def extract_affected_flights(raw_url, file_type='csv'):
    print("Fetching data from:", raw_url)

    # Fetch the raw file
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(raw_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch file. HTTP Status Code: {response.status_code}")

    # Load the file into a DataFrame
    if file_type == 'csv':
        dataframe = pd.read_csv(StringIO(response.text))
    elif file_type in ('xls', 'xlsx'):
        from io import BytesIO
        dataframe = pd.read_excel(BytesIO(response.content))
    else:
        raise ValueError("Unsupported file type. Only 'csv' and 'excel' are supported.")

    return dataframe


# Correct raw URL
raw_url = "https://raw.githubusercontent.com/Qusid/MphasisQuantumChallenge/main/Data/PRMI-DM_TARGET_FLIGHTS.csv"


affected_flights = extract_affected_flights(raw_url)

# Call the function and display results
dataframe = extract_affected_flights(raw_url)
print(dataframe)  # Preview the first few rows