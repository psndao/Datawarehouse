# Installation et Configuration de PostgreSQL sous Windows

Ce guide décrit les étapes d'installation et de configuration de PostgreSQL pour un projet de Data Warehouse sur un système Windows. Il ne couvre **pas** la partie Python.

---

## Prérequis

- Système d'exploitation : Windows 10 ou 11
- Connexion Internet active
- Droits d'administrateur local

---

## 1. Téléchargement de PostgreSQL

1. Aller sur le site officiel : [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
2. Cliquer sur **Download the installer**
3. Choisir la version souhaitée (ex. : PostgreSQL 14 ou 17) et télécharger l’installateur pour Windows 64 bits

---

## 2. Installation de PostgreSQL

1. Lancer l’installateur `.exe` téléchargé
2. Laisser les options par défaut, sauf :
   - **Définir un mot de passe** pour l’utilisateur `postgres` (à conserver)
   - Laisser le port par défaut `5432`
   - Choisir la locale `fr_FR.UTF8` si disponible
3. Terminer l’installation

---

## 3. Désactiver Stack Builder

À la fin de l'installation, une fenêtre `Stack Builder` peut apparaître.  
Vous pouvez **fermer ou annuler** cette étape, sauf si vous avez besoin d'extensions spécifiques.

---

## 4. Ajouter PostgreSQL au PATH

Pour accéder à `psql` depuis le terminal :

1. Ouvrir **Panneau de configuration > Système > Paramètres système avancés**
2. Cliquer sur **Variables d’environnement**
3. Modifier la variable système **Path**
4. Ajouter une nouvelle entrée :


*(adapter selon la version installée)*

5. Valider avec **OK**

6. Redémarrer PowerShell ou CMD

---

## 5. Connexion à PostgreSQL avec `psql`

Ouvrir PowerShell et taper :

```bash
psql -U postgres


CREATE USER papes WITH PASSWORD 'votremotdepasse';
CREATE DATABASE projet OWNER papes;
GRANT ALL PRIVILEGES ON DATABASE projet TO papes;
