from pathlib import Path
import pandas as pd 

from src.profiling import profile_dataframe
DATA_DIR = Path("data/raw/olist")
customers_path = DATA_DIR / "olist_customers_dataset.csv"
customers = pd.read_csv(customers_path)

profile_dataframe(customers, "olist_customers_dataset")
