/**
 * Created by anna on 03.06.16.
 */

    $(document).ready(function() {
        $("button.vote").click(function () {
            var current_button = $(this);
            var a_id = $(this).attr('art_id');
            var d_selector = "i[art_id=" + a_id + "].dislikes";
            var l_selector = "i[art_id=" + a_id + "].likes";
            var dislikes = $(d_selector);
            var likes = $(l_selector);
            var type = $(this).attr('vote')

            $.ajax({
                url: "/articles/" + a_id + "/vote/" + type,
                type: "GET",
                data: {"article": a_id, "vote": type},
                success: function (data) {
                    var info = JSON.parse(data)
                    var new_l = ""+info.likes
                    var new_d = ""+info.dislikes
                    likes.innerText = new_l
                    dislikes.innerText = new_d

                }
            });
        });
      $( "button.like" ).click(function(){
        var current_button = $(this);
        var a_id = $(this).attr('art_id');
        var n_selector = "button[art_id="+a_id+"].dislike";
        var neigbour_button = $(n_selector);

        $.ajax({
            url: "/articles/"+ a_id +"/vote/"+"+",
            type: "GET",
            data: {"article": a_id},
            success: function(data){
              var info = JSON.parse(data)
              var nei = "- "+info.dislikes
              var cur = "+ "+info.likes
              neigbour_button.text(nei)
              current_button.text(cur);
            }
        });
       });
        $( "button.dislike" ).click(function(){
        var current_button = $(this);
        var a_id = $(this).attr('art_id');
        var n_selector = "button[art_id="+a_id+"].like";
        var neigbour_button = $(n_selector);
        $.ajax({
            url: "/articles/"+a_id+"/vote/"+"-",
            type: "GET",
            data: {"article": a_id, },
            success: function(data){
              var info = JSON.parse(data)
              var nei = "+ "+info.likes
              var cur = "- "+info.dislikes
              neigbour_button.text(nei)
              current_button.text(cur);
            }
        });
       });
    });