from ydata_profiling import ProfileReport

def generate_profile(df, output_file):
    """
    Generates a YData Profiling report for a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze.
        output_file (str): Path where the HTML report will be saved.
    """
    profile = ProfileReport(df, title="EDA Report", explorative=True)
    profile.to_file(output_file)

def analyze_with_pandas(df):
    """
    Complements the analysis with pandas.
    """
    print("General overview:")
    print(df.info())
    
    print("\nStatistical description:")
    print(df.describe())
    
    print("\nNull value distribution:")
    print(df.isnull().sum())
    
    print("\nUnique values per column:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")
