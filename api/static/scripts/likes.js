// Handler of Like Post SHOW button click event
$(".myCustom_like_post_show").on("click", function () {
    var clockedButtonInformation = $(this).attr("data-bs-target");
    var postID_index = clockedButtonInformation.indexOf("post_");
    var poster_index = clockedButtonInformation.indexOf("_author_");
    var postID = clockedButtonInformation.substring(postID_index + 5, poster_index);
    var poster = clockedButtonInformation.substring(poster_index + 8);

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "api/author/" + poster + "/posts/" + postID + "/likes",
        type: "GET",

        success: function(data) {
            var count = 0;
            var html = "";

            for (var like of data) {
                count += 1;
                html += "<hr>" + '<div class="">';
                html += '<a href="profile/' + like['author'] + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">';
                html += like['summary'].substring(0, like['summary'].indexOf(" Like"));
                html += "</a> Liked this Post</div>";
            }

            if (count == 0) {
                html = "<hr><h5>No one Like this post so far, T^T</h5>";
            }

            $("#like_post_" + postID).html(html);
        }
    })
        
});

// Handler of like Post SEND button click event
$(".myCustom_button_like_post_send").on("click", function () {
    var clockedButtonInformation = $(this).attr("id");
    var postID_index = clockedButtonInformation.indexOf("post_");
    var authorID_index = clockedButtonInformation.indexOf("_author_");
    var postID = clockedButtonInformation.substring(postID_index + 5, authorID_index);
    var authorID = clockedButtonInformation.substring(authorID_index + 8);

    var HOSTNAME = $("#like_post_hostname_" + postID).attr("value");
    var poster = $("#like_post_hostname_" + postID).attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "api/author/" + authorID + "/inbox/",
        type: "POST",
        data: { "summary": authorID + " Likes your post", "object": HOSTNAME + '/author/' + poster + '/posts/' + postID },

        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "api/author/" + poster + "/posts/" + postID + "/likes",
                type: "GET",

                success: function(data) {
                    var html = "";

                    for (var like of data) {
                        html += "<hr>" + '<div class="">';
                        html += '<a href="profile/' + like['author'] + '" ';
                        html += 'style="text-decoration: none; font-size: 14pt;">';
                        html += like['summary'].substring(0, like['summary'].indexOf(" Like"));
                        html += "</a> Liked this Post</div>";
                    }

                    $("#like_post_" + postID).html(html);
                }
            })

        }

    })
});
