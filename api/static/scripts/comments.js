// Handler of comment SEND button click event
$("button.myCustom_comment_send").on("click", function () {
    var postID = $(this).attr("var");
    var clockedButtonInformation = $(this).attr("value");
    var poster_index = clockedButtonInformation.indexOf("_poster_");
    var authorID = clockedButtonInformation.substring(0, poster_index);
    var poster = clockedButtonInformation.substring(poster_index + 8);

    var content = $("input#comment_input_" + postID).val();
    //let objects = { "content": content, "contentType": "text/plain" };

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "api/author/" + authorID + "/posts/" + postID + "/comments",
        type: "POST",
        data: { "content": content, "contentType": "text/plain" },
        success: function(data) {
            $("#comment_" + postID + "_author_" + poster).empty();
            document.getElementById("comment_input_" + postID).value = "";
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "api/author/" + poster + "/posts/" + postID + "/comments",
                type: "GET",
                success: function(data) {
                    for (var comment of data) {
                        var html = "";
                        html += "<hr>" + '<div class="">';
                        html += 'Comment by <a href="profile/' + comment['author'] + '" ';
                        html += 'style="text-decoration: none; font-size: 14pt;">' + comment["author"] + '</a> <br>';
                        html += '<p class="col-sm-12">' + comment["content"] + '</p>';
                        html += "</div>";
                        $("#comment_" + postID + "_author_" + poster).append(html);
                    }
                }
            })
        }
    })
});