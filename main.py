import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from etl.load_commandes import load_commandes_csv

# Charger les variables d’environnement
load_dotenv()
user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

# Connexion à PostgreSQL
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

# Lancer le chargement des données
csv_path = "data/walmart_stock.csv"
load_commandes_csv(engine, csv_path)
