function msgCotainerGenerator(data, counter) {
    let msg = 
    `<div class="d-flex justify-content-start mb-4">
        <div class="img_cont_msg">
            <img src="static/img/profile.jpg" class="rounded-circle user_img_msg">
        </div>
        <div class="msg_cotainer">
    ` + data + 
    `   </div>
    </div>
    <div class="buffer` + counter +
    `
    "></div>
    `
    return msg;
}

function msgCotainerSendGenerator(data, counter) {
    let msg = 
    `<div class="d-flex justify-content-end mb-4">
        <div class="msg_cotainer_send">
            ` + data + `
        </div>
        <div class="img_cont_msg">
            <img src="static/img/myprofile.jpg" class="rounded-circle user_img_msg">
        </div>
    </div>
    <div class="buffer` + counter + 
    `
    "></div>
    `
    return msg;
}

var counter = 1;
var prev_buffer = ".buffer0";

$(document).ready(function(){
	$('#msg').keydown(function(e){
		if(e.keyCode == 13){
            mysend = $('#msg').val();
	    encoded_mysend = window.btoa(unescape(encodeURIComponent(mysend)));
            let postdata = "msg=" + encoded_mysend;
            $.ajax({
                type:'POST',
                data: postdata,
                url:'/bubble/send',
                success : function(data){
                    $(prev_buffer).after(msgCotainerSendGenerator(mysend, counter));
                    prev_buffer = ".buffer" + counter;
                    counter++;
		    if(data) {
                    	$(prev_buffer).after(msgCotainerGenerator(data, counter));
                    	prev_buffer = ".buffer" + counter;
                    	counter++;
		    }
                    document.getElementById("msg").value = "";
                    // $(".msg_cotainer").html(data);
                }
            });
        }
	});
});
