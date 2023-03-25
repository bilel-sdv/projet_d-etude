import os
import PyPDF2

results=[]

# Fonction pour exécuter la commande Nmap avec l'option de scan choisie
def run_nmap_scan(site, scan_type):
    if scan_type == "1":
        results.append(os.system(f"nmap {site}"))
    elif scan_type == "2":
        results.append(os.system(f"nmap -sV {site}"))
    elif scan_type == "3":
        results.append(os.system(f"nmap -A {site}"))
    elif scan_type == "4":
        results.append(os.system(f"nmap -sS {site}"))
    elif scan_type == "5":
        results.append(os.system(f"nmap -sU {site}"))

# Demander à l'utilisateur de saisir le nom du site à analyser
site = input("Entrez le nom du site à analyser : ")

# Boucle pour permettre à l'utilisateur d'effectuer plusieurs actions
while True:
    # Afficher les options disponibles
    print("Options d'analyse disponibles : ")
    print("1. Footprinting")
    print("2. Reconnaissance")
    print("3. Test d'intrusion")
    print("4. Quitter")

    # Demander à l'utilisateur de saisir une option
    option = input("Choisissez une option : ")

    # Vérifier l'option choisie par l'utilisateur et exécuter les actions correspondantes
    if option == "1":
        results.append(os.system(f"whois {site}"))
        results.append(os.system(f"nslookup {site}"))
        results.append(os.system(f"tracert {site}"))
    elif option == "2":
        results.append(os.system(f"nmap -sS -O {site}"))
        results.append(os.system(f"nikto -h {site}"))
    elif option == "3":
        # Demander à l'utilisateur de choisir un outil de test d'intrusion
        print("Outils de test d'intrusion disponibles : ")
        print("1. Nmap")
        print("2. Metasploit")
        tool = input("Choisissez un outil : ")

        # Vérifier l'outil choisi par l'utilisateur et exécuter les actions correspondantes
        if tool == "1":
            # Demander à l'utilisateur de choisir un type de scan Nmap
            print("Types de scan Nmap disponibles : ")
            print("1. Scan en profondeur")
            print("2. Scan agressif")
            print("3. Scan évasif")
            print("4. Scan SYN")
            print("5. Scan UDP")
            scan_type = input("Choisissez un type de scan : ")
            run_nmap_scan(site, scan_type)
        elif tool == "2":
            results.append(os.system(f"msfconsole -x 'use auxiliary/scanner/http/dir_scanner;set RHOSTS {site};run'"))
        else:
            print("Outil invalide")
    elif option == "4":
        break
    else:
        print("Option invalide")

 # Enregistrer les résultats dans un fichier PDF
if results:
    pdf_file = 'results.pdf'
    with open(pdf_file, 'wb') as file:
        writer = PyPDF2.PdfFileWriter()
        writer.addBlankPage(width=612, height=792)  # Ajouter une nouvelle page
        for result in results:
            writer.addBlankPage(width=612, height=792)  # Ajouter une nouvelle page
            page_num = writer.getNumPages()  # Récupérer le numéro de page
            new_page = PyPDF2.pdf.PageObject.createBlankPage(writer, width=612, height=792)
            new_page.mergePage(PyPDF2.pdf.PageObject.createTextObject(writer, result))
            writer.addPage(new_page)
            writer.addBookmark(str(result), parent=None, pagenum=page_num, color=None, fit='/Fit', bold=False, italic=False)  # Ajouter un signet pour chaque résultat
        writer.addBlankPage(width=612, height=792)  # Ajouter une nouvelle page
        new_page = PyPDF2.pdf.PageObject.createBlankPage(writer, width=612, height=792)
        new_page.mediaBox.upperRight = (612, 792) # Définir la taille de la boîte de médias pour prendre en compte le texte ajouté
        new_page.addText('Les résultats sont prêts', 10, 10) # Ajouter du texte à la page
        writer.addPage(new_page)
        writer.write(file)
    print(f'Les résultats ont été enregistrés dans le fichier {pdf_file}')
else:
    print('Aucun résultat à enregistrer')


print("voici les resultats \n ")
print(results)
