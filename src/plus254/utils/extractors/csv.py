import pandas as pd 

def get_table(
        url: str, 
        sheet_name: str = None
): 
    """
    Extracts a table from a CSV file located at the given URL.
    """
    if sheet_name:
        df = pd.read_excel(url, sheet_name=sheet_name)
    else:
        df = pd.read_csv(url)
    return df

