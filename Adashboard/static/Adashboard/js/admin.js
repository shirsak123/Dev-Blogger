$('.left').click(function (){
  $('.left').css('display','none');
  $('.right').css('display','flex');
  $('.scroll').animate({
        scrollLeft: $('.card-overlay').offset().left
    }, 500);
})

$('.right').click(function (){
  $('.right').css('display','none');
  $('.left').css('display','flex');
  $('.scroll').animate({
        scrollLeft: $('.card-details').offset().left
    }, 800);
})