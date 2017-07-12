$(document).ready(main);

function main() {
    getCharacterCards();
    $('#btn-next').on('click', function() {
        var nextPage = $(this).data('next');
        $.get(nextPage, function(result) {
            var newData = result;
            changeCharacterData(newData);
            updatePageButtons(newData);
        });
    });
    $('#btn-prev').on('click', function() {
        var prevPage = $(this).data('previous');
        $.get(prevPage, function(result) {
            var newData = result;
            changeCharacterData(newData);
            updatePageButtons(newData);
        })
    });

}

function getCharacterCards() {
    var charUrl = 'http://swapi.co/api/people/'
    $.ajax({
            type: 'GET',
            url: charUrl,
            dataType: 'json',
            success: function(response) {
                createCharacterCards(response);
            },
            error: function() {
                alert('Error in network request!');
            } 
        });


    function createCharacterCards(response) {
        var charactersData = response['results'];
        console.log(charactersData);
        $('#characters-deck').html('');
        for (let i = 0; i < charactersData.length; i++) {
            var character = charactersData[i];
            var pictureId = character['url'].replace ( /[^\d]/g, '' );
            $('#characters-deck').append(`
                                        <div class="card col-6 col-sm-3" style="background-image: url('https://starwars-visualguide.com/assets/img/characters/${pictureId}.jpg');">
                                            <div class="card-block">
                                                <h4 class="card-title"> ${charactersData[i]['name']} </h4>
                                                <a href="#" class="btn btn-primary">Details</a>
                                            </div>
                                        </div>
                                        `);
        }
    }
}

function changeCharacterData(newData) {
    var charactersData = newData['results'];
    $('#characters-deck').html('');
    for (let i = 0; i < charactersData.length; i++) {
            var character = charactersData[i];
            var pictureId = character['url'].replace ( /[^\d]/g, '' );
            $('#characters-deck').append(`
                                        <div class="card col-6 col-sm-3" style="background-image: url('https://starwars-visualguide.com/assets/img/characters/${pictureId}.jpg');">
                                            <div class="card-block">
                                                <h4 class="card-title"> ${charactersData[i]['name']} </h4>
                                                <a href="#" class="btn btn-primary">Details</a>
                                            </div>
                                        </div>
                                        `);
        }
}

function updatePageButtons(newData) {
    $('#btn-next').data('next', newData['next']);
    $('#btn-prev').data('previous', newData['previous']);
    if (!newData['next'] && !$('#btn-next').attr('disabled')) {
        $('#btn-next').attr('disabled', 'disabled');
    }
    if ($('#btn-next').attr('disabled') && newData['next']) {
        $('#btn-next').removeAttr('disabled');
    }
    if (!newData['previous'] && !$('#btn-prev').attr('disabled')) {
        $('#btn-prev').attr('disabled', 'disabled');
    }
    if ($('#btn-prev').attr('disabled') && newData['previous']) {
        $('#btn-prev').removeAttr('disabled');
    }
}