// Handler of comment SHOW button click event
$(".myCustom_comment_show").click(function () {
    var clockedButtonInformation = $(this).attr("data-bs-target");
    var postID_index = clockedButtonInformation.indexOf("post_");
    var poster_index = clockedButtonInformation.indexOf("_author_");
    var postID = clockedButtonInformation.substring(postID_index + 5, poster_index);
    var poster = clockedButtonInformation.substring(poster_index + 8);

    var clicked = document.getElementById("myCustom_comment_button_clicked_" + postID);
    var authorID = $("#myCustom_comment_button_clicked_" + postID).attr("var");
    var HOSTNAME = $("#like_post_hostname_" + postID).attr("value");

    if (clicked.value.match("false")) {
        clicked.value = "true";

        $.ajax({
            csrfmiddlewaretoken: '{{ csrf_token }}',
            url: "api/author/" + poster + "/posts/" + postID + "/comments",
            type: "GET",
            success: function(data) {
                var count = 0;
                var html = "";

                for (var comment of data.comments) {
                    count += 1;
                    html += "<hr>" + '<div class="">';
                    html += '<input type="hidden" id="myCustom_comment_commenter_' + comment['commentID']+ '" value="' + comment['author'].authorID + '">';
                    html += 'Commented by <a href="profile/' + comment['author'].authorID + '" ';
                    html += 'style="text-decoration: none; font-size: 14pt;">' + comment["author"].displayName + '</a> <br>';
                    html += '<p class="col-sm-12">' + comment["content"] + '</p>';

                    // Button of Comment Like SHOW
                    html += '<button type="button" class="btn btn-primary myCustom_like_comment_show" ';
                    html += 'data-bs-toggle="modal" style="width: 100px;" var="' + authorID + '" ';
                    html += 'data-bs-target="#modal_like_post_' + postID + '_author_' + poster + '_comment_' + comment['commentID'] + '">';
                    html += 'Likes</button>';

                    // View of Post Like SHOW
                    html += '<div class="modal fade" id="modal_like_post_' + postID + '_author_' + poster + '_comment_' + comment['commentID'] + '" ';
                    html += 'style="top: 15%;" aria-labelledby="like_comment_title" aria-hidden="true">';
                    html += '<input type="hidden" id="myCustom_like_comment_button_clicked_' + comment['commentID'] + '" value="false">';
                    html += '<div class="modal-dialog">';
                    html += '<div class="modal-content">';

                    // Header
                    html += '<div class="modal-header">';
                    html += '<h4 id="like_comment_title">Likes of this Comment</h4>';
                    html += '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                    html += '</div>';

                    // Body
                    html += '<div class="modal-body">';
                    html += '<h5 id="like_comment_content_' + comment['commentID'] + '">Click ' + "'Like'" + ' Button to like this comment</h5>';
                    html += '<input type="hidden" id="like_comment_hostname_' + comment['commentID'] + '" ';
                    html += 'value="' + HOSTNAME + '" var="' + poster + '">';
                    html += '<button id="button_like_post_' + postID + '_author_' + authorID + '_comment_' + comment['commentID'] + '" ';
                    html += 'type="button" class="btn btn-outline-success myCustom_button_like_comment_send" style="width: 100px;">Like</button>';

                    html += '<div id="like_comment_' + comment['commentID'] + '"></div>';
                    html += '</div></div></div></div>';

                    html += "</div>";
                }

                if (count == 0) {
                    html = "<br><h4>No one Comment this post so far, T^T</h4>";
                }
                
                $("#comment_" + postID + "_author_" + poster).html(html);
            }
        })
        
    }
    else {
        clicked.value = "false";
        $("#comment_" + postID + "_author_" + poster).empty();
    }
});

// Handler of comment SEND button click event
$("button.myCustom_comment_send").click(function () {
    var postID = $(this).attr("var");
    var clockedButtonInformation = $(this).attr("value");
    var poster_index = clockedButtonInformation.indexOf("_poster_");
    var authorID = clockedButtonInformation.substring(0, poster_index);
    var poster = clockedButtonInformation.substring(poster_index + 8);
    
    var HOSTNAME = $("#like_post_hostname_" + postID).attr("value");

    var content = $("input#comment_input_" + postID).val();

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "api/author/" + authorID + "/posts/" + postID + "/comments",
        type: "POST",
        data: { "content": content, "contentType": "text/plain" },
        success: function(data) {
            document.getElementById("comment_input_" + postID).value = "";
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "api/author/" + poster + "/posts/" + postID + "/comments",
                type: "GET",
                success: function(data) {
                    var html = "";
                    for (var comment of data.comments) {
                        html += "<hr>" + '<div class="">';
                        html += '<input type="hidden" id="myCustom_comment_commenter_' + comment['commentID']+ '" value="' + comment['author'].authorID + '">';
                        html += 'Commented by <a href="profile/' + comment['author'].authorID + '" ';
                        html += 'style="text-decoration: none; font-size: 14pt;">' + comment["author"].displayName + '</a> <br>';
                        html += '<p class="col-sm-12">' + comment["content"] + '</p>';

                        // Button of Comment Like SHOW
                        html += '<button type="button" class="btn btn-primary myCustom_like_comment_show" ';
                        html += 'data-bs-toggle="modal" style="width: 100px; var="' + authorID + '" ';
                        html += 'data-bs-target="#modal_like_post_' + postID + '_author_' + poster + '_comment_' + comment['commentID'] + '">';
                        html += 'Likes</button>';

                        // View of Post Like SHOW
                        html += '<div class="modal fade" id="modal_like_post_' + postID + '_author_' + poster + '_comment_' + comment['commentID'] + '" ';
                        html += 'style="top: 15%;" aria-labelledby="like_comment_title" aria-hidden="true">';
                        html += '<input type="hidden" id="myCustom_like_comment_button_clicked_' + comment['commentID'] + '" value="false">';
                        html += '<div class="modal-dialog">';
                        html += '<div class="modal-content">';

                        // Header
                        html += '<div class="modal-header">';
                        html += '<h4 id="like_comment_title">Likes of this Comment</h4>';
                        html += '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                        html += '</div>';

                        // Body
                        html += '<div class="modal-body">';
                        html += '<h5 id="like_comment_content_' + comment['commentID'] + '">Click ' + "'Like'" + ' Button to like this comment</h5>';
                        html += '<input type="hidden" id="like_comment_hostname_' + comment['commentID'] + '" ';
                        html += 'value="' + HOSTNAME + '" var="' + poster + '">';
                        html += '<button id="button_like_post_' + postID + '_author_' + authorID + '_comment_' + comment['commentID'] + '" ';
                        html += 'type="button" class="btn btn-outline-success myCustom_button_like_comment_send" style="width: 100px;">Like</button>';

                        html += '<div id="like_comment_' + comment['commentID'] + '"></div>';
                        html += '</div></div></div></div>';

                        html += "</div>";
                    }
                    $("#comment_" + postID + "_author_" + poster).html(html);
                }
            })

        }

    })
});
