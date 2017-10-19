$(document).ready(main);

function main() {
    getCharacterHomeworld();
}

function getCharacterHomeworld() {
    //var charID = window.location.pathname.split('/').pop();
    var homeWorldUrl = $('#homeworld').html();
    console.log(homeWorldUrl);
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

function replaceHomeworldName(response) {
    console.log(response);
    var homeWorldData = response['results'];
    console.log(homeWorldData);
    var homeWorldName = $('#homeworld');
    homeWorldName.html('');
    homeWorldName.append(homeWorldData[name]);
    console.log(homeWorldData[name]);
}