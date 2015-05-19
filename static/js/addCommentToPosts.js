function addComment()
{
    $('.cm_button').bind("click" , function(e) {
        e.preventDefault();
        
        var comment = document.createElement('div');
        
        comment.innerHTML='<a href="" title="Navid Mashayekhi"><img src="img/user.png" \ class="left_img post_cm_img"></img></a> <p>Navid Mashayekhi</p>';
        comment.innerHTML+= ('<p>' + $(this).prev().val() + '</p>');
        
        comment.className='post_comment_div';
        
        $(this).parent().parent().prev().prepend(comment);
        $(this).parent().parent().prev().children().first().after('<hr>');
        $(this).prev().val("")
    });
}

addComment();
