from ydata_profiling import ProfileReport

def generate_profile(df, output_file):
    """
    Generates an EDA report using YData Profiling for a given DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to be analyzed.
        output_file (str): The path where the HTML report will be saved.
    """
    profile = ProfileReport(df, title="EDA Report", explorative=True)
    profile.to_file(output_file)
