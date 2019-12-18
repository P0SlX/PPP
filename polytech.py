"""
Une école d'ingénieur est modélisé par un dictionnaire {etablissement:{ 'description':(part1,part2,part3),
 'adresse':(rue,ville,code_postal), 'coordonees':('lat','long'),'date_limite':date}
"""

{etab:{ 'description':(num,part2,part3), 
'adresse':('rue','ville','code_postal',''), 'coordonees':('lat','long'),'date_limite':'27 avril 2020'}

dico_polytech = {'Polytech Lille':{ 'description':('part1','Informatique microélectronique automatique','Génie informatique et statistique'), 
'adresse':('Avenue Paul Langevin','Lille','59655','03 28 76 73 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
'adresse':('4 Place Jussieu','Paris','75005','01 44 27 73 13'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Paris-Sud':{ 'description':('Electronique et systèmes robotisés ','Informatique','Photonique et systèmes optroniques'), 
'adresse':("Bâtiment 620, Maison de l'Ingénieur, Rue Louis de Broglie",'Orsay','91190','01 69 33 86 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Nancy':{ 'description':('part1','Ingénierie de l’Information et des Systèmes','Internet Industriel'), 
'adresse':('2 Rue Jean Lamour','Vandœuvre-lès-Nancy','54519','03 72 74 69 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Orleans':{ 'description':('02 38 41 70 50','Ingénierie de l’Information et des Systèmes','Internet Industriel'), 
'adresse':('8 Rue Léonard de Vinci','Orléans','45100','02 38 41 70 50'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Tours':{ 'description':('02 47 36 14 14','Informatique','Internet Industriel'), 
'adresse':('64 Avenue Jean Portalis','Tours','37200','02 47 36 14 14'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Angers':{ 'description':('part1','Systèmes automatisés et génie informatique','part3'), 
'adresse':('62 Avenue de Notre Dame du Lac','Angers','49000','02 44 68 75 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Nantes':{ 'description':('Informatique','completer','completer'), 
'adresse':('Rue Christian Pauc','Nantes','44300','02 40 68 32 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Lyon':{ 'description':('04 26 23 71 42','Informatique','part3'),
'adresse':('15 Boulevard André 'Lat'arjet','Villeurbanne','69100','04 26 23 71 42'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Clermont-Ferrand':{ 'description':('Génie mathématique et modélisation','part3'), 
'adresse':('Campus Universitaire des Cézeaux, 2 Avenue Blaise Pascal','Aubière','63100','04 73 40 75 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Annecy-Chambéry':{ 'description':("Informatique, Données, Usages",'Instrumentation - Automatique - Informatique'), 
'adresse':('5 Chemin de Bellevue','Annecy','74940','04 50 09 66 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Grenoble':{ 'description':('Informatique','completer','completer'), 
'adresse':('14 Place du Conseil National de la Résistance',"Saint-Martin-d'Hères",'38400','04 76 82 79 02'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Montpellier':{ 'description':('Informatique et gestion','Systèmes embarqués','part3'), 
'adresse':('Place Eugène Bataillon','Montpellier','34095','02 40 68 32 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Nice Sophia':{ 'description':('completer','Informatique','Informatique par apprentissage'), 
'adresse':('930 Route des Colles','Biot','06410','04 92 96 50 50'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'},
{'Polytech Marseille':{ 'description':('completer','Informatique','Génie industriel et informatique'), 
'adresse':("Parc scientifique et technologique de Luminy, 163 Avenue de Luminy",'Marseille','13009','02 40 68 32 00'), 'coordonees':('lat','long'),'date_limite':'27 avril 2020','image': 'pic'}}


def noms(dico):
    res = []
    for etablissement in dico.keys():
        res.append(etablissement)
    return res

print(noms(dico_polytech))

def description(dico):
    res = []
    for etablissement in dico.values():
        res.append(etablissement['description'])
    return res

print(description(dico_polytech))

def assemblage(dico):
    res = []
    cpt = 0
    for nom in noms(dico_polytech):
        decri = description(dico_polytech)
        res.append((nom, decri[cpt]))
        cpt += 1
    return res

print(assemblage(dico_polytech))