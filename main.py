import module_lecture_fichier as read
import module_tri as tris
from random import choice

def frequence_portion():
    """
    fonction permettant d'obtenir les fréquences des premières lettres des mots d'une langue
    renvoie un fichier contenant pour chaque ligne : assemblage_possible    nombre_occurrence   frequence
    """
    suite = 0
    while suite == 0:
        suite = int(input("Combien de lettres souhaite-tu ?"))

    liste_langue = read.lire_fichier("data/langue.txt")
    langue = ""
    while langue not in liste_langue:
        print("langue disponible : ", liste_langue)
        langue = str(input("Quelle langue souhaite-tu utilisé ?"))


    if read.fichier_existe("frequences/%d_lettre_%s.txt" % (suite, langue)):
        print("Fichier existant")
    else:
        mots = read.lire_fichier("data/liste_%s.txt" % langue)
        dico_frequence = {}
        frequence = []

        i = 0
        while i < len(mots):
            if len(mots[i]) < suite:
                morceau = mots[i].lower()
            else:
                morceau = mots[i][:suite].lower()

            if morceau in dico_frequence.keys():
                dico_frequence[morceau] += 1
            else:
                dico_frequence[morceau] = 1
                frequence += [morceau]

            i += 1

        frequence = tris.tri_fusion(frequence)

        texte = ""

        i = 0
        while i < len(frequence):
            morceau = frequence[i]
            texte += '"' + morceau + '"'
            texte += " : \t"
            texte += str(dico_frequence[morceau]) + " occurrences"
            texte += " : \t"
            texte +=str(dico_frequence[morceau] / len(mots))
            texte += "\n"
            i += 1

        read.add_fichier("frequences", "%d_lettre_%s.txt" % (suite, langue), texte)

def frequence_emplacement(debut, fin, langue):
    """
    fonction permettant d'obtenir les fréquences des syllabes présentes dans une portion de mots
    parametres:
        debut, un entier indiquant le début de la section choisit
        fin, un entier indiquant la fin de la section choisit
        langue, une chaine de caracteres indiquant la langue sélectionner
    renvoie un dictionnaire : {assemblage_lettres_possibles : frequence}
    """
    liste_langue = read.lire_fichier("data/langue.txt")
    while langue not in liste_langue:
        print("langue disponible : ", liste_langue)
        langue = str(input("Quelle langue souhaite-tu utilisé ?"))


    mots = read.lire_fichier("data/liste_%s.txt" % langue)
    dico_frequence = {}

    i = 0
    while i < len(mots):
        try:
            morceau = mots[i][debut : fin].lower()
        except:
            morceau = ""

        if morceau in dico_frequence.keys():
            dico_frequence[morceau] += 1
        else:
            dico_frequence[morceau] = 1

        i += 1

    for key, value in dico_frequence.items():
        dico_frequence[key] = (value / len(mots)) * 1000

    return dico_frequence

def mots_imaginaire():
    """
    fonction permettant de créer un mot imaginaire
    /!\ les mots créer peuvent être imprononcable
    """
    suite = 0
    while suite == 0:
        suite = int(input("Combien de lettres compose ce nouveau mot ? "))

    liste_langue = read.lire_fichier("data/langue.txt")
    langue = ""
    while  langue not in liste_langue:
        print("langue disponible : ", liste_langue)
        langue = str(input("Quelle langue souhaite-tu utilisé ? "))

    frequence = []
    for i in range(suite):
        pourcentage = frequence_emplacement(i, i+1, langue)
        portion = []
        for lettre, valeur in pourcentage.items():
            for j in range(int(valeur)):
                portion += [lettre]
        frequence += [portion]

    mot = ""
    for lettre in frequence:
        mot += choice(lettre)

    print("Le nouveau mot généré est : " + mot)


def mots_imaginaire_2():
    """
    fonction permettant de créer des néologismes
    les mots créer sont pronocables et cohérentes
    """
    suite = 0
    while suite == 0:
        suite = int(input("Combien de lettres compose ce nouveau mot ? "))

    liste_langue = read.lire_fichier("data/langue.txt")
    langue = ""
    while  langue not in liste_langue:
        print("langue disponible : ", liste_langue)
        langue = str(input("Quelle langue souhaite-tu utilisé ? "))

    frequence = []
    i = 0
    while i < suite:
        if i+3 < suite:
            pourcentage = frequence_emplacement(i, i+3, langue)
            i += 3
        elif i+2 < suite:
            pourcentage = frequence_emplacement(i, i+2, langue)
            i += 2
        else:
            pourcentage = frequence_emplacement(i, i+1, langue)
            i += 1

        portion = []
        for lettre, valeur in pourcentage.items():
            for j in range(int(valeur)):
                portion += [lettre]
        frequence += [portion]

    mot = ""
    for lettre in frequence:
        mot += choice(lettre)

    print("Le nouveau mot généré est : " + mot)