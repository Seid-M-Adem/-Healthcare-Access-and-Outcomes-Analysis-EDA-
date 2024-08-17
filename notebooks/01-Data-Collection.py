import pandas as pd
import os

def load_csv(file_path, encoding='utf-8'):
    """Load a CSV file into a DataFrame with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File {file_path} does not exist.")
    
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        if df.empty:
            raise ValueError(f"Error: File {file_path} is empty.")
        if df.columns.empty:
            raise ValueError(f"Error: File {file_path} has no columns.")
        return df
    except pd.errors.EmptyDataError:
        raise ValueError(f"Error: No columns to parse from file {file_path}.")
    except pd.errors.ParserError:
        raise ValueError(f"Error: Parsing error in file {file_path}.")
    except Exception as e:
        raise RuntimeError(f"Error loading {file_path}: {e}")

# Define file paths relative to the workspace path
gbd_data_2021_path = '/workspaces/Healthcare-Access-and-Outcomes-Analysis-EDA/data/raw/gbd_data_2021.csv'
gbd_data_2024_path = '/workspaces/Healthcare-Access-and-Outcomes-Analysis-EDA/data/raw/gbd_data_2024.csv'
who_health_services_path = '/workspaces/Healthcare-Access-and-Outcomes-Analysis-EDA/data/raw/who_health_services.csv'
world_bank_health_expenditures_path = '/workspaces/Healthcare-Access-and-Outcomes-Analysis-EDA/data/raw/world_bank_health_expenditures.csv'

# Load datasets with error handling
def load_and_display(file_path, name):
    try:
        df = load_csv(file_path)
        print(f"\n{name} loaded successfully.")
        print(f"{name} Data Sample:")
        print(df.head())
        return df
    except Exception as e:
        print(e)
        return None

# Load and display datasets
gbd_data_2021 = load_and_display(gbd_data_2021_path, "GBD Data 2021")
gbd_data_2024 = load_and_display(gbd_data_2024_path, "GBD Data 2024")
who_health_services = load_and_display(who_health_services_path, "WHO Health Services")
world_bank_health_expenditures = load_and_display(world_bank_health_expenditures_path, "World Bank Health Expenditures")


