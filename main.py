import json


def load_players(file_path="joueurs.json"):
    try:
        with open(file_path, "r") as file:
            joueurs = json.load(file)
        return joueurs
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {file_path}.")
        return []
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
        return []


