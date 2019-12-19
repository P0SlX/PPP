BDEcoles = {
    "Polytech Lille": {
        "lat": 50.607736,
        "lon": 3.136850
    },
    "Polytech Paris-Sud": {
        "lat": 48.709228,
        "lon": 2.171136
    },
    "Polytech Nancy": {
        "lat": 48.660120,
        "lon": 6.188261
    },
    "Polytech Orleans": {
        "lat": 47.844203,
        "lon": 1.939034
    },
    "Polytech Tours": {
        "lat": 47.363995,
        "lon": 0.683255
    },
    "Polytech Angers": {
        "lat": 47.480626,
        "lon": -0.592132
    },
    "Polytech Nantes": {
        "lat": 47.281892,
        "lon": -1.515896
    },
    "Polytech Lyon": {
        "lat": 45.779316,
        "lon": 4.868214
    },
    "Polytech Clermont-Ferrand": {
        "lat": 45.760938,
        "lon": 3.109215
    },
    "Polytech Annecy-Chambéry": {
        "lat": 45.919742,
        "lon": 6.157915
    },
    "Polytech Grenoble": {
        "lat": 45.184493,
        "lon": 5.752969
    },
    "Polytech Montpellier": {
        "lat": 43.632789,
        "lon": 43.632789
    },
    "Polytech Nice Sophia": {
        "lat": 43.615614,
        "lon": 7.071725
    },
    "Polytech Marseille": {
        "lat": 43.231976,
        "lon": 5.443125
    },
    "Ensimag": {
        "lat": 45.184638,
        "lon": 5.752744
    },
    "Ecole 42": {
        "lat": 48.896676,
        "lon": 2.318507
    },
    "Ecole normale supérieure": {
        "lat": 48.842233,
        "lon": 2.345181
    },
    "Insa Toulouse": {
        "lat": 43.569683,
        "lon": 1.467740
    },
    "ENSEEIHT": {
        "lat": 43.602101,
        "lon": 1.454398
    },
    "Centrale Supélec": {
        "lat": 48.708809,
        "lon": 2.163995
    },
    "Université Pierre et Marie Curie": {
        "lat": 48.847019,
        "lon": 2.357370
    },
    "Télécom-Paristech": {
        "lat": 48.713106,
        "lon": 2.200591
    },
    "Isima": {
        "lat": 45.759327,
        "lon": 3.111220
    },
    "Université Paul Sabatier": {
        "lat": 43.561984,
        "lon": 1.470043
    },
    "Télécom Nancy": {
        "lat": 48.669147,
        "lon": 6.155318
    },
    "Epita": {
        "lat": 48.797981,
        "lon": 2.357191
    },
    "Isae - Supaéro": {
        "lat": 43.565904,
        "lon": 1.474605
    },
    "Insa Lyon": {
        "lat": 45.783369,
        "lon": 4.878059
    },
    "ENSIIE": {
        "lat": 48.626811,
        "lon": 2.431944
    },
    "Université Paris Sud": {
        "lat": 48.702859,
        "lon": 2.174252
    },
    "Efrei": {
        "lat": 48.788783,
        "lon": 2.363658
    },
    "Enseirb-Matmeca": {
        "lat": 44.806569,
        "lon": -0.605596
    },
    "Université Claude Bernard": {
        "lat": 45.756190,
        "lon": 4.853846
    }
}

/*
for (let ecoles in BDEcoles) {
    let latlon = BDEcoles[ecoles];
    console.log(ecoles);
    console.log(latlon);
}
*/

function SwapOrder(){
    function PositionRecue(position){
        var listetrie = PlusVersMoinsProche(position)
        console.log(position);
        var i = 1;
        for (let ecole in listetrie) {
            document.getElementById(ecole).style.order = i;
            i++;
        }
    }

    function CalculDistance(position, latlon){ 
        /*
        fonction qui calcul la distance qui sépare deux position (Pythagore)
        parametres : deux tuples contenant deux int (les latitudes et longitudes)
        resultat : un float
        */
        let latA = position.coords.latitude
        let lonA = position.coords.longitude
        let latB = latlon.lat
        let lonB = latlon.lon
        let x = (lonB-lonA)*Math.cos((latA+latB)/2)
        let y = latB-latA
        let z = Math.sqrt((Math.pow(x, 2))+(Math.pow(y, 2)))
        let distance = 1.852*60*z
        return distance
    }

    function PlusVersMoinsProche(position){ 
        /*
        retourne la liste des écoles triés de la plus proche de la position donnée à la moins proche
        parametres :
        resultat : une liste 
        */
        var res = []
        for (let ecole in BDEcoles) {
            let latlon = BDEcoles[ecole]
            res[ecole] = CalculDistance(position, latlon)
        }
        resTrie = Object.keys(res).sort(function(a,b){return res[a]-res[b]})
        console.log(resTrie)
        return resTrie
    }

    function PoistionNONRecue(positionError){  
        //fonction qui est appelé si la position de l'utilisateur n'a pas pu être récupéré
        console.log(positionError);
    }

    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(PositionRecue, PoistionNONRecue);
    }
};