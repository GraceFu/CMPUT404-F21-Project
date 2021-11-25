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
            }

            if (count == 0) {
                html = "<h5>No one Like this post so far, T^T</h5>";
            }

            $("#like_post_" + postID).html(html);
        }
    })
        
});