# 🛡️ Secure Erase - Effacement sécurisé de fichiers

## 🚀 Description

**Secure Erase** est un outil de ligne de commande qui permet d'effacer des fichiers ou des répertoires de manière sécurisée. Il remplace les données existantes en les écrasant avec des motifs aléatoires, ce qui rend la récupération des fichiers presque impossible.

Secure Erase is a command-line tool for securely deleting files or directories by overwriting them with random patterns, making file recovery nearly impossible.

---

## ⚙️ Fonctionnalités / Features

- 🗑️ **Effacement sécurisé** de fichiers ou dossiers avec plusieurs passes d'écriture.
- 🔒 **Prévention de la récupération** des données grâce à l'écrasement aléatoire.
- ⚡ **Rapide** et efficace avec une interface simple.

---

## 📥 Installation

1. **Cloner le dépôt** / **Clone the repository** :
   ```bash
   🛠️ Utilisation / Usage
Commande de base / Basic command :
bash
Copier le code
python secure_erase.py -f <chemin_du_fichier> -p <nombre_de_passes>
bash
Copier le code
python secure_erase.py -f <file_path> -p <number_of_passes>
Exemple / Example :
Effacer le fichier fichier_test.txt avec 5 passes d'écriture sécurisée.

bash
Copier le code
python secure_erase.py -f "C:\Users\Eleve\Desktop\fichier_test.txt" -p 5
Delete the file fichier_test.txt with 5 passes of secure overwriting.

bash
Copier le code
python secure_erase.py -f "C:\Users\Eleve\Desktop\fichier_test.txt" -p 5
Options disponibles / Available options :
-f <chemin_du_fichier> / -f <file_path> : Chemin complet du fichier ou dossier à effacer.
-p <nombre_de_passes> / -p <number_of_passes> : Nombre de passes d'écriture pour sécuriser l'effacement (par défaut 3).
📝 Exemple d'utilisation / Usage Example
Effacer un fichier avec 7 passes d'écriture :

bash
Copier le code
python secure_erase.py -f "C:\Users\Eleve\Documents\important.txt" -p 7
Delete a file with 7 overwrite passes:

bash
Copier le code
python secure_erase.py -f "/Users/User/Documents/important.txt" -p 7
🛡️ Sécurité / Security
Ce programme écrase les fichiers en mémoire avec des motifs aléatoires avant de les supprimer. Cela rend la récupération des fichiers via des méthodes classiques très difficile.

This program overwrites files in memory with random patterns before deletion, making file recovery through standard methods very difficult.

🖥️ Compatibilité / Compatibility
🖥️ Windows
🐧 Linux
🍏 macOS
👨‍💻 Contribuer / Contribute
Les contributions sont les bienvenues ! Vous pouvez ouvrir une issue ou soumettre une pull request.

Contributions are welcome! You can open an issue or submit a pull request.
