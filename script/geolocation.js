var fromJSON = localStorage.getItem("bdlatlon");
var obj = JSON.parse(fromJSON);

function SwapOrder(){
    function onPositionReceived(position){
        PlusVersMoinsProche(position, listelatlon)
        console.log(position);
        var i = 0;
        for (var i = 0; i < 9; i++) {
            document.getElementsByClassName(varclasse).style.order = i;
        }
    }

    function CalculDistance(position, latlon){ 
        /*
        fonction qui calcul la distance qui sépare deux position.
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

    function PlusVersMoinsProche(position, listelatlon){ 
        /*
        retourne la liste des écoles triés de la plus proche de la position donnée à la moins proche
        parametres :
        resultat : une liste 
        */
        let n = 0;
        var res = []
        for (var i = 0; i < length(listelatlon); i++) {
            res.append(CalculDistance(position, latlon))
            
        }
    }

    function locationNotReceived(positionError){  
        //fonction qui est appelé si la position de l'utilisateur n'a pas pu être récupéré
        console.log(positionError);
    }

    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onPositionReceived, locationNotReceived);
    }
};