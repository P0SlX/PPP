#!/usr/bin/python3
# ===========
# Les données
# ===========
# Une école d'ingénieur est modélisé par un dictionnaire {etablissement:{ description:'desc', adresse:(rue,ville,code_postal,n°tel),date_limite:date,image:image}}


dico_des_écoles = {
    "Ensimag": {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': ('681 Rue de la Passerelle', 'Saint-Martin-d\'Hères', '38400', '04 76 82 72 33'),
        "date_limite": '10 Octobre 2020',
        'image': "http://ensimag.grenoble-inp.fr/medias/photo/minatec_1485525408991-jpg?ID_FICHE=192861"},

    "Ecole 42": {
        'description': 'Formation de développeurs informatiques',
        'adresse': ('96 Boulevard Bessières', 'Paris', '75017', '01 42 28 12 84'),
        "date_limite": '20 Avril 2020 et 2 Novembre 2020',
        'image': "https://www.42.fr/images/slide01_01.jpg"},

    "Ecole normale supérieure": {
        'description': 'Informatique',
        'adresse': ('15 parvis René Descartes', 'Lyon', '69342', '04 72 72 80 00'),
        "date_limite": '12 Juin et 19 Juillet 2020',
        'image': 'https://img.lemde.fr/2017/03/22/0/0/1280/720/688/0/60/0/20df06e_12583-zpnmhp.yq8l3xflxr.JPG'},

    "Insa Toulouse": {
        'description': 'Informatique et Réseaux',
        'adresse': ('135 Avenue de Rangueil', 'Toulouse', '31400', '05 61 55 95 13'),
        "date_limite": "Avril/Mai 2020",
        'image': 'https://groupe-insa.fr/sites/default/files/uploads/images/photo-8_0.jpg'},

    "ENSEEIHT": {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': ('2 Rue Charles Camichel', 'Toulouse', '31000', '05 34 32 20 00'),
        "date_limite": '23 août au 15 novembre 2020',
        'image': 'https://www.usine-digitale.fr/mediatheque/3/9/2/000225293_homePageUne/enseeiht.jpg'},

    "Centrale Supélec": {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': ('3 Rue Joliot Curie', 'Gif-sur-Yvette', '91190', '01 75 31 60 00'),
        "date_limite": '6 janvier au 13 mars 2020',
        'image': 'https://www.usinenouvelle.com/mediatheque/3/4/2/000576243_image_896x598/parissaclay.jpg'},

    "Université Pierre et Marie Curie": {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': ('4 Place Jussieu', 'Paris', '75005', '01 44 27 44 27'),
        "date_limite": '8 juillet au 30 octobre 2019',
        'image': 'https://i.f1g.fr/media/eidos/805x453_crop/2017/08/15/XVM567ffe32-81b1-11e7-bfab-1cd822713d7e.jpg'},

    "Télécom-Paristech": {
        'description': 'Informatique et réseaux',
        'adresse': ('19 Place Marguerite Perey', 'Palaiseau', '91120 ', '01 45 81 77 77'),
        "date_limite": 'De Décembre à Janvier',
        'image': 'logo-TP.png'},

    "Isima": {
        'description': 'Informatique des systèmes embarqués et Génie logiciel et Systèmes informatiques et Systèmes d’information et Aide à la décision et Modélisation mathématique et Science des données et Réseaux et sécurité informatique',
        'adresse': ('1 Rue de la Chebarde', 'Aubière', '63178', '04 73 40 50 00'),
        "date_limite": '19 juin 2020',
        'image': 'https://www.letudiant.fr/static/uploads/mediatheque/EDU_EDU/7/3/484973-ne-580x310.jpg'},

    "Université Paul Sabatier": {
        'description': 'Informatique et de mathématiques appliquées',
        'adresse': ('Route de Narbonne', 'Toulouse', '31330', '05 61 55 66 11'),
        "date_limite": '8 juillet 2020',
        'image': 'https://static.latribune.fr/full_width/1149541/universite-paul-sabatier.jpg'},

    "Télécom Nancy": {
        'description': 'Big DATA, IoT, Cyber Sécurité, IA, Réalité Virtuelle, Cloud',
        'adresse': ('193 Avenue Paul Muller', 'Villers-lès-Nancy', '54602', '03 72 74 59 00'),
        "date_limite": '15 janvier au 23 avril 2020',
        'image': 'https://telecomnancy.univ-lorraine.fr/sites/telecomnancy.univ-lorraine.fr/files/users/vueciel.jpg'},

    "Epita": {
        'description': 'Système et Réseaux et Développement, Programmation et lot',
        'adresse': ('14-16 Rue Voltaire', 'Le Kremlin-Bicêtre', '94270', '01 44 08 01 01'),
        "date_limite": 'octobre 2020',
        'image': 'https://www.epita.fr/wp-content/uploads/2017/08/epita-ecole-ingenieur-intelligence-informatique-admissions-1024x641.jpg'},

    "Isae - Supaéro": {
        'description': 'Informatique',
        'adresse': ('10 Avenue Edouard Belin', '31055', 'Toulouse', '05 61 33 80 80'),
        "date_limite": '20 Novembre',
        'image': 'https://recrutement.isae-supaero.fr/generated_contents/images/career_wide_picture/9rabP3jZ-isae-supaero-3-0jpg4523043cropped.jpg'},

    "Insa Lyon": {
        'description': 'Informatique, Système et Réseaux, Mathématiques appliquées',
        'adresse': ('20 Avenue Albert Einstein', 'Villeurbanne', '69100', '04 72 43 83 83'),
        "date_limite": '29 mars 2019',
        'image': 'https://i.f1g.fr/media/eidos/805x453_crop/2016/11/10/XVM7a51fc58-e36f-11e9-a1ff-b10277ef3606.jpg'},

    "ENSIIE": {
        'description': 'Informatique',
        'adresse': ('1 Square de la Résistance', 'Évry', '91000', '01 69 36 73 50'),
        "date_limite": '23 août 2020 (Par mail)',
        'image': 'http://static.iquesta.com/logo/iquesta/ENSIIE080914-5714.gif'},

    "Université Paris Sud": {
        'description': 'Informatique',
        'adresse': ('15 Rue Georges Clemenceau', 'Orsay', '91400', '01 69 15 67 50'),
        "date_limite": 'à partir du 9 juillet',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/PCRI_%C3%A0_c%C3%B4t%C3%A9_de_Digiteo.JPG/220px-PCRI_%C3%A0_c%C3%B4t%C3%A9_de_Digiteo.JPG'},

    "Efrei": {
        'description': 'Informatique',
        'adresse': ('30- 32 Avenue de la République', 'Villejuif', '94800', '01 46 77 46 77'),
        "date_limite": 'à partir du 15 mai 2020',
        'image': 'https://www.affiches-parisiennes.com/content/images/2018/11/14/8461/dsc3456-ld.jpg'},

    "Enseirb-Matmeca": {
        'description': 'Calcul intensif et sciences de données, robotique et apprentissage, intelligence artificielle, génie logiciel et cybersécurité',
        'adresse': ('1 Avenue du Dr Albert Schweitzer', 'Talence', '33400 ', '05 56 84 65 00'),
        "date_limite": '5 Juillet au 29 Aout',
        'image': 'https://www.letudiant.fr/static/uploads/mediatheque/EDU_EDU/9/9/1439899-academie-de-bordeaux-580x310.jpg'},

    "Université Claude Bernard": {
        'description': 'Informatique',
        'adresse': ('43 Boulevard du 11 Novembre 1918', 'Villeurbanne', '69100', '04 72 44 80 00'),
        "date_limite": 'à partir du 26 juin',
        'image': 'http://www.annuaire-ecoles-sante-social.adeccomedical.fr/uploads/all_photo/555.jpg'},

    'Polytech Lille': {
        'description': 'Informatique microélectronique automatique et Génie informatique et statistique',
        'adresse': ('Avenue Paul Langevin', 'Lille', '59655', '03 28 76 73 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.geipi-polytech.org/sites/default/files/photos/Polytech_Lille_presentation.JPG'},

    'Polytech Sorbonne': {
        'description': 'Electronique et informatique, Mathématiques appliquées et informatique',
        'adresse': ('4 Place Jussieu', 'Paris', '75005', '01 44 27 73 13'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.polytech.sorbonne-universite.fr/sites/default/files/styles/big_actus/public/2019-09/Amphi%202019.jpg?itok=QMXVNqjl'},

    'Polytech Paris-Sud': {
        'description': 'Electronique et systèmes robotisés, Informatique et Photonique et systèmes optroniques',
        'adresse': ("Bâtiment 620, Maison de l'Ingénieur, Rue Louis de Broglie", 'Orsay', '91190', '01 69 33 86 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Polytech_ParisSud.JPG'},

    'Polytech Nancy': {
        'description': 'Ingénierie de l’Information et des Systèmes et Internet Industriel',
        'adresse': ('2 Rue Jean Lamour', 'Vandœuvre-lès-Nancy', '54519', '03 72 74 69 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://polytech-nancy.univ-lorraine.fr/sites/dev-esstin.univ-lorraine.fr/files/styles/image_slider/public/polytech_nancy_panoramique.jpg?itok=CfN94Kyo'},

    'Polytech Orleans': {
        'description': 'Ingénierie de l’Information et des Systèmes et Internet Industriel',
        'adresse': ('8 Rue Léonard de Vinci', 'Orléans', '45100', '02 38 41 70 50'),
        'date_limite': '27 avril 2020',
        'image': 'http://www.ganex.fr/images/Polytech_Orleans.jpg'},

    'Polytech Tours': {
        'description': 'Informatique, Internet Industriel',
        'adresse': ('64 Avenue Jean Portalis', 'Tours', '37200', '02 47 36 14 14'),
        'date_limite': '27 avril 2020',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Polytech_Tours_Portalis.jpg/1280px-Polytech_Tours_Portalis.jpg'},

    'Polytech Angers': {
        'description': 'Systèmes automatisés et génie informatique',
        'adresse': ('62 Avenue de Notre Dame du Lac', 'Angers', '49000', '02 44 68 75 0 0'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.my-angers.info/wp-content/uploads/2016/06/istia_angers3__076886300_1049_25092014.jpg'},

    'Polytech Nantes': {
        'description': 'Informatique',
        'adresse': ('Rue Christian Pauc', 'Nantes', '44300', '02 40 68 32 00'),
        'date_limite': '27 avril 2020',
        'image': '"https://www.studizz.fr/uploadfile/school_391/391_3bat_WEB.jpg"'},

    'Polytech Lyon': {
        'description': 'Informatique',
        'adresse': ('15 Boulevard André Latarjet', 'Villeurbanne', '69100', '04 26 23 71 42'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.geipi-polytech.org/sites/default/files/photos/Polytech_Lyon_presentation.jpg'},

    'Polytech Clermont-Ferrand': {
        'description': 'Génie mathématique et modélisation',
        'adresse': ('Campus Universitaire des Cézeaux, 2 Avenue Blaise Pascal', 'Aubière', '63100', '04 73 40 75 00'),
        'date_limite': '27 avril 2020',
        'image': '"https://lejournaldeleco.fr/wp-content/uploads/2019/05/Polytech-1-705x470.jpg"'},

    'Polytech Annecy-Chambéry': {
        'description': "Informatique, Données, Usages, Instrumentation - Automatique - Informatique",
        'adresse': ('5 Chemin de Bellevue', 'Annecy', '74940', '04 50 09 66 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.polytech.univ-smb.fr/fileadmin/_processed_/d/3/csm_site_annecy_polytech_6c149cbbbc.jpg'},

    'Polytech Grenoble': {
        'description': 'Informatique et Informatique et Electronique des Systèmes Embarqués',
        'adresse': ('14 Place du Conseil National de la Résistance', "Saint-Martin-d'Hères", '38400', '04 76 82 79 02'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.polytech-grenoble.fr/medias/photo/batiment4_1493736398531-jpg'},

    'Polytech Montpellier': {
        'description': 'Informatique et gestion et Systèmes embarqués',
        'adresse': ('Place Eugène Bataillon', 'Montpellier', '34095', '02 40 68 32 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.geipi-polytech.org/sites/default/files/images/polytech-montpellier-presentation.jpg'},

    'Polytech Nice Sophia': {
        'description': 'Informatique et Informatique par apprentissage',
        'adresse': ('930 Route des Colles', 'Biot', '06410', '04 92 96 50 50'),
        'date_limite': '27 avril 2020',
        'image': 'http://univ-cotedazur.fr/contenus-riches/actualites/fr/mise-a-l2019honneur-de-polytech-nice-sophia-dans-le-classement-l2019etudiant-2018/@@images/3b9c4d89-da9a-4feb-8c63-b1d24e554260.jpeg'},

    'Polytech Marseille': {
        'description': 'Informatique et Génie industriel et informatique',
        'adresse': ("Parc scientifique et technologique de Luminy, 163 Avenue de Luminy", 'Marseille', '13009', '02 40 68 32 00'),
        'date_limite': '27 avril 2020',
        'image': 'https://www.studizz.fr/uploadfile/school_394/394_studizz.png'}

}

def nomDescEcoles(dico):
    res = []
    for (nom, desc)in dico.items():
        for valeurs in desc.items():
           if valeurs[0] == 'description':
               res.append((nom,valeurs[1]))
    return res