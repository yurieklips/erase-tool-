import os
import random
import argparse
import sys

def overwrite_file(filepath, passes=3):
    """
    
    """
    try:
        with open(filepath, "r+b") as f:
            length = os.path.getsize(filepath)
            for i in range(passes):
                print(f"Effacement en profondeur: passage {i + 1}/{passes}")
                f.seek(0)
                f.write(bytearray(random.getrandbits(8) for _ in range(length)))
        os.remove(filepath)
        print(f"Fichier {filepath} effacé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'effacement de {filepath}: {str(e)}")

def overwrite_disk(disk_path, passes=3):
    """
   
    """
    try:
        with open(disk_path, 'wb') as disk:
            disk.seek(0)
            for i in range(passes):
                print(f"Effacement en profondeur: passage {i + 1}/{passes}")
                disk.write(os.urandom(1024 * 1024))  
        print(f"Disque {disk_path} effacé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'effacement du disque {disk_path}: {str(e)}")

def parse_arguments():
    """

    """
    parser = argparse.ArgumentParser(description="Effacement sécurisé d'un fichier ou d'un disque dur.")
    parser.add_argument('-f', '--file', type=str, help="Chemin vers le fichier à effacer de manière sécurisée.")
    parser.add_argument('-d', '--disk', type=str, help="Chemin vers le disque dur à effacer de manière sécurisée.")
    parser.add_argument('-p', '--passes', type=int, default=3, help="Nombre de passes d'écrasement (défaut: 3).")
    
    args = parser.parse_args()

    if not args.file and not args.disk:
        print("Erreur: Vous devez spécifier un fichier ou un disque à effacer.")
        parser.print_help()
        sys.exit(1)
    
    return args

def main():
    """
    
    """
    args = parse_arguments()

    if args.file:
        print(f"Effacement sécurisé du fichier: {args.file} avec {args.passes} passes.")
        overwrite_file(args.file, args.passes)
    
    if args.disk:
        print(f"Effacement sécurisé du disque: {args.disk} avec {args.passes} passes.")
        overwrite_disk(args.disk, args.passes)

if __name__ == "__main__":
    main() 
