import pandas as pd  # 'numpy as np' removed since it is unused


def load_data(filepath):
    """
    Loads data from a CSV file.
    """
    data = pd.read_csv(filepath)
    print("Data loaded:", data.head())
    return data


def process_data(data):
    """
    Adds a new column to the data based on the Age column.
    """
    data['new_column'] = data['Age'] * 2
    print("New column added")
    return data


def main():
    """
    Main function to load, process, and display the data.
    """
    df = load_data("datasets/titanic.csv")
    df = process_data(df)  # Removed unused 'result' variable
    print("Processing Complete")


main()
