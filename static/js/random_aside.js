
var destination = $('aside').attr('address')

$.ajax(
        {
            type: 'GET',
            url: destination,
            dataType: 'text',
            contentType: 'application/json; charset=utf-8',
            success: function (response)
            {
                var results = $.parseJSON(response)

                for(var i in results)
                {
                    var obj = results[i]

                    if(obj['type'] === 'film')
                    {
                        $('aside').append('<div class="suggested_movie">' +
                        '<a href="' + obj['profile'] + '"><img src="' + obj['picture'] + '" ' +
                        'title="' + obj['name'] + '" class="left_img suggested_movie_img"></a>' +
                        '<a href="' + obj['profile'] + '"><h2>' + obj['name'] + '</h2></a>' +
                        '<img src="/static/img/rate_' + obj['rate'] + '.png" %}">' +
                        '<a href="" class="suggested_movie_imdb"><img src="/static/img/IMDB.png"></a>' +
                        '</div><hr>')
                    }

                    else
                    {
                        $('aside').append('<h1> Suggested People </h1>' +
                        '<hr>' +
                        '<div class="suggested_people">' +
                        '<a href="' + obj['profile'] + '" title="' + obj['name'] + '">' +
                        '<img src="' + obj['picture'] + '" class="left_img"></a>' +
                        '<a href="' + obj['profile'] + '"><h2>' + obj['name'] + ' </h2></a>' +
                        '</div>')
                    }
                }
            }
        })
