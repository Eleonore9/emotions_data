function GetTracks() {
  $.getJSON('/emotions/music', function(data){
    console.log(data); window.data = data;
    $.each(data.toptags.tag, function(index, element) {
      if(element.name == 'rock'){
	console.log(element.url);
        $('#music').html('<p>' + element.url + '</p>');
        $('#music').html('<embed height="50" width="100" src="http://' + element.url + '">');

      }
    });
  });
};

$(document).ready(function() {
  //$('#music .btn').click(function(e) {
//console.log("click", e);
//e.preventDefault();
   //GetTracks();
  //});
  $('.jumbotron .btn').click(function(){
    $('.jumbotron').append('<p> Are you ready?</p>');
    $('.jumbotron').append('<p><a class="btn btn-lg btn-success" href="/emotions" role="button">Yes</a></p>')
    $('.jumbotron').append('<p><a class="btn btn-lg no" role="button">No</a></p>');
    $('.jumbotron .btn.btn-lg.no').click(function(){
     $('.jumbotron').append('<p>Too bad!</p>');
    });
  });
})

//console.log('load emotions');

