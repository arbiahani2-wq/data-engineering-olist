from pathlib import Path
import pandas as pd 

from src.profiling import profile_dataframe

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

for table_name, table_file in tables.items():
    filepath = DATA_DIR / table_file
    df = pd.read_csv(filepath)
    profile_dataframe(df, table_name)
