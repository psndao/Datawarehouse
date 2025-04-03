# === etl/load_commandes.py ===
import pandas as pd
import sqlalchemy
from datetime import datetime
import os

HISTORIQUE_PATH = "data/historique_chargements.csv"

def enregistrer_historique(source_csv, nb_lignes, mode):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historique = pd.DataFrame([{ 
        "horodatage": now,
        "fichier": os.path.basename(source_csv),
        "nb_lignes": nb_lignes,
        "mode": mode
    }])
    if os.path.exists(HISTORIQUE_PATH):
        historique.to_csv(HISTORIQUE_PATH, mode='a', header=False, index=False)
    else:
        historique.to_csv(HISTORIQUE_PATH, index=False)


def load_commandes_csv(engine, path, mode="replace"):
    """
    Charge les données d'un fichier CSV dans la table 'commandes'.
    mode = "replace" pour recréer la table, "append" pour ajouter sans supprimer.
    """
    df = pd.read_csv(path, encoding='latin1')
    df.to_sql('commandes', engine, if_exists=mode, index=False)
    enregistrer_historique(path, len(df), mode)
    print(f"✅ Données {'ajoutées' if mode == 'append' else 'remplacées'} dans la table 'commandes'")
