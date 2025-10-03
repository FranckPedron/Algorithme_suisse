import json


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
    n = len(joueurs)
    s1 = []
    s2 = []
    for i in range(n):
        if i < n / 2:
            s1.append(joueurs[i])
        else:
            s2.append(joueurs[i])

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
    print("\nListe des matchs:")
    for i in range(turns):
        print(f"Match {i + 1}: {s1[i]['first_name']} vs {s2[i]['first_name']}")


def game():
    joueurs = load_players("./joueurs.json")
    sorted_joueurs = sort_players(joueurs)
    s1, s2 = groups_def(sorted_joueurs)
    show_goups(s1, s2)
    play_game(s1, s2)


game()
