$(document).ready(function() {
  $.ajax({
      method: "GET",
      url: "offer"
    })
    .done(function(responseData) {
      if (responseData['status'].trim().toLowerCase() === 'ok') {
        console.log('success');
        //paytmOffers
        if (responseData['paytm'].length > 0) {
          $('#tablePaytm').append('<tr><th>Offer</th><th>Promo Code</th><th>URL</th>');
          $.each(responseData['paytm'], function(i, item) {
            $('#tablePaytm').append('<tr><td>' + item['offerName'] + '</td><td>' + item['offerPromoCode'] + "</td><td><a href='" + item['offerURL'] + "'>" + item['offerURL'] + "</a></td></tr>");
          });
        } else {
          //No data for paytm
          $('#tablePaytm').append('<h4>No Data Found</h4>');
        }
        //redbusOffers
        if (responseData['redbus'].length > 0) {
          $('#tableRedbus').append('<tr><th>Offer</th><th>Info</th><th>Promo Code</th><th>Valid Till</th><th>URL</th>');
          $.each(responseData['redbus'], function(i, item) {
            $('#tableRedbus').append('<tr><td>' + item['offerName'] + '</td><td>' + item['offerInfo'] + '</td><td>' + item['offerPromoCode'] + '</td><td>' + item['offerValidTill'] + "</td><td><a href='" + item['offerURL'] + "'>" + item['offerURL'] + "</a></td></tr>");
          });
        } else {
          //No data for paytm
          $('#tableRedbus').append('<h4>No Data Found</h4>');
        }
      } else {
        console.log('NOT OK:' + responseData);
      }
    })
    .error(function(errorResponseData) {
      console.log('SERVER ERROR:' + JSON.stringify(errorResponseData));
    });
});
