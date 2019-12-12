function getMarkets() {
    $.ajax({
	    url: '/assets',
	    success: function(data){
		    //var json = $.parseJSON(data);
	    	var json = JSON.parse(data);

			$(json["instruments"]).each(function (key, value) {
			    $('#markets table').append('<tr id="' + value["name"] + '"><td class="displayName">' + value["displayName"] + '</td><td class="type">' + value["type"] + '</td><td class="buy"></td><td class="sell"></td><td><button class="buyButton" onclick="orderForm(\'buy\', \'' + value["name"] + '\', \'' + value["displayName"] + '\', \'' + value["type"] + '\')">buy</button>&nbsp;&nbsp;<button class="sellButton" onclick="orderForm(\'sell\', \'' + value["name"] + '\', \'' + value["displayName"] + '\', \'' + value["type"] + '\')">sell</button>&nbsp;&nbsp;<button class="followButton" onclick="follow(\'none\', \'' + value["name"] + '\', \'' + value["displayName"] + '\', \'' + value["type"] + '\')">follow</button></td></tr>');
			});
			prices();
	    },
	    error: function(error){
		    console.log(error);
	    }
    });
}

function getPrices(instruments, paint=false) {
    $.ajax({
	    url: '/prices?instruments='+instruments,
	    success: function(data){
		    //var json = $.parseJSON(data);
		    var json = JSON.parse(data);

			$(json["prices"]).each(function (key, value) {
				td_buy = $('#markets table tr#'+value["instrument"]+' td.buy');
				td_sell = $('#markets table tr#'+value["instrument"]+' td.sell');

				//limpa todas as classes
				td_buy.removeClass('up down');
				td_sell.removeClass('up down');

				var buy = value['asks'][0]['price'];
				var sell = value['bids'][0]['price'];
				var old_buy = td_buy.text();
				var old_sell = td_sell.text();

				td_buy.text(buy);
				td_sell.text(sell);

				//exibe cor red ou green conforme sobe ou desce
				//Only if true porque na 1ª call não queremos porqu está vazio
				if(paint==true){
					if(buy>old_buy){
						td_buy.addClass('up');
					}
					else if (buy<old_buy){
						td_buy.addClass('down');
					}

					if(sell>old_sell){
						td_sell.addClass('up');
					}
					else if (sell<old_sell){
						td_sell.addClass('down');
					}
				}
			});
	    },
	    error: function(error){
		    console.log(error);
	    }
    });
}

function closeAsset(idAsset) {
  $.get('/close?idasset='+idAsset,
  function(data, status){
  });
}

function follow(ordertype, instrument, displayName, marketType) {

/* $.get('/follow?instrument='+instrument+'&name='+displayName+'&market='+marketType,
  function(data, status){
  	alert("Adicionado aos seguidos! Pode consultar no menu Fllowed.");
  });
}*/


$.ajax({
	    url: '/follow?instrument='+instrument+'&name='+displayName+'&market='+marketType,
	    success: function(data){
	    	alert("Adicionado aos seguidos! Pode consultar no menu Fllowed.");
	    },
	    error: function(error){
		    console.log(error);
	    }
    });
}