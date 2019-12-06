var listetest = [
    { "Ecole1" : "EX1", "Lat" : "" },
    { "Ecole2" : "EX2",  "Lat" : "" },
    { "Ecole3" : "EX3", "Lat" : "" },
    { "Ecole4" : "EX4", "Lat" : "" }
  ];

function SwapOrder(){
    
    function onPositionReceived(){
        PlusVersMoinsProche(position, listelatlon)
        console.log(position);
        document.getElementById('un').style.order = 4;
        document.getElementById('deux').style.order = 3;
        document.getElementById('trois').style.order = 2;
        document.getElementById('quatre').style.order = 1;
    }

    function CalculDistance(position, latlon){
        let latitudeA = position.coords.latitude
        let longitudeA = position.coords.longitude
        let latitudeB = latlon.latitude
        let longitudeB = latlon.longitude
        let x = (longitudeB-longitudeA)*Math.cos((latitudeA+latitudeB)/2)
        let y = latitudeB-latitudeA
        let z = Math.sqrt((x^2)+(y^2))
        let distance = 1.852*60*z
        return distance
    }

    function PlusVersMoinsProche(position, listelatlon){
        let n = 0;
        var res = []
        for (var i = 0; i < length(listelatlon); i++) {
            res.append(CalculDistance(position, latlon))
        
        }
    }

    function locationNotReceived(positionError){
        console.log(positionError);
    }

    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onPositionReceived, locationNotReceived);
    }
};
