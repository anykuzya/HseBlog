/**
 * Created by anna on 03.06.16.
 */

    $(document).ready(function(){
      $( "button.like" ).click(function(){
        var current_button = $(this);
        var a_id = $(this).attr('art_id');
        var n_selector = "button[art_id="+a_id+"].dislike";
        var neigbour_button = $(n_selector);

        $.ajax({
            url: "/articles/"+ a_id +"/like/",
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
            url: "/articles/"+a_id+"/dislike/",
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