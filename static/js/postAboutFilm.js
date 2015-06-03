console.log('gg')

$('#postFilm').on('click', function(e){
    e.preventDefault()
    var form = $('<form></form>')
    var rate = $('<input name="rate" type="hidden">')
    var body = $('<textarea name="postBody"></textarea>')

    rate.attr('value', $('#rating').attr('rate'))
    form.append(rate)

    body.val($('.popup_div textarea').val())
    form.append(body)

    form.attr('action', $('.popup').attr('formAction'))
    form.attr('method', 'post')

    console.log(rate.attr('value'))
    form.submit()
})