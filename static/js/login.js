/* The world of Star Wars assignment's login functions 
    by Gabor Koncz */


$('#modal').on('show.bs.modal', function(event){
    $.get("login_modal.html", function(data){
        $('#modal').find('.modal-content').html(data);
    })
})