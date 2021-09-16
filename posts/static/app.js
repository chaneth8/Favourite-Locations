var mylatlng = {lat: 38.3460, lng: -0.4907};
var mapOptions = {
    center: mylatlng,
    zoom: 7, 
    mapTypeId: google.maps.MapTypeId.ROADMAP
}; 

var map = new google.maps.Map(document.getElementById("googleMap"), mapOptions)

var directionsService = new google.maps.DirectionsService();

var directionsDisplay = new google.maps.DirectionsRenderer();

directionsDisplay.setMap(map);

function calcRoute() { 
    //Calculates distance and time it takes to travel between 2 locations. Also renders travel route onto a map.

    var request = {
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,
        travelMode: google.maps.TravelMode.DRIVING, 
        unitSystem: google.maps.UnitSystem.METRIC, 
    }

    directionsService.route(request, (result, status) => {
        if (status == "OK") {
            const output = document.querySelector("#output");
            output.innerHTML = "<div class = 'alert-info'> From: " + document.getElementById("from").value + ". <br/>To: " + document.getElementById("to").value + ". <br/> Driving Distance <i class = 'fas fa-road'></i>" + result.routes[0].legs[0].distance.text + ".</br>Duration <i class = 'fas fa-hourglass-start'></i>:" + result.routes[0].legs[0].duration.text + ". </div>";

            directionsDisplay.setDirections(result);

        } else {
            const output = document.querySelector("#output");
            output.innerHTML = "<div class = 'alert-info'>  There has been an error! </div>"

        }
    });
}

//Adds autocomplete function to form. The form will now fill in the origin and destination, given the user's input

var options = {
    types: ['(cities)']
}

var input1 = document.getElementById("from"); 
var autocomplete1 = new google.maps.places.Autocomplete(input1, options)

var input2 = document.getElementById("to");
var autocomplete2 = new google.maps.places.Autocomplete(input2, options)

