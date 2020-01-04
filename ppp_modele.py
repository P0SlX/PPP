#!/usr/bin/python3
# ===========
# Les données
# ===========
# Une école d'ingénieur est modélisé par un dictionnaire {etablissement:{ description:'desc', adresse:(rue,ville,code_postal,n°tel),date_limite:date,image:image}}

dico_des_écoles = {
    'Ensimag': {
        'description': "Grande école publique d'ingénieurs en informatique et mathématiques appliquées de Grenoble",
        'adresse': '681 Rue de la Passerelle Saint-Martin-d\'Hères 38400',
        'tel': '04 76 82 72 33',
        "date_limite": '10 Octobre 2020',
        'image': "./img/ensimag.jpg",
        'adresse_site': "http://ensimag.grenoble-inp.fr/",
        'nomhtml': 'Ensimag' },

    'Ecole 42': {
        'description': 'Formation de développeurs informatiques',
        'adresse': '96 Boulevard Bessières Paris 75017',
        'tel': '01 42 28 12 84',
        "date_limite": '20 Avril 2020 et 2 Novembre 2020',
        'image': "./img/42.jpg",
        'adresse_site': "https://www.42.fr/",
        'nomhtml': 'Ecole_42' },

    'Ecole normale supérieure': {
        'description': 'Informatique',
        'adresse': '15 parvis René Descartes Lyon 69342',
        'tel': '04 72 72 80 00',
        "date_limite": '12 Juin et 19 Juillet 2020',
        'image': './img/ens.jpg',
        'adresse_site': "http://www.ens.fr/",
        'nomhtml': 'Ecole_normale_supérieure' },

    'Insa Toulouse': {
        'description': 'Informatique et Réseaux',
        'adresse': '135 Avenue de Rangueil Toulouse 31400',
        'tel': '05 61 55 95 13',
        "date_limite": "Avril/Mai 2020",
        'image': './img/insa_toulouse.jpg',
        'adresse_site': "http://www.insa-toulouse.fr/fr/index.html",
        'nomhtml': 'Insa_Toulouse' },

    'ENSEEIHT': {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': '2 Rue Charles Camichel Toulouse 31000',
        'tel': '05 34 32 20 00',
        "date_limite": '23 août au 15 novembre 2020',
        'image': './img/enseeiht.jpg',
        'adresse_site': "http://www.enseeiht.fr/fr/index.html",
        'nomhtml': 'ENSEEIHT' },

    'Centrale Supélec': {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': '3 Rue Joliot Curie Gif-sur-Yvette 91190',
        'tel': '01 75 31 60 00',
        "date_limite": '6 janvier au 13 mars 2020',
        'image': './img/supelec.jpg',
        'adresse_site': "https://www.centralesupelec.fr/",
        'nomhtml': 'Centrale_Supélec' },

    'Université Pierre et Marie Curie': {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': '4 Place Jussieu Paris 75005',
        'tel': '01 44 27 44 27',
        "date_limite": '8 juillet au 30 octobre 2019',
        'image': './img/univ_curie.jpg',
        'adresse_site': "https://www.sorbonne-universite.fr/",
        'nomhtml': 'Université_Pierre_et_Marie_Curie' },

    'Télécom-Paristech': {
        'description': 'Informatique et réseaux',
        'adresse': '19 Place Marguerite Perey Palaiseau 91120',
        'tel': '01 45 81 77 77',
        "date_limite": 'De Décembre à Janvier',
        'image': './img/telecom_paristech.jpeg',
        'adresse_site': "https://www.telecom-paris.fr/",
        'nomhtml': 'Télécom-Paristech' },

    'Isima': {
        'description': 'Informatique des systèmes embarqués et Génie logiciel et Systèmes informatiques et Systèmes d’information et Aide à la décision et Modélisation mathématique et Science des données et Réseaux et sécurité informatique',
        'adresse': '1 Rue de la Chebarde Aubière 63178',
        'tel': '04 73 40 50 00',
        "date_limite": '19 juin 2020',
        'image': './img/isima.jpg',
        'adresse_site': "https://www.isima.fr/",
        'nomhtml': 'Isima' },

    'Université Paul Sabatier': {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': 'Route de Narbonne Toulouse 31330',
        'tel': '05 61 55 66 11',
        "date_limite": '8 juillet 2020',
        'image': './img/univ_paul_sabatier.jpg',
        'adresse_site': "http://www.univ-tlse3.fr/",
        'nomhtml': 'Université_Paul_Sabatier' },

    'Télécom Nancy': {
        'description': 'Big DATA, IoT, Cyber Sécurité, IA, Réalité Virtuelle, Cloud',
        'adresse': '193 Avenue Paul Muller Villers-lès-Nancy 54602',
        'tel': '03 72 74 59 00',
        "date_limite": '15 janvier au 23 avril 2020',
        'image': './img/telecom_nancy.jpg',
        'adresse_site': "https://telecomnancy.univ-lorraine.fr/",
        'nomhtml': 'Télécom_Nancy' },

    'Epita': {
        'description': 'Système et Réseaux et Développement, Programmation et lot',
        'adresse': '14-16 Rue Voltaire Le Kremlin-Bicêtre 94270',
        'tel': '01 44 08 01 01',
        "date_limite": 'octobre 2020',
        'image': './img/epita.jpg',
        'adresse_site': "https://www.epita.fr/",
        'nomhtml': 'Epita' },

    'Isae - Supaéro': {
        'description': 'Informatique',
        'adresse': '10 Avenue Edouard Belin 31055 Toulouse',
        'tel': '05 61 33 80 80',
        "date_limite": '20 Novembre',
        'image': './img/isae_supaero.jpg',
        'adresse_site': "https://www.isae-supaero.fr/fr/",
        'nomhtml': 'Isae_-_Supaéro' },


    'Insa Lyon': {
        'description': 'Informatique, Système et Réseaux, Mathématiques appliquées',
        'adresse': '20 Avenue Albert Einstein Villeurbanne 69100',
        'tel': '04 72 43 83 83',
        "date_limite": '29 mars 2019',
        'image': './img/insa.jpg',
        'adresse_site': "https://www.insa-lyon.fr/",
        'nomhtml': 'Insa_Lyon' },

    'ENSIIE': {
        'description': 'Informatique',
        'adresse': '1 Square de la Résistance Évry 91000',
        'tel': '01 69 36 73 50',
        "date_limite": '23 août 2020 (Par mail)',
        'image': './img/ensiie.gif',
        'adresse_site': "https://www.ensiie.fr/",
        'nomhtml': 'ENSIIE' },

    'Université Paris Sud': {
        'description': 'Informatique',
        'adresse': '15 Rue Georges Clemenceau Orsay 91400',
        'tel': '01 69 15 67 50',
        "date_limite": 'à partir du 9 juillet',
        'image': './img/univ_parissud.jpg',
        'adresse_site': "https://www.u-psud.fr/fr/index.html",
        'nomhtml': 'Université_Paris_Sud' },

    'Efrei': {
        'description': 'Informatique',
        'adresse': '30-32 Avenue de la République Villejuif 94800',
        'tel': '01 46 77 46 77',
        "date_limite": 'à partir du 15 mai 2020',
        'image': './img/efrei.jpg',
        'adresse_site': "https://www.efrei.fr/",
        'nomhtml': 'Efrei' },

    'Enseirb-Matmeca': {
        'description': 'Calcul intensif et sciences de données, robotique et apprentissage, intelligence artificielle, génie logiciel et cybersécurité',
        'adresse': '1 Avenue du Dr Albert Schweitzer Talence 33400',
        'tel': '05 56 84 65 00',
        "date_limite": '5 Juillet au 29 Aout',
        'image': './img/academie_bordeaux.jpg',
        'adresse_site': "https://enseirb-matmeca.bordeaux-inp.fr/fr",
        'nomhtml': 'Enseirb-Matmeca' },

    'Université Claude Bernard': {
        'description': 'Informatique',
        'adresse': '43 Boulevard du 11 Novembre 1918 Villeurbanne 69100',
        'tel': '04 72 44 80 00',
        "date_limite": 'à partir du 26 juin',
        'image': './img/univ_claude_bernard.jpg',
        'adresse_site': "https://www.univ-lyon1.fr/",
        'nomhtml': 'Université_Claude_Bernard' },

    'Polytech Lille': {
        'description': 'Informatique microélectronique automatique et Génie informatique et statistique',
        'adresse': 'Avenue Paul Langevin Lille 59655',
        'tel': '03 28 76 73 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_lille.jpeg',
        'adresse_site': "http://www.polytech-lille.fr/ecole-d-ingenieurs.html",
        'nomhtml': 'Polytech_Lille' },

    'Polytech Sorbonne': {
        'description': 'Electronique et informatique, Mathématiques appliquées et informatique',
        'adresse': '4 Place Jussieu Paris 75005',
        'tel': '01 44 27 73 13',
        'date_limite': '27 avril 2020',
        'image': './img/poly_sorbonne.jpg',
        'adresse_site': "https://www.polytech.sorbonne-universite.fr/",
        'nomhtml': 'Polytech_Sorbonne' },

    'Polytech Paris-Sud': {
        'description': 'Electronique et systèmes robotisés, Informatique et Photonique et systèmes optroniques',
        'adresse': "Bâtiment 620, Maison de l'Ingénieur, Rue Louis de Broglie Orsay 91190",
        'tel': '01 69 33 86 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_parissud.jpeg',
        'adresse_site': "http://www.polytech.u-psud.fr/fr/index.html",
        'nomhtml': 'Polytech_Paris-Sud' },

    'Polytech Nancy': {
        'description': 'Ingénierie de l’Information et des Systèmes et Internet Industriel',
        'adresse': '2 Rue Jean Lamour Vandœuvre-lès-Nancy 54519',
        'tel': '03 72 74 69 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_nancy.jpg',
        'adresse_site': "https://polytech-nancy.univ-lorraine.fr/",
        'nomhtml': 'Polytech_Nancy' },

    'Polytech Orleans': {
        'description': 'Ingénierie de l’Information et des Systèmes et Internet Industriel',
        'adresse': '8 Rue Léonard de Vinci Orléans 45100',
        'tel': '02 38 41 70 50',
        'date_limite': '27 avril 2020',
        'image': './img/poly_orleans.jpg',
        'adresse_site': "http://www.univ-orleans.fr/fr/polytech",
        'nomhtml': 'Polytech_Orleans' },

    'Polytech Tours': {
        'description': 'Informatique, Internet Industriel',
        'adresse': '64 Avenue Jean Portalis Tours 37200',
        'tel': '02 47 36 14 14',
        'date_limite': '27 avril 2020',
        'image': './img/poly_tours.jpg',
        'adresse_site': "https://polytech.univ-tours.fr/",
        'nomhtml': 'Polytech_Tours' },

    'Polytech Angers': {
        'description': 'Systèmes automatisés et génie informatique',
        'adresse': '62 Avenue de Notre Dame du Lac Angers 49000',
        'tel': '02 44 68 75 00 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_angers.jpg',
        'adresse_site': "http://www.polytech-angers.fr/fr/index.html",
        'nomhtml': 'Polytech_Angers' },

    'Polytech Nantes': {
        'description': 'Informatique',
        'adresse': 'Rue Christian Pauc Nantes 44300',
        'tel': '02 40 68 32 00',
        'date_limite': '27 avril 2020',
        'image': "./img/poly_nantes.jpg",
        'adresse_site': "https://polytech.univ-nantes.fr/",
        'nomhtml': 'Polytech_Nantes' },

    'Polytech Lyon': {
        'description': 'Informatique',
        'adresse': '15 Boulevard André Latarjet Villeurbanne 69100',
        'tel': '04 26 23 71 42',
        'date_limite': '27 avril 2020',
        'image': './img/poly_lyon.jpg',
        'adresse_site': "https://polytech.univ-lyon1.fr/",
        'nomhtml': 'Polytech_Lyon' },

    'Polytech Clermont-Ferrand': {
        'description': 'Génie mathématique et modélisation',
        'adresse': 'Campus Universitaire des Cézeaux, 2 Avenue Blaise Pascal Aubière 63100',
        'tel': '04 73 40 75 00',
        'date_limite': '27 avril 2020',
        'image': "./img/poly_clermont.jpg",
        'adresse_site': "http://polytech.univ-bpclermont.fr/",
        'nomhtml': 'Polytech_Clermont-Ferrand' },

    'Polytech Annecy-Chambéry': {
        'description': "Informatique, Données, Usages, Instrumentation - Automatique - Informatique",
        'adresse': '5 Chemin de Bellevue Annecy 74940',
        'tel': '04 50 09 66 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_annecy.jpg',
        'adresse_site': "https://www.polytech.univ-smb.fr/",
        'nomhtml': 'Polytech_Annecy-Chambéry' },

    'Polytech Grenoble': {
        'description': 'Informatique et Informatique et Electronique des Systèmes Embarqués',
        'adresse': "14 Place du Conseil National de la Résistance Saint-Martin-d'Hères 38400",
        'tel': '04 76 82 79 02',
        'date_limite': '27 avril 2020',
        'image': './img/poly_grenoble.jpg',
        'adresse_site': "https://www.polytech-grenoble.fr/",
        'nomhtml': 'Polytech_Grenoble' },

    'Polytech Montpellier': {
        'description': 'Informatique et gestion et Systèmes embarqués',
        'adresse': 'Place Eugène Bataillon Montpellier 34095',
        'tel': '02 40 68 32 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_montpellier.jpg',
        'adresse_site': "https://www.polytech.umontpellier.fr/",
        'nomhtml': 'Polytech_Montpellier' },

    'Polytech Nice Sophia': {
        'description': 'Informatique et Informatique par apprentissage',
        'adresse': '930 Route des Colles Biot 06410',
        'tel': '04 92 96 50 50',
        'date_limite': '27 avril 2020',
        'image': './img/poly_nice.jpeg',
        'adresse_site': "http://www.polytech.unice.fr/",
        'nomhtml': 'Polytech_Nice_Sophia' },

    'Polytech Marseille': {
        'description': 'Informatique et Génie industriel et informatique',
        'adresse': "Parc scientifique et technologique de Luminy, 163 Avenue de Luminy Marseille 13009",
        'tel': '02 40 68 32 00',
        'date_limite': '27 avril 2020',
        'image': './img/poly_marseille.png',
        'adresse_site': "https://polytech.univ-amu.fr/",
        'nomhtml': 'Polytech_Marseille'}

}

dico_des_licences_pro = {
    'Administration et sécurité des systèmes et des réseaux': {
        'ressource': 'http://www.onisep.fr/Ressources/Univers-Formation/Formations/Post-bac/Licence-pro-metiers-de-l-informatique-administration-et-securite-des-systemes-et-des-reseaux'},

    'Applications web': {
        'ressource': 'http://www.onisep.fr/Ressources/Univers-Formation/Formations/Post-bac/Licence-pro-metiers-de-l-informatique-applications-web'},

    'Conception, développement et test de logiciels': {
        'ressource': 'http://www.onisep.fr/Ressources/Univers-Formation/Formations/Post-bac/Licence-pro-metiers-de-l-informatique-conception-developpement-et-test-de-logiciels'},

    'Conduite de projets': {
        'ressource': 'http://www.onisep.fr/Ressources/Univers-Formation/Formations/Post-bac/Licence-pro-metiers-de-l-informatique-conduite-de-projets'},

    'Systèmes d\'information et gestion de données': {
        'ressource': 'http://www.onisep.fr/Ressources/Univers-Formation/Formations/Post-bac/Licence-pro-metiers-de-l-informatique-systemes-d-information-et-gestion-de-donnees'}

}

dico_des_ecoles_info = {
    'management des SI': {
        'ressource': 'https://diplomeo.com/trouver-bachelor-management_des_si'},

    'développement logiciel': {
        'ressource': 'https://diplomeo.com/trouver-bachelor-developpement_logiciel'},

    'domotique': {
        'ressource': 'https://diplomeo.com/trouver-bachelor-domotique'},

    'marketing digital': {
        'ressource': 'https://diplomeo.com/trouver-bachelor-marketing_digital'}

}


def info(dico):
    """
    Cette fonction prend en parametre une base de données (ensemble de dictionnaires)
    et filtre les données afin de les retourner sous forme de liste pour faciliter son intégration dans Jinja
    """
    tempRes = []
    res = []
    for (nom, ensemble) in dico.items():
        for (_, valeur) in ensemble.items():
            tempRes.append(valeur)
        tempRes.append(nom)
        res.append(tempRes)
        tempRes = []
    return res


assert info({'Ensimag': {
    'description': "Grande école publique d'ingénieurs en informatique et mathématiques appliquées de Grenoble",
    'adresse': '681 Rue de la Passerelle Saint-Martin-d\'Hères 38400',
    'tel': '04 76 82 72 33',
    "date_limite": '10 Octobre 2020',
    'image': "http://ensimag.grenoble-inp.fr/medias/photo/minatec_1485525408991-jpg?ID_FICHE=192861",
    'adresse_site': "http://ensimag.grenoble-inp.fr/",
}}
) == [[
    "Grande école publique d'ingénieurs en informatique et mathématiques appliquées de Grenoble",
    "681 Rue de la Passerelle Saint-Martin-d'Hères 38400",
    '04 76 82 72 33',
    '10 Octobre 2020',
    'http://ensimag.grenoble-inp.fr/medias/photo/minatec_1485525408991-jpg?ID_FICHE=192861',
    'http://ensimag.grenoble-inp.fr/',
    'Ensimag']]
