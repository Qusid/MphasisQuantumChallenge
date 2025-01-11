import qiskit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dimod
from dwave.system import DWaveSampler, EmbeddingComposite

## I think there are ways to extract the file from a cloud or github repo but for now just use local file path

##To get code to run just upload filepath from your own device
filepath = "C:/Users/felix\Downloads\PRMI-DM_TARGET_FLIGHTS.csv"


def extract_affected_flights(filepath):
    """
    Reads a file into a DataFrame and extracts each column into its own dictionary, using the DEP_KEY column as the key.

    Parameters:
    filepath (str): The path to the input file (CSV or Excel).

    Returns:
    dict: A dictionary where each column (except the key column) is represented as a separate dictionary.
    """
    # Determine file type and load data accordingly
    if filepath.endswith('.csv'):
        dataframe = pd.read_csv(filepath)
    elif filepath.endswith(('.xls', '.xlsx')):
        dataframe = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    # Convert the DataFrame to a list of dictionaries (row-wise)
    rows = dataframe.to_dict(orient='records')

    return rows


# Extract and print data to ensure function works
affected_flights = extract_affected_flights(filepath)
print(affected_flights)

