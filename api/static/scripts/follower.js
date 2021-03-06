// Handler of Following button click event
$("#myCustom_following_button_clicked").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "PUT",
        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
                type: "GET",
                success: function(data) {
                    var count = 0;

                    for (var follow of data) {
                        count += 1;
                    }

                    if (count == 0) {
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                        document.getElementById("myCustom_following_button_id").style.display = 'inline';
                        alert("Following Failed");
                    } else {
                        document.getElementById("myCustom_following_button_id").style.display = 'none';
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';

                        $.ajax({
                            csrfmiddlewaretoken: '{{ csrf_token }}',
                            url: "../api/author/" + authorID + "/followers/" + currentLoginAuthorID,
                            type: "GET",
                            success: function(data) {
                                var count = 0;
                    
                                for (var follow of data) {
                                    count += 1;
                                }
                    
                                if (count == 0) {
                                    document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_wait_friend_button_id").style.display = 'inline';
                                }
                                else {
                                    document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_remove_friend_button_id").style.display = 'inline';
                                }
                            }
                        })
                    }

                    $("#follow_modal").modal('toggle');
                }
            })

        }
    })

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/inbox",
        type: "POST",
        data: {"type": "follow", "follower": authorID},
        success: function(data) {}
    })
});

// Handler of Unfollow button click event
$("#myCustom_unfollow_button_clicked").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "DELETE",
        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
                type: "GET",
                success: function(data) {
                    var count = 0;

                    for (var follow of data) {
                        count += 1;
                    }

                    if (count == 0) {
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                        document.getElementById("myCustom_following_button_id").style.display = 'inline';

                        document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_add_friend_button_id").style.display = 'inline';
                    } else {
                        document.getElementById("myCustom_following_button_id").style.display = 'none';
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';
                        alert("Unfollow Failed");
                    }

                    $("#unfollow_modal").modal('toggle');
                }
            })

        }
    })
});

// Handler of Add Friend button click event
$("#myCustom_friend_add_button_clicked").click(function () {
    var currentLoginAuthorID= $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "PUT",
        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
                type: "GET",
                success: function(data) {
                    var count = 0;

                    for (var follow of data) {
                        count += 1;
                    }

                    if (count == 0) {
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                        document.getElementById("myCustom_following_button_id").style.display = 'inline';
                        alert("Following Failed");
                    } else {
                        document.getElementById("myCustom_following_button_id").style.display = 'none';
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';

                        $.ajax({
                            csrfmiddlewaretoken: '{{ csrf_token }}',
                            url: "../api/author/" + authorID + "/followers/" + currentLoginAuthorID,
                            type: "GET",
                            success: function(data) {
                                var count = 0;
                    
                                for (var follow of data) {
                                    count += 1;
                                }
                    
                                if (count == 0) {
                                    document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_wait_friend_button_id").style.display = 'inline';
                                }
                                else {
                                    document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                                    document.getElementById("myCustom_remove_friend_button_id").style.display = 'inline';
                                }
                            }
                        })
                    }

                    $("#friend_add_modal").modal('toggle');
                }
            })

        }
    })

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/inbox",
        type: "POST",
        data: {"type": "follow", "follower": authorID},
        success: function(data) {}
    })
});

// Handler of Wait Friend button click event
$("#myCustom_friend_wait_button_clicked").click(function () {
    var currentLoginAuthorID= $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "DELETE",
        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
                type: "GET",
                success: function(data) {
                    var count = 0;

                    for (var follow of data) {
                        count += 1;
                    }

                    if (count == 0) {
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                        document.getElementById("myCustom_following_button_id").style.display = 'inline';

                        document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_add_friend_button_id").style.display = 'inline';
                    } else {
                        document.getElementById("myCustom_following_button_id").style.display = 'none';
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';
                        alert("Unfollow Failed");
                    }

                    $("#friend_wait_modal").modal('toggle');
                }
            })

        }
    })
});

// Handler of Remove Friend button click event
$("#myCustom_friend_remove_button_clicked").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "DELETE",
        success: function(data) {
            
            $.ajax({
                csrfmiddlewaretoken: '{{ csrf_token }}',
                url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
                type: "GET",
                success: function(data) {
                    var count = 0;

                    for (var follow of data) {
                        count += 1;
                    }

                    if (count == 0) {
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                        document.getElementById("myCustom_following_button_id").style.display = 'inline';

                        document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                        document.getElementById("myCustom_add_friend_button_id").style.display = 'inline';
                    } else {
                        document.getElementById("myCustom_following_button_id").style.display = 'none';
                        document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';
                        alert("Unfollow Failed");
                    }

                    $("#friend_remove_modal").modal('toggle');
                }
            })

        }
    })
});

// Handler of Followees SHOW button click event
$("#myCustom_followees_button").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followees",
        type: "GET",
        success: function(data) {
            var count = 0;
            var html = "";

            for (var follow of data) {
                count += 1;
                html += '<hr><a href="../profile/' + follow['followee'].authorID + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">' + follow["followee"].displayName + '</a>';
            }

            if (count == 0) {
                html = "<br><h4>His/Her has no followees, T^T</h4><br>";
            }
            else {
                html = html.substring(html.indexOf("<hr>") + 4);
            }
            
            $("#myCustom_followees").html(html);
        }
    })
});

// Handler of Followers SHOW button click event
$("#myCustom_followers_button").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers",
        type: "GET",
        success: function(data) {
            var count = 0;
            var html = "";

            for (var follow of data) {
                count += 1;
                html += '<hr><a href="../profile/' + follow['follower'].authorID + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">' + follow["follower"].displayName + '</a>';
            }

            if (count == 0) {
                html = "<br><h4>His/Her has no followers, T^T</h4><br>";
            }
            else {
                html = html.substring(html.indexOf("<hr>") + 4);
            }
            
            $("#myCustom_followers").html(html);
        }
    })
});

// Handler of Friends SHOW button click event
$("#myCustom_friends_button").click(function () {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/friends",
        type: "GET",
        success: function(data) {
            var count = 0;
            var html = "";

            for (var follow of data) {
                count += 1;
                html += '<hr><a href="../profile/' + follow['follower'].authorID + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">' + follow["follower"].displayName + '</a>';
            }

            if (count == 0) {
                html = "<br><h4>His/Her has no friends, T^T</h4><br>";
            } 
            else {
                html = html.substring(html.indexOf("<hr>") + 4);
            }
            
            $("#myCustom_friends").html(html);
        }
    })
});

// Handler of checking the current Author is following and friending to giving Author
function check_follow_and_friend() {
    var currentLoginAuthorID = $("#myCustom_profile_user_info").attr("value");
    var authorID = $("#myCustom_profile_user_info").attr("var");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + currentLoginAuthorID + "/followers/" + authorID,
        type: "GET",
        success: function(data) {
            var count = 0;

            for (var follow of data) {
                count += 1;
            }

            if (count == 0) {
                document.getElementById("myCustom_unfollow_button_id").style.display = 'none';
                document.getElementById("myCustom_following_button_id").style.display = 'inline';

                document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                document.getElementById("myCustom_add_friend_button_id").style.display = 'inline';
            } else {
                document.getElementById("myCustom_following_button_id").style.display = 'none';
                document.getElementById("myCustom_unfollow_button_id").style.display = 'inline';

                $.ajax({
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    url: "../api/author/" + authorID + "/followers/" + currentLoginAuthorID,
                    type: "GET",
                    success: function(data) {
                        var count = 0;
            
                        for (var follow of data) {
                            count += 1;
                        }
            
                        if (count == 0) {
                            document.getElementById("myCustom_remove_friend_button_id").style.display = 'none';
                            document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                            document.getElementById("myCustom_wait_friend_button_id").style.display = 'inline';
                        }
                        else {
                            document.getElementById("myCustom_add_friend_button_id").style.display = 'none';
                            document.getElementById("myCustom_wait_friend_button_id").style.display = 'none';
                            document.getElementById("myCustom_remove_friend_button_id").style.display = 'inline';
                        }
                    }
                })

            }
        }
    })

}
