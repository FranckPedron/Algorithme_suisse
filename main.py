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


def sort_players(joueurs):
    return sorted(joueurs, key=lambda joueur: joueur["elo_points"], reverse=True)


def groups_def(joueurs):
    n = len(joueurs)
    s1 = []
    s2 = []
    for i in range(n):
        if i < n / 2:
            s1.append(joueurs[i])
        else:
            s2.append(joueurs[i])

    return s1, s2


