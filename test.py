from tqdm import tqdm  # Importez tqdm

# Exemple de deux listes de même taille
liste1 = ["Piste 1", "Piste 2", "Piste 3"]
liste2 = ["Artiste 1", "Artiste 2", "Artiste 3"]

# Créez une barre de chargement avec tqdm
with tqdm(total=len(liste1)) as pbar:
    # Parcourez les deux listes simultanément
    for piste, artiste in zip(liste1, liste2):
        # Traitez les éléments de la liste ici
        # Dans cet exemple, nous simulons un traitement en attente
        import time

        time.sleep(0.5)

        # Mettez à jour la barre de chargement
        pbar.update(1)

# Affichez un message une fois la boucle terminée
print("Boucle terminée !")