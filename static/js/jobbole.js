$(document).ready(
    $('button').click(function () {
        let page = $('#text').val()
        $.ajax({
            url: '/getshell/page.html',
            data: {
                'page': page
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                let html = ""
                html += '<ol>'
                for (let i = 0; i < data.length; i++) {
                    html += '<li><a href="' + data[i].href + '" target="_blank">' + data[i].title + '</a></li>'
                }
                html += '</ol>'
                $('#title_list').html(html)
            },
            error: function (data, error) {

            }
        });
    })
)