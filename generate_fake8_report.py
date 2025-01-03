#!/usr/bin/env python3
import subprocess
import os


def generate_flake8_report():
    """Génère un rapport HTML à partir de l'analyse Flake8."""
    try:
        # Définir le répertoire de sortie pour le rapport HTML
        output_dir = "flake8_report"

        # Créer le répertoire si nécessaire
        os.makedirs(output_dir, exist_ok=True)

        # Exécuter flake8 avec le format HTML et le répertoire de sortie
        result = subprocess.run(
            ["flake8", "--format=html", f"--htmldir={output_dir}"],
            text=True,
            capture_output=True,
        )

        # Vérifier si des problèmes ont été détectés
        if result.returncode == 0:
            print(f"no Prbl. Rapport : {os.path.abspath(output_dir)}")
        else:
            print(f"Rapport généré dans : {os.path.abspath(output_dir)}")
            print("Consultez index.html dans ce répertoire pour les détails.")

    except FileNotFoundError:
        print("Erreur : Flake8 ou flake8-html not install.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


if __name__ == "__main__":
    generate_flake8_report()
