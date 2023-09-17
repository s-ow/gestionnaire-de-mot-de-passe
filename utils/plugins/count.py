import json

def countmdps():
    try:
        with open("mdps.txt", "r") as fichier:
            mdps = fichier.read()

        mdps = json.loads(mdps)
    except FileNotFoundError:
        return 0

    return len(mdps)