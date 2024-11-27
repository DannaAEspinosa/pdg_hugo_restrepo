import pandas as pd

def load_data(filepath, sheet_name=0):
    """
    Loads an Excel file into a DataFrame.
    
    Args:
        filepath (str): Path to the Excel file.
        sheet_name (str or int): Name or index of the sheet to load. Defaults to the first sheet.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    print(f"Column names in the loaded DataFrame: {df.columns.tolist()}")
    return df
    
def save_data(df, output_path, file_name):
    """
    Saves a DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): DataFrame to be saved.
        output_path (str): Directory path where the file will be saved.
        file_name (str): Name of the CSV file.
    """
    file_path = f"{output_path}/{file_name}"
    df.to_csv(file_path, index=False)
    print(f"Saved: {file_path}")

def clean_data(df):
    # Imprimir el DataFrame antes de la limpieza
    print("Initial DataFrame:")
    print(df.head())
    print(f"Initial number of rows: {len(df)}")

    # Selección de columnas
    columns_to_keep = [
        'ACTIVOS', 'Código Agricultor', 'EMPRESA', 'PRIMER NOMBRE', 'SEGUNDO NOMBRE',
        'PRIMER APELLIDO', 'SEGUNDO APELLIDO', 'CEDULA', 'IDENTIFICACION  EN EL REGISTRO DEL CONTRATO',
        'RUT', 'CORREO ELECTRONICO', 'CONTACTO', 'CELULAR', 'Ciudad/Pueblo',
        'Departamento', 'Técnico Agrícola', 'ESTACIÓN DE MOLIENDA', 'VARIEDAD',
        'CONTRATO', 'Código Cultivo'
    ]

    # Verificar y conservar solo las columnas que existen en el DataFrame
    missing_columns = [col for col in columns_to_keep if col not in df.columns]
    if missing_columns:
        print(f"Warning: Missing columns in DataFrame: {missing_columns}")

    columns_to_keep = [col for col in columns_to_keep if col in df.columns]
    df = df[columns_to_keep]

    # Imprimir después de la selección de columnas
    print("DataFrame after column selection:")
    print(df.head())
    print(f"Number of rows after column selection: {len(df)}")

    # Limpieza adicional: eliminar filas con valores nulos en las columnas seleccionadas
    df = df.dropna(how='any')
    print(f"Number of rows after dropping rows with any NAs: {len(df)}")

    # Opcional: más limpieza de datos, como eliminación de filas duplicadas
    df = df.drop_duplicates()
    print(f"Number of rows after dropping duplicates: {len(df)}")

    # Verificar si alguna columna tiene un alto porcentaje de valores nulos y considerar eliminarla
    threshold = 0.5  # Umbral del 50% de valores no nulos
    df = df.loc[:, df.isnull().mean() < threshold]
    print(f"Number of columns after removing those with > {threshold*100}% missing values: {len(df.columns)}")

    return df
