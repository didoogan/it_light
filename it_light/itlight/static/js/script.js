// determine which button was clicked and give it corresponde value 
var buttonpressed;
$('.but').click(function() {
      buttonpressed = $(this).context.innerText;
      if(buttonpressed === 'Codify') {
      	buttonpressed = "True";
      } else {
      	buttonpressed = "False";
      }
      // event.preventDefault();
}); 

// prevent default behavior and pass control to Ajax script
// $('#post-form').on('submit', function(event){
// 	event.preventDefault();
// 	var regex = /^[a-zA-Z\s]+$/;
// 	if (regex.test($('#post-text').val())) {
// 		$('#post-text').attr('placeholder', 'Input text');
// 		$('#chart').attr("hidden", false); 
// 	    create_post();
// 	} else {
// 		$('#post-text').attr("placeholder", "You should input only letters and spaces");
// 		$('#post-text').val('');
// 		$('#result-text').val('');
// 		$('#chart').attr("hidden", true); 
// 	}
// 	// event.preventDefault();
// 	// create_post();
    
// });

$('#post-form').on('submit', myCallBack);

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

$('#post-form').keyup(function() {
	delay(function() {
		myCallBack(event, false);
	}, 1000);
});	

function myCallBack(event, param=true){
	if(param) {
		event.preventDefault();
	}
	// event.preventDefault();
	var regex = /^[a-zA-Z\s]+$/;
	if (regex.test($('#post-text').val())) {
		// $('#post-text').attr('placeholder', 'Input text');
		$('#chart').attr("hidden", false); 
	    create_post();
	} else {
		$('#post-text').attr("placeholder", "You should input only letters and spaces");
		$('#post-text').val('');
		$('#result-text').val('');
		$('#chart').attr("hidden", true); 
	}
	// event.preventDefault();
	// create_post();
    
}

// Ajax handling
function create_post(data) {
	$.ajax({
		url: "/",
		type: "POST",
		data: {
			the_post:   ($("#post-text").val()),
			the_number: $("#id_num").val(),
			codify:     buttonpressed,
		},

		// handle a successful response
		success: function(json) {
			console.log(json);
			// $('#post-text').val('');
			$('#result-text').val(json.result);
			var text = json.suggest;
			$("p").html(text)
			console.log(text);
			var data = json.chart;
			google.charts.setOnLoadCallback(drawChart(data));
			
		} ,

		// handle a non-successful response
		error: function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
			$('#chart').val('');
		}

	});
}


// All code below I have succesfuly copy- paste but I now, that all of this
// about csrf handling
$(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});