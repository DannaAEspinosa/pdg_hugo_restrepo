import pandas as pd

def load_data(filepath):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def save_data(df, output_path, file_name):
    """
    Save a DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The directory path to save the file.
        file_name (str): The name of the CSV file.
    """
    file_path = f"{output_path}/{file_name}"
    df.to_csv(file_path, index=False)
    print(f"Saved: {file_path}")

def clean_data(df, output_path="data/processed"):
    """
    Clean the data and save rows with null values and duplicates to separate files.

    Args:
        df (pd.DataFrame): The original DataFrame.
        output_path (str): The folder to save the processed files.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Save duplicates before removing them
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        save_data(duplicates, output_path, "duplicated_rows.csv")
    
    # Save rows with null values before handling them
    null_data = df[df.isnull().any(axis=1)]
    if not null_data.empty:
        save_data(null_data, output_path, "null_rows.csv")
    
    # Remove duplicates and rows with null values
    df = df.drop_duplicates()
    df = df.dropna()
    
    return df
