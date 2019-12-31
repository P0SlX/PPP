const BDEcoles = {
    "Polytech Lille": {
        "lat": 50.607736,
        "lon": 3.136850
    },
    "Polytech Sorbonne": {
        "lat": 48.845216,
        "lon": 2.357145
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
        "lon": 3.862606
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
        "lat": 48.788769,
        "lon": 2.363711
    },
    "Enseirb-Matmeca": {
        "lat": 44.806569,
        "lon": -0.605596
    },
    "Université Claude Bernard": {
        "lat": 45.756190,
        "lon": 4.853846
    }
};

function SwapOrder() {
    /**
    Modifie la disposition des cards de l'index en fonction de la geolocalisation de l'utilisateur.
    Cette fonction ne prends aucun parametre car la geolocalisation ainsi que la liste des posistions des écoles sont récupérées en interne de cette fonction.
    */
    function PositionNONRecue(positionError) {
        /**
        Cette fonction est appelée si la position de l'utilisateur n'a pas pu être récupéré (soit l'utilisateur à refuser l'autorisation de la geolocalisation
        soit le navigateur ne prends pas en charge cette fonctionnalitée).
        paramètre : un message d'erreur ex : GeolocationPositionError {code: 1, message: "User denied Geolocation"}
        */
        if (positionError.message = "User denied Geolocation") {
            alert('Veuillez autoriser la géolocalisation afin de trier les écoles.');
        }
        else {
            alert('Erreur, nous n\'avons pas pu récuper votre position. \nVotre navigateur ne supporte peut-être pas cette fonctionnalité.');
        }
    }

    function PositionRecue(position) {
        /**
        L'utilité de cette fpnction est d'ordonner les cards du html en fonction d'une liste.
        paramètre : un objet contenant toutes les informations sur la localisation de l'utilisateur (latitude, longitude, altitude...).
        */
        let listetrie = PlusVersMoinsProche(position); //appel de la fonction qui trie les écoles puis définition d'une variable contenant le résultat de la fonction.
        let i = 1;
        listetrie.forEach(function (ecole) {
            document.getElementById(ecole.nom).style.order = i;
            document.getElementById(ecole.nom).getElementsByClassName("distance")[0].textContent = ecole.distance + " km";
            i++;
        });
    }

    function CalculDistance(position, position_ecole) {
        /**
        Fonction qui calcule la distance (à vol d'oiseau) qui sépare deux position (avec le théorème de Pythagore). Source : http://villemin.gerard.free.fr/aGeograp/Distance.htm#haver
        parametres : deux objets contenant la latitude et la longitude (float), position est la position de l'utilisateur et position_ecole est la position de l'école.
        résultat : un float répresentant la distance en kilomètres qui sépare l'utilisateur de l'école.
        */
        let latA = position.coords.latitude;
        let lonA = position.coords.longitude;
        let latB = position_ecole.lat;
        let lonB = position_ecole.lon;
        let todegree = ((latA + latB) / 2) * (Math.PI / 180);
        let x = (lonB - lonA) * Math.cos(todegree);
        let y = latB - latA;
        let z = Math.sqrt((Math.pow(x, 2)) + (Math.pow(y, 2)));
        let distance = 1.852 * 60 * z;
        return distance.toPrecision(5);
    }

    function PlusVersMoinsProche(position) {
        /**
        Retourne la liste des écoles triés de la plus proche de la position donnée à la moins proche.
        paramètre : un objet contenant toutes les informations sur la localisation de l'utilisateur (latitude, longitude, altitude...).
        resultat : une liste d'écoles (str)
        */
        let ListeEcoleDistances = [];
        for (let ecole in BDEcoles) {
            let position_ecole = BDEcoles[ecole]; //la variable position_ecole prend la valeur de la clé correspondant au nom de l'école (un objet contenant la latitude et la longitude ex : {"lat": 47.363995, "lon": 0.683255})
            ListeEcoleDistances.push({ "nom": ecole, "distance": CalculDistance(position, position_ecole) });
        }
        ListeEcoleDistances.sort(function (a, b) {
            return a.distance - b.distance;
        });
        return ListeEcoleDistances;
    }

    const checkBox = document.getElementById('location-button');
    if (checkBox.checked) {
        if (navigator.geolocation) { //si le navigateur prends en charge la géolocalisation
            navigator.geolocation.getCurrentPosition(PositionRecue, PositionNONRecue);
        }
    }
    else {
        for (let ecole in BDEcoles) {
            document.getElementById(ecole).style.order = 0;
        }
    }
};