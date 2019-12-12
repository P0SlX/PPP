"""
Une école d'ingénieur est modélisé par un dictionnaire {etablissement:{ 'description':(part1,part2,part3),
 'adresse':(rue,ville,code_postal), 'cordonnees':('lat','long'),'date_limite':date}}
"""

{'etablissement':{ 'description':('num','part2','part3'), 
'adresse':('rue','ville','code_postal'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'}}

dico_polytech = {'Polytech Lille':{ 'description':('03 28 76 73 00','Informatique microélectronique automatique','Génie informatique et statistique'), 
'adresse':('Avenue Paul Langevin','Lille','59655'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Sorbonne':{ 'description':('01 44 27 73 13','Mathématiques appliquées et informatique ','Robotique ','Electronique et informatique'),
'adresse':('4 Place Jussieu','Paris','75005'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Paris-Sud':{ 'description':('+33 (0)1 69 33 86 00 ','Electronique et systèmes robotisés ','Informatique','Photonique et systèmes optroniques'), 
'adresse':("Bâtiment 620, Maison de l'Ingénieur, Rue Louis de Broglie",'Orsay','91190'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Nancy':{ 'description':('03 72 74 69 00','Ingénierie de l’Information et des Systèmes','Internet Industriel '), 
'adresse':('2 Rue Jean Lamour','Vandœuvre-lès-Nancy','54519'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Orleans':{ 'description':('02 38 41 70 50','Ingénierie de l’Information et des Systèmes','Internet Industriel '), 
'adresse':('8 Rue Léonard de Vinci','Orléans','45100'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Tours':{ 'description':('02 47 36 14 14','Informatique','Internet Industriel'), 
'adresse':('64 Avenue Jean Portalis','Tours','37200'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Angers':{ 'description':('02 44 68 75 00','Systèmes automatisés et génie informatique','part3'), 
'adresse':('62 Avenue de Notre Dame du Lac','Angers','49000'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Nantes':{ 'description':('02 40 68 32 00','Informatique','part3'), 
'adresse':('Rue Christian Pauc','Nantes','44300'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Lyon':{ 'description':('04 26 23 71 42','Informatique','part3'), 
'adresse':('15 Boulevard André arjet','Villeurbanne','69100'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Clermont-Ferrand':{ 'description':('04 73 40 75 00','Génie mathématique et modélisation','part3'), 
'adresse':('Campus Universitaire des Cézeaux, 2 Avenue Blaise Pascal','Aubière','63100'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Annecy-Chambéry':{ 'description':('04 50 09 66 00',"Informatique, Données, Usages",'Instrumentation - Automatique - Informatique'), 
'adresse':('5 Chemin de Bellevue','Annecy','74940'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Grenoble':{ 'description':('04 76 82 79 02','Informatique','part3'), 
'adresse':('14 Place du Conseil National de la Résistance',"Saint-Martin-d'Hères",'38400'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Montpellier':{ 'description':('02 40 68 32 00','Informatique et gestion','Systèmes embarqués'), 
'adresse':('Place Eugène Bataillon','Montpellier','34095'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Nice Sophia':{ 'description':('04 92 96 50 50','Informatique','Informatique par apprentissage'), 
'adresse':('930 Route des Colles','Biot','06410'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'},

'Polytech Marseille':{ 'description':('02 40 68 32 00','Informatique','Génie industriel et informatique'), 
'adresse':("Parc scientifique et technologique de Luminy, 163 Avenue de Luminy",'Marseille','13009'), 'cordonnees':('lat','long'),'date_limite':'27 avril 2020'}}

def noms(dico):
    res = []
    for etablissement in dico.keys():
        res.append(etablissement)
    return res

def description(dico):
    res = []
    for etablissement in dico.values():
        res.append(etablissement['description'])
    return res

def assemblage(dico):
    res = []
    cpt = 0
    for nom in noms(dico_polytech):
        decri = description(dico_polytech)
        res.append((nom, decri[cpt]))
        cpt += 1
    return res
