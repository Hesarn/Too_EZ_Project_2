function addComment()
{
    $('.commentOnPost').on("submit" , function(e) {

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

addComment();
