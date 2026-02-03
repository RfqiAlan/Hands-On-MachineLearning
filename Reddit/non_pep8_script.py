import pandas as pd, numpy as np # Multiple imports on one line

def Load_Data(filepath): # Function name should be lowercase with underscores
    data=pd.read_csv(filepath) # No spaces around '='
    print("Data loaded:",data.head()) # No space after the comma
    return data

def Process_Data(data): # Function name should be lowercase with underscores
    data['new_column'] = data['Age']* 2 # Inconsistent spacing around operators
    print("New column added") # Missing blank line above function
    return data

def main(): # Missing two blank lines above function definition
    df=Load_Data("datasets/titanic.csv") # No spaces around '='
    result=Process_Data(df) # No spaces around '='
    print("Processing Complete") # Missing newline at end of file

main()
