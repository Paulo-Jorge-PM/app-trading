function getMarkets() {
    $.ajax({
    	//dataType: "json",
	    url: '/markets',
	    //data: $('form').serialize(),
	    //type: 'POST',
	    success: function(data){
	        //var json = JSON.parse(data);
		    var json = $.parseJSON(data);
	        


			//var table = "";
			$(json["instruments"]).each(function (key, value) {
			  //$.each(val, function (k, v) {
				  //$.each(v, function (key, value) {
				  //$.each(value, function (k2, v2) {



				    $('#markets').append("<tr><td>" + value['displayName'] + "</td><td>" + value['type'] + "</td></tr>");
				    


				  //});
				  //});
			  //});
			});

				    //table += "<tr><td>teste</td></tr>";

				    				    //$('#markets').append("<tr><td>"+ value[key].type + "</td></tr>");

	    },
	    error: function(error){
		    console.log(error);
	    }
    });
}

