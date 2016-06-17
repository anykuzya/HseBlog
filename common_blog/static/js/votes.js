/**
 * Created by anna on 03.06.16.
 */

    $(document).ready(function() {
        $("button.vote").click(function () {
            var a_id = $(this).attr('art_id');
            var d_selector = "i[art_id='" + a_id + "'].dislikes";
            var l_selector = "i[art_id='" + a_id + "'].likes";
            var dislikes = $(d_selector);
            var likes = $(l_selector);
            var type = $(this).attr('vote')

            $.ajax({
                url: "/articles/" + a_id + "/vote/" + type,
                type: "GET",
                data: {"article": a_id, "vote": type},
                success: function (data) {
                    var info = JSON.parse(data)
                    var new_l = "" + info.likes
                    var new_d = "" + info.dislikes
                    var voted = info.voted
                    $(likes).text(new_l)
                    $(dislikes).text(new_d)
                }
            });
        });
    });