from pathlib import Path
import pandas as pd 

from src.profiling import profile_dataframe
from src.data_discovery import check_foreign_key

DATA_DIR = Path("data/raw/olist")


tables = {
    "customers" : "olist_customers_dataset.csv",
    "geolocation" : "olist_geolocation_dataset.csv",
    "orders" : "olist_orders_dataset.csv",
    "order_items" : "olist_order_items_dataset.csv",
    "order_payments" : "olist_order_payments_dataset.csv",
    "order_reviews" : "olist_order_reviews_dataset.csv",
    "products" : "olist_products_dataset.csv",
    "sellers" : "olist_sellers_dataset.csv",
    "translations" : "product_category_name_translation.csv"
    
}

loaded_tables = {}

for table_name, table_file in tables.items():
    filepath = DATA_DIR / table_file
    loaded_tables[table_name] = pd.read_csv(filepath)
    profile_dataframe(loaded_tables[table_name], table_name)


print("\n" + "=" * 50)
print("Foreign Key Validation")
print("=" * 50)

check_foreign_key(
    loaded_tables["orders"],
    "customer_id",
    loaded_tables["customers"],
    "customer_id",
)
