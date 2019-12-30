dico_polytech ={

    'Polytech Lille':{ 
        'description': 'Informatique microélectronique automatique et Génie informatique et statistique', 
        'adresse':('Avenue Paul Langevin','Lille','59655','03 28 76 73 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Sorbonne':{
        'description': 'Electronique et informatique, Mathématiques appliquées et informatique', 
        'adresse':('4 Place Jussieu','Paris','75005','01 44 27 73 13'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Paris-Sud':{ 
        'description': 'Electronique et systèmes robotisés, Informatique et Photonique et systèmes optroniques', 
        'adresse':("Bâtiment 620, Maison de l'Ingénieur, Rue Louis de Broglie",'Orsay','91190','01 69 33 86 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Nancy':{ 
        'description':'Ingénierie de l’Information et des Systèmes et Internet Industriel', 
        'adresse':('2 Rue Jean Lamour','Vandœuvre-lès-Nancy','54519','03 72 74 69 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Orleans':{ 
        'description':'Ingénierie de l’Information et des Systèmes et Internet Industriel', 
        'adresse':('8 Rue Léonard de Vinci','Orléans','45100','02 38 41 70 50'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Tours':{ 
        'description':'Informatique, Internet Industriel', 
        'adresse':('64 Avenue Jean Portalis','Tours','37200','02 47 36 14 14'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Angers':{ 
        'description':'Systèmes automatisés et génie informatique', 
        'adresse':('62 Avenue de Notre Dame du Lac','Angers','49000','02 44 68 75 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Nantes':{ 
        'description':'Informatique', 
        'adresse':('Rue Christian Pauc','Nantes','44300','02 40 68 32 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Lyon':{ 
        'description':'Informatique',
        'adresse':('15 Boulevard André Latarjet','Villeurbanne','69100','04 26 23 71 42'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Clermont-Ferrand':{ 
        'description':'Génie mathématique et modélisation',
        'adresse':('Campus Universitaire des Cézeaux, 2 Avenue Blaise Pascal','Aubière','63100','04 73 40 75 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Annecy-Chambéry':{ 
        'description':'Informatique, Données, Instrumentation, Automatique', 
        'adresse':('5 Chemin de Bellevue','Annecy','74940','04 50 09 66 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Grenoble':{ 
        'description':'Informatique et Informatique et Electronique des Systèmes Embarqués',
        'adresse':('14 Place du Conseil National de la Résistance',"Saint-Martin-d'Hères",'38400','04 76 82 79 02'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Montpellier':{ 
        'description':'Informatique et gestion et Systèmes embarqués',
        'adresse':('Place Eugène Bataillon','Montpellier','34095','02 40 68 32 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Nice Sophia':{ 
        'description':'Informatique et Informatique par apprentissage',
        'adresse':('930 Route des Colles','Biot','06410','04 92 96 50 50'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'},

    'Polytech Marseille':{ 
        'description':'Informatique et Génie industriel et informatique',
        'adresse':("Parc scientifique et technologique de Luminy, 163 Avenue de Luminy",'Marseille','13009','02 40 68 32 00'), 
        'date_limite':'27 avril 2020',
        'image': 'pic'}

}

def nomDescEcoles(dico):
    res = []
    for (nom, desc)in dico.items():
        for valeurs in desc.items():
           if valeurs[0] == 'description':
               res.append((nom,valeurs[1]))
    return res
