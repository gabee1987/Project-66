$(document).ready(main);

function main() {

}

function getCharacterCards() {
    var charUrl = 'http://swapi.co/api/people/'
    $.ajax({
            type: 'GET',
            url: charUrl,
            dataType: 'json',
            success: function(response) {
                createCharacterCards(response);
                console.log(response);
            },
            error: function() {
                alert('Error in network request!');
            } 
        });


    function createCharacterCards(response) {
        var charactersData = response['results'];
        $('#characters-deck').html('');
        for (let i = 0; i < charactersData.length; i++) {
            var character = charactersData[i];
            $('#characters-deck').append(`
                                        <div class="card" style="width: 20rem;">
                                            <img class="card-img-top" src=" ${imageLink} " alt="Card image cap">
                                            <div class="card-block">
                                                <h4 class="card-title"> ${charactersData['name']} </h4>
                                                <a href="#" class="btn btn-primary">Details</a>
                                            </div>
                                        </div>
                                        `);
        }
    }
}