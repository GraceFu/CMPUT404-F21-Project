// Handler of Followees SHOW button click event
$("#myCustom_followees_button").click(function () {
    var authorID = $("#myCustom_profile_user_info").attr("value");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + authorID + "/followees",
        type: "GET",
        success: function(data) {
            var count = 0;
            var html = "";

            for (var follow of data) {
                count += 1;
                html += '<a href="../profile/' + follow['followee'] + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">' + follow["followeeDisplayName"] + '</a>';
            }

            if (count == 0) {
                html = "<br><h4>His/Her has no followees, T^T</h4><br>";
            }
            
            $("#myCustom_followees").html(html);
        }
    })
});

// Handler of Followers SHOW button click event
$("#myCustom_followers_button").click(function () {
    var authorID = $("#myCustom_profile_user_info").attr("value");

    $.ajax({
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: "../api/author/" + authorID + "/followers",
        type: "GET",
        success: function(data) {
            var count = 0;
            var html = "";

            for (var follow of data) {
                count += 1;
                html += '<a href="../profile/' + follow['follower'] + '" ';
                html += 'style="text-decoration: none; font-size: 14pt;">' + follow["followerDisplayName"] + '</a>';
            }

            if (count == 0) {
                html = "<br><h4>His/Her has no followers, T^T</h4><br>";
            }
            
            $("#myCustom_followers").html(html);
        }
    })
});
