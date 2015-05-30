
function showComments(pk, post)
{
    $.ajax(
    {
        type: 'POST',
        url: '/ajax/comments/' + pk,
        data: JSON.stringify(),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(response)
        {
            //for(var i in response)
            //{
            //    console.log(response[i])
            //}

            for(var i in response)
            {
                comment = response[i].fields;

                $('.post_comments', post).append('<div class="post_comment_div">' +
                '<a href="../profile/' + comment.user[0] +'" title="' + comment.user[1] + '"><img src="' +
                comment.user[2] + '" class="left_img post_cm_img"></a>' +
                '<p><a href="../profile/' + comment.user[0] + '">' + comment.user[1] + '</a></p>'+
                '<p>' + comment.body + '</p>' +
                '</div>' +
                '<hr>');
            }

            $('#numberOfComments', post).text(response.length)

            return response
        }
    })
}

function showPost(response)
{
    var x = document.createElement('div')
    x.className = 'post'
    var user = response.fields.user
    var post = response.fields
    var film = response.fields.film
    showComments(response.pk, x)

    x.innerHTML ='<div class="post_header">' +
    '<a href="../profile' + '/' + user[0] + '"><img src="' + user[2] + '" title="' + user[1] + '" class="left_img"></a>' +
    '<p> <a href="../profile/' + user[0] + '">' + user[1] + '</a> </p>' +
    '<a href="post/' + user[0] + '/' + response.pk + '" class="post_time">' + post.pubDate + '</a>' +
    '</div> <hr>'

    x.innerHTML += '<div class="post_body">' +
    '<a href="" title="' + film[0] + '"><img src="' + film[1] + '" class="right_img"></a>' +
    '<a href="movieProfile/' + film[0] + '" class="inline_block"><h1>' + film[0] + '</h1></a>' +
    '<div class="tooltip" style="display: none;">' +
    '<div class="suggested_movie box-inner">' +
    '<a href=""><img src="' + film[1] + '" title="' + film[0] + '" class="left_img suggested_movie_img"></a>' +
    '<a href=""><h2>' + film[0] + '</h2></a>' +

//{#            <p> Director(s):#}
//{#                {% for cast in post.film.cast_set.all%}#}
//{#                    {% if cast.roleName == 'Director' %}#}
//{#                        {{ cast.name }}#}
//{#                    {% endif %}#}
//{##}
//{#                    {% if not forloop.last %} , {% endif %}#}
//{#                {% endfor %}#}
//{#            </p>#}

    '<img src="/static/img/rate_10.png"><br>' +
    '<a href="" class="suggested_movie_imdb"><img src="/static/img/IMDB.png"></a>' +
    '</div>' +
    '</div>' +
    '<img src="/static/img/rate_10.png" class="rate_img">' +
    '<div class="post_content">' +
    '<p>' +
    post.body +
    '</p>' +
    '</div>' +
    '</div> <hr>' +
    '<div>' +
    '<img src="/static/img/like.png">' +
    '<span>' + post.likeUsers.length + '</span>' +
    '<img src="/static/img/cm2.png">' +
    '<span id="numberOfComments"> </span>' +
    '</div>' +
    '<hr>' +
    '<div class="post_comments">';

    x.innerHTML += '</div>' +
    '<div class="post_incm">' +
    '<a href="" title="' + user[1] + '"><img src="' + user[2] + '" class="left_img"></a>' +
    '<form action="/ajax/commentOnPost/' + response.pk + '" method="post" class="commentOnPost">' +
    '<textarea name="comment" value="" placeholder="Comment" class="cm_input"> </textarea>' +
    '<input type="submit" name="commit" value=" " class="cm_button">' +
    '</form>' +
    '</div>'


    addComment($('.commentOnPost', x))


    $('#postsWrapper').append(x)

    $('.tooltip').prev().mouseover(function(){

        $(this).next().css('display' , 'block');
    });

    $('.tooltip').prev().mouseout(function(){
        $(this).next().css('display' , 'none');
    });
}

$(window).scroll(function()
{
    if($(window).scrollTop() == ($(document).height() - $(window).height()))
    {
        $.ajax(
            {
                type: 'POST',
                url: '/ajax/' + $('#postsWrapper').children().length,
                data: JSON.stringify(),
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                success: function (response) {
                    for (var i in response) {
                        showPost(response[i])
                        //console.log(response[i])

                    }
                }
            })
    }
});




// addCommentToPosts

function addComment(element)
{
    element.on("submit" , function(e) {

        console.log('ezzzz')
        e.preventDefault()

        var destination = $(this).attr('action')
        var commentBody = $('textarea', this).val()
        var cm_wrapper = $(this).parent()

        $.ajax(
            {
                type: 'POST',
                url: destination,
                data: JSON.stringify({comment: commentBody}),
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                    for (var i in response)
                    {
                        var comment = response[i].fields

                        cm_wrapper.prev().prepend('<div class="post_comment_div">' +
                        '<a href="../profile/' + comment.user[0] + '" title="' + comment.user[1] + '">' +
                        '<img src="' + comment.user[2] + '" class="left_img post_cm_img"></a>' +
                        '<a href="../profile/' + comment.user[0] + '"><p>' + comment.user[1] + '</p></a>' +
                        '<p>' + comment.body + '</p>' +
                        '</div>' +
                        '<hr>')

                        $('textarea', cm_wrapper).val('')

                        //$(this).parent().parent().prev().prepend(comment);
                        //$(this).parent().parent().prev().children().first().after('<hr>');
                        //$(this).prev().val("")
                    }
                }
            })
    });
}

