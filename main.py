# main.py

from core import inventory_ops, stock_monitor, transaction_ops, reports
from data import inventory_data, transactions
import sys

def afficher_menu():
    print("\n=== Système de Gestion de Stock ===")
    print("1. Lister tous les produits")
    print("2. Ajouter un nouveau produit")
    print("3. Modifier un produit")
    print("4. Supprimer un produit")
    print("5. Rechercher des produits par nom")
    print("6. Trier les produits par un champ")
    print("7. Visualiser les produits en faible stock")
    print("8. Réapprovisionnement automatique")
    print("9. Enregistrer un achat")
    print("10. Enregistrer une vente")
    print("11. Voir l'historique des transactions")
    print("12. Générer un rapport mensuel")
    print("13. Top produits les plus vendus")
    print("14. Produit le plus cher")
    print("15. Prix moyen des produits")
    print("16. Voir les produits par catégorie")
    print("0. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ").strip()

        if choix == '1':
            print("Tous les produits :", inventory_ops.list_all_products())

        elif choix == '2':
            try:
                new_id = int(input("ID du produit : "))
                nom = input("Nom du produit : ")
                prix = float(input("Prix du produit : "))
                quantite = int(input("Quantité : "))
                categorie = input("Catégorie : ")
                inventory_ops.add_product({"id": new_id, "name": nom, "price": prix, "quantity": quantite, "category": categorie})
                print("Produit ajouté.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == '3':
            try:
                pid = int(input("ID du produit à modifier : "))
                print("Laissez vide pour ne pas changer.")
                nom = input("Nouveau nom : ")
                prix_input = input("Nouveau prix : ")
                quantite_input = input("Nouvelle quantité : ")
                categorie = input("Nouvelle catégorie : ")

                nouvelles_donnees = {}
                if nom:
                    nouvelles_donnees['name'] = nom
                if prix_input:
                    nouvelles_donnees['price'] = float(prix_input)
                if quantite_input:
                    nouvelles_donnees['quantity'] = int(quantite_input)
                if categorie:
                    nouvelles_donnees['category'] = categorie

                inventory_ops.update_product(pid, nouvelles_donnees)
                print("Produit modifié.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == '4':
            try:
                pid = int(input("ID du produit à supprimer : "))
                inventory_ops.delete_product(pid)
                print("Produit supprimé.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == '5':
            nom = input("Nom à rechercher : ")
            resultats = inventory_ops.search_product_by_name(nom)
            print("Résultats :", resultats)

        elif choix == '6':
            champ = input("Champ pour trier (id, name, price, quantity, category) : ")
            resultats = inventory_ops.sort_products_by(champ)
            print("Produits triés :", resultats)

        elif choix == '7':
            seuil = int(input("Seuil de stock faible : "))
            produits_baiss = stock_monitor.get_low_stock_products(seuil)
            print("Produits en faible stock :", produits_baiss)

        elif choix == '8':
            min_lvl = int(input("Niveau de stock minimal : "))
            repos_to = int(input("Remplir jusqu'à : "))
            stock_monitor.auto_restock(min_lvl, repos_to)
            print("Réapprovisionnement automatique effectué.")

        elif choix == '9':
            try:
                pid = int(input("ID du produit à acheter : "))
                qte = int(input("Quantité : "))
                cout = float(input("Coût unitaire : "))
                transaction_ops.purchase_product(pid, qte, cout)
                print("Achat enregistré.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == '10':
            try:
                pid = int(input("ID du produit à vendre : "))
                qte = int(input("Quantité : "))
                transaction_ops.sell_product(pid, qte)
                print("Vente enregistrée.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == '11':
            historique = transaction_ops.view_transaction_history()
            print("Historique des transactions :")
            for t in historique:
                print(t)

        elif choix == '12':
            try:
                mois = int(input("Mois (1-12) : "))
                annee = int(input("Année (ex : 2025) : "))
                rapport = reports.generate_monthly_report(mois, annee)
                print("Rapport mensuel :", rapport)
            except ValueError:
                print("Entrée invalide.")

        elif choix == '13':
            try:
                n = int(input("Nombre de produits top : "))
                top_products = reports.get_top_selling_products(n)
                print("Produits les plus vendus :", top_products)
            except ValueError:
                print("Entrée invalide.")

        elif choix == '14':
            produit = reports.get_most_expensive_product()
            print("Produit le plus cher :", produit)

        elif choix == '15':
            prix_moyen = reports.average_product_price()
            print("Prix moyen des produits :", prix_moyen)

        elif choix == '16':
            categorie = input("Nom de la catégorie : ")
            produits_categorie = [p for p in inventory_ops.list_all_products() if p['category'].lower() == categorie.lower()]
            print(f"Produits dans la catégorie '{categorie}':", produits_categorie)

        elif choix == '0':
            print("Au revoir!")
            sys.exit()

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()