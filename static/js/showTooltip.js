$('.tooltip').css('display' , 'none');

$('.tooltip').prev().mouseover(function(){
    console.log('ggg');
    $('.tooltip').css('display' , 'block');
});

$('.tooltip').prev().mouseout(function(){
    $('.tooltip').css('display' , 'none');  
});