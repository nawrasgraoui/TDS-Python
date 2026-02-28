donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"), 
 ("Bouchra", "Info", "abc", "G2"), 
 ("", "Math", 10, "G1"), 
 ("Yassine", "Info", 22, "G2"), 
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"), 
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"), 
 ("Hana", "Physique", 15, "G3"), 
 ("Hana", "Math", 8, "G3"),
]

#PARTIE1: VALIDATION

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    
    if nom == "" or matiere == "" or groupe == "":
        return (False, "champ vide")
    
    if not isinstance(note, (int, float)):
        return (False, "note non numerique")
    
    if note < 0 or note > 20:
        return (False, "note hors intervalle")
    
    return (True, "")

valides = []
erreurs = []
doublons_exact = set()
vus = set()

for ligne in donnees:
    if ligne in vus:
        doublons_exact.add(ligne)
    else:
        vus.add(ligne)
    
    ok, raison = valider(ligne)
    
    if ok:
        nom, matiere, note, groupe = ligne
        valides.append((nom, matiere, float(note), groupe))
    else:
        erreurs.append({"ligne": ligne, "raison": raison})

#PARTIE2:STRUCTURATION

matieres = set()

for v in valides:
    matieres.add(v[1])

print("Matieres :", matieres)

etudiants = {}

for nom, matiere, note, groupe in valides:
    if nom not in etudiants:
        etudiants[nom] = {}
    
    if matiere not in etudiants[nom]:
        etudiants[nom][matiere] = []
    
    etudiants[nom][matiere].append(note)

groupes = {}

for nom, matiere, note, groupe in valides:
    if groupe not in groupes:
        groupes[groupe] = set()
    
    groupes[groupe].add(nom)

#PARTIE3: SOMME et MOYENNE

def somme_recursive(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def moyenne(liste):
    if len(liste) == 0:
        return 0
    return somme_recursive(liste) / len(liste)

for nom in etudiants:
    toutes_notes = []
    
    for matiere in etudiants[nom]:
        notes = etudiants[nom][matiere]
        print(nom, "-", matiere, ":", moyenne(notes))
        toutes_notes += notes
    
    print("Moyenne generale de", nom, ":", moyenne(toutes_notes))
    print()

#PARTIE4 : DETECTION D’ANOMALIES

alertes = {
    "doublons_matiere": [],
    "profil_incomplet": [],
    "groupe_faible": [],
    "ecart_eleve": []
}

for nom in etudiants:
    for matiere in etudiants[nom]:
        if len(etudiants[nom][matiere]) > 1:
            alertes["doublons_matiere"].append((nom, matiere))

for nom in etudiants:
    if len(etudiants[nom]) < len(matieres):
        alertes["profil_incomplet"].append(nom)

seuil = 10

for groupe in groupes:
    notes_groupe = []
    
    for nom in groupes[groupe]:
        for matiere in etudiants[nom]:
            notes_groupe += etudiants[nom][matiere]
    
    if moyenne(notes_groupe) < seuil:
        alertes["groupe_faible"].append(groupe)

for nom in etudiants:
    notes = []
    for matiere in etudiants[nom]:
        notes += etudiants[nom][matiere]
    
    if len(notes) > 0:
        if max(notes) - min(notes) > 10:
            alertes["ecart_eleve"].append(nom)
            
print("Valides :", valides)
print("Erreurs :", erreurs)
print("Doublons :", doublons_exact)