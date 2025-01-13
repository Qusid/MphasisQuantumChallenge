import qiskit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dimod
import requests
from io import StringIO,BytesIO
from dwave.system import DWaveSampler, EmbeddingComposite

##Need to make repo public for link to work
repo_url = "https://github.com/Qusid/MphasisQuantumChallenge"
file_path = "data/PRMI-DM_TARGET_FLIGHTS.csv"
file_type = "csv"

def extract_affected_flights(repo_url, file_path, file_type='csv'):
    """
    Extracts rows as dictionaries from a file hosted in a GitHub repository.

    Parameters:
    repo_url (str): The URL of the GitHub repository (raw file URL).
    file_path (str): Path to the file in the repository.
    file_type (str): Type of the file ('csv' or 'excel').

    Returns:
    list: A list of dictionaries, each representing a row in the file.
    """
    # Build the raw URL
    raw_url = f"{repo_url}/raw/main/{file_path}"

    # Fetch the file from GitHub
    response = requests.get(raw_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch file. HTTP Status Code: {response.status_code}")

    # Read the file into a DataFrame
    if file_type == 'csv':
        dataframe = pd.read_csv(StringIO(response.text))
    elif file_type in ('xls', 'xlsx'):
        dataframe = pd.read_excel(BytesIO(response.content))
    else:
        raise ValueError("Unsupported file type. Only 'csv' and 'excel' are supported.")

    # Convert the DataFrame to a list of dictionaries
    rows_as_dicts = dataframe.to_dict(orient='records')

    return rows_as_dicts



affected_flights = extract_affected_flights(repo_url, file_path, file_type)

# Print the extracted data
for row in affected_flights:
    print(row)