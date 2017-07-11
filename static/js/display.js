/* The world of Star Wars assignment's display functions 
    by Gabor Koncz */


$(document).ready(function(){
    $('.navbar').affix({offset: {top: 312} }); 
    $('.navbar').on('affix.bs.affix', function(){
        $('.navbar').append('<img id="sw_logo_nav" src="/static/images/sw_logo_nav.png" />');
        $('.navbar img').hide().fadeIn(500);
    });

    $('.navbar').on('affix-top.bs.affix', function(){
        $('.navbar img').remove();
    });

    $(window).scroll(function(i){
        $('.jumbotron').css('opacity', 1 - $(window).scrollTop() / 250);
    })

    $('.nav li').on('click', function() {
      $('.nav li').removeClass('active');
      $(this).addClass('active');
    });
});