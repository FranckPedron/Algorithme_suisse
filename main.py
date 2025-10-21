import json
from os import NGROUPS_MAX


def load_players(file_path):
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
    return sorted(joueurs, key=lambda joueur: joueur["elo_points"], reverse=False)


def groups_def(joueurs):
    groups_size = len(joueurs)//2
    s1 = joueurs[:groups_size]
    s2 = joueurs[groups_size:]

    return s1, s2


def show_player(joueur):
    print(f"{joueur['first_name']} - {joueur['last_name']} - {joueur['elo_points']} points")


def show_goups(s1, s2):
    print("Groupe 1:")
    for joueur in s1:
        show_player(joueur)

    print("\nGroupe 2:")
    for joueur in s2:
        show_player(joueur)


def play_game(s1, s2):
    turns = min(len(s1), len(s2))
    matches = []
    print("\nListe des matchs:")
    for i in range(turns):
        matches.append((s1[i], s2[i]))
        print(f"Match {i + 1}: {s1[i]['first_name']} vs {s2[i]['first_name']}")
    with open("./data/matches.json", "w") as file:
        json.dump(matches, file, indent=4)


def game():
    joueurs = load_players("./data/joueurs.json")
    sorted_joueurs = sort_players(joueurs)
    s1, s2 = groups_def(sorted_joueurs)
    show_goups(s1, s2)
    play_game(s1, s2)


game()
