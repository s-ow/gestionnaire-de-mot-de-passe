# Gestionnaire de mots de passe
J'ai créé ce gestionnaire dans l'objectif de me familiariser avec le module `Tkinter` de python, ainsi que le module `cryptography`.    
> `Tkinter` est assez pratique mais j'ai du mal à rendre l'interface vraiment jolie (sûrement en partie par manque de goût). 

> Grâce à `cryptography`, je pense avoir réussi à créer un système de cryptage **très efficace**, qui pourrait presque poser problème car j'ai
simplement placé la clé de décryptage dans un fichier.    
Cette clé est personnelle est le système est assez difficile à comprendre pour qu'un simple skiddie qui s'amuse à RAT des gens ne puisse
pas le décrypter, mais je dis qu'elle peut poser problème car **en cas de suppression** de celle-ci, ou même **de modification** du fichier,
il sera **impossible de récupérer** tous les mots de passe cryptés à partir de celle-ci.

![image](https://i.imgur.com/2Kp4wRz.png)

## Recommendations
Je vous recommande, si vous décidez d'utiliser ce gestionnaire, d'éviter les actions suivantes :
> Suppression du fichier `key.key` -> Sans celui-ci, impossible de décrypter vos mots de passe.

> Suppression du fichier `mdps.txt` -> Il contient vos mots de passe cryptés, et le programme ne pourra pas les récupérer si celui-ci est supprimé.

### Installation
Comme d'habitude, plusieurs choix s'offrent à vous :
- Pour le premier lancement :
> Utilisez le fichier `install.bat`, qui installera toutes les dépendances et créera le fichier `start.bat`.

- Par la suite :
> Utilisez simplement le fichier `start.bat` pour lancer le programme.

- Si vous perdez les fichiers bat, vous pouvez aussi lancer le programme en utilisant `python main.py` dans votre invite de commandes.