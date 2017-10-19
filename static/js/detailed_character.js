$(document).ready(main);

function main() {
    /*var allUrls = getUrls();
    console.log(allUrls);
    for (let i = 0; i < allUrls.length; i++) {
        getCharacterHomeworld(i);
    }*/
    getCharacterHomeworld();
    //getSPeciesName();

}

function getUrls() {
    var homeWorldUrl = $('#homeworldUrl').html();
    var speciesUrl = $('#speciesUrl').html();
    var vehiclesUrl = $('#vehiclesUrl').html();
    var starshipsUrl = $('#starshipsUrl').html();
    var filmsUrl = $('#filmsUrl').html();

    var allUrls = [homeWorldUrl, speciesUrl, vehiclesUrl, starshipsUrl, filmsUrl];
    return allUrls;
}

function getCharacterHomeworld() {
    //var charID = window.location.pathname.split('/').pop();
    var homeWorldUrl = $('#homeworldUrl').html();
    //console.log(homeWorldUrl);
    $.ajax({
            type: 'GET',
            url: homeWorldUrl,
            dataType: 'json',
            success: function(response) {
                replaceHomeworldName(response);
            },
            error: function() {
                alert('Error in network request!');
            } 
        });
}

/*
function getSPeciesName() {
    //var charID = window.location.pathname.split('/').pop();
    var speciesUrl = $('#speciesUrl').html();
    //console.log(homeWorldUrl);
    $.ajax({
            type: 'GET',
            url: speciesUrl,
            dataType: 'json',
            success: function(response) {
                replaceSPeciesNames(response);
            },
            error: function() {
                alert('Error in network request!');
            } 
        });
}
*/

function replaceHomeworldName(response) {
    var homeWorldData = response;
    var homeWorldName = $('#homeworldUrl');
    homeWorldName.html('');
    homeWorldName.append(homeWorldData['name']);
}

/*
function replaceSPeciesNames(response) {
    var speciesData = response['results'];
    var speciesName = $('#speciesUrl');
    speciesName.html('');
    speciesName.append(speciesData['name']);
}
*/

/*function replacecharacterBioUrlName(response) {
    var homeWorldData = response;
    var homeWorldName = $('#homeworldUrl');
    homeWorldName.html('');
    homeWorldName.append(homeWorldData['name']);

    var speciesData = response['results'];
    var speciesName = $('#speciesUrl');
    speciesName.html('');
    speciesName.append(speciesData['name']);

    var vehiclesData = response['results'];
    var vehiclesName = $('#vehiclesUrl');
    vehiclesName.html('');
    vehiclesName.append(vehiclesData['name']);

    var starshipsData = response['results'];
    var starshipsName = $('#starshipsUrl');
    starshipsName.html('');
    starshipsName.append(starshipsData['name']);

    var filmsData = response['results'];
    var filmsName = $('#filmsUrl');
    filmsName.html('');
    filmsName.append(filmsData['name']);

}*/