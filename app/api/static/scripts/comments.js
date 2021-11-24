$("button.myCustom_comment_send").on("click", function () {
    let postID = $(this).attr("var");
    let authorID = $(this).attr("value");

    let content = $("input#comment_input_" + postID).val();
    var objects = { "content": content, "contentType": "text/plain" };
    alert(JSON.stringify(objects));

    var request = new XMLHttpRequest();

    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            try {
                if (request.status === 200) {
                }
            }
            catch (e) {
                alert('Error: ' + e.name);
            }
        }
    }

    request.open('POST', 'api/author/' + authorID + '/posts/' + postID + '/comments');
    request.send(JSON.stringify(objects));
});