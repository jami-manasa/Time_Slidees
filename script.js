$(function() {
  $('#slider-range').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [2.45,22.15]
  });
  $('.ui-slider-range').append($('.range-wrapper'));
  $('.range').html('<span class="range-value"><sup></sup>' + $('#slider-range').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value"><sup></sup>' + $("#slider-range").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range').html('<span class="range-value"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));

      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert').hasClass('active')) {
          $('.range-alert').addClass('active');
        }
      } else {
        if ($('.range-alert').hasClass('active')) {
          $('.range-alert').removeClass('active');
        }
      }
    }
  });
  $('.range, .range-alert').on('mousedown', function(event) {
    event.stopPropagation();
  });
  $('#slider-range1').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [6.45,15.15]
  });
  $('.ui-slider-range1').append($('.range-wrapper1'));
  $('.range1').html('<span class="range-value1"><sup></sup>' + $('#slider-range1').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider1"></span><span class="range-value1"><sup></sup>' + $("#slider-range1").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range1').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
      console.log(res);
      console.log(ui.value);
    console.log("--->",ui.values);
      console.log(r);

     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range1').html('<span class="range-value1"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider1"></span><span class="range-value1"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));
      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert1').hasClass('active1')) {
          $('.range-alert1').addClass('active1');
        }
      } else {
        if ($('.range-alert1').hasClass('active1')) {
          $('.range-alert1').removeClass('active1');
        }
      }
    }
  });
  $('.range1, .range-alert1').on('mousedown', function(event) {
    event.stopPropagation();
  });
  $('#slider-range2').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [4.45,12.15]
  });
  $('.ui-slider-range2').append($('.range-wrapper2'));
  $('.range2').html('<span class="range-value2"><sup></sup>' + $('#slider-range2').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider2"></span><span class="range-value2"><sup></sup>' + $("#slider-range2").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range2').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range2').html('<span class="range-value2"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider2"></span><span class="range-value2"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));
      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert2').hasClass('active2')) {
          $('.range-alert2').addClass('active2');
        }
      } else {
        if ($('.range-alert2').hasClass('active2')) {
          $('.range-alert2').removeClass('active2');
        }
      }
    }
  });
  $('.range1, .range-alert2').on('mousedown', function(event) {
    event.stopPropagation();
  });
  $('#slider-range3').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [1.45,23.15]
  });
  $('.ui-slider-range3').append($('.range-wrapper3'));
  $('.range3').html('<span class="range-value3"><sup></sup>' + $('#slider-range3').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider3"></span><span class="range-value3"><sup></sup>' + $("#slider-range3").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range3').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){ 
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range3').html('<span class="range-value3"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider3"></span><span class="range-value3"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));

      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert3').hasClass('active3')) {
          $('.range-alert3').addClass('active3');
        }
      } else {
        if ($('.range-alert3').hasClass('active3')) {
          $('.range-alert3').removeClass('active3');
        }
      }
    }
  });

  $('.range3, .range-alert3').on('mousedown', function(event) {
    event.stopPropagation();
  });
$('#slider-range4').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [0,13]
  });
  $('.ui-slider-range4').append($('.range-wrapper4'));
  $('.range4').html('<span class="range-value4"><sup></sup>' + $('#slider-range4').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider4"></span><span class="range-value4"><sup></sup>' + $("#slider-range4").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range4').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range4').html('<span class="range-value4"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider4"></span><span class="range-value4"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));
      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert4').hasClass('active4')) {
          $('.range-alert4').addClass('active4');
        }
      } else {
        if ($('.range-alert4').hasClass('active4')) {
          $('.range-alert4').removeClass('active4');
        }
      }
    }
  });
  $('.range4, .range-alert4').on('mousedown', function(event) {
    event.stopPropagation();
  });
  $('#slider-range5').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [12.30,22]
  });

  $('.ui-slider-range5').append($('.range-wrapper5'));
  $('.range5').html('<span class="range-value5"><sup></sup>' + $('#slider-range5').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider5"></span><span class="range-value5"><sup></sup>' + $("#slider-range5").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  $('#slider-range5').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15"); 
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range5').html('<span class="range-value5"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider5"></span><span class="range-value5"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));

      $(this).data({
        'value': parseInt(r)  
      });

      if (ui.values[1] === 110000) {
        if (!$('.range-alert5').hasClass('active5')) {
          $('.range-alert5').addClass('active5');
        }
      } else {
        if ($('.range-alert5').hasClass('active5')) {
          $('.range-alert5').removeClass('active5');
        }
      }
    }
  });
  $('.range5, .range-alert5').on('mousedown', function(event) {
    event.stopPropagation();
  });
  $('#slider-range6').slider({
    range: true,
    min: 0,
    max: 24,
    step: 0.25,
    values: [5,20]
  });

  $('.ui-slider-range6').append($('.range-wrapper6'));

  $('.range6').html('<span class="range-value6"><sup></sup>' + $('#slider-range6').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider6"></span><span class="range-value6"><sup></sup>' + $("#slider-range6").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');

  $('#slider-range6').slider({
    slide: function(event, ui) {
  var n = ui.values[0].toString();
      var res = n.substr(-2);
      if(res==".5"){
        var r = n.replace(".5", ".30");
      }
       else if (res=="25") {
        var r = n.replace("25", "15");
     } else if (res=="75"){
       var r = n.replace("75", "45");
     }
     else{
      var r=ui.values[0];
     }
     var y = ui.values[1].toString();
      var res = y.substr(-2);
      if(res==".5"){
        var  s= y.replace(".5", ".30");
      }
       else if (res=="25") {
        var s = y.replace("25", "15");
     } else if (res=="75"){
       var s = y.replace("75", "45");
     }
     else{
      var s=ui.values[1];
     }
      $('.range6').html('<span class="range-value6"><sup></sup>' + r.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider6"></span><span class="range-value6"><sup></sup>' + s.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
      var previousVal = parseInt($(this).data('value'));
      $(this).data({
        'value': parseInt(r)
      });
      if (ui.values[1] === 110000) {
        if (!$('.range-alert2').hasClass('active2')) {
          $('.range-alert2').addClass('active2');
        }
      } else {
        if ($('.range-alert6').hasClass('active6')) {
          $('.range-alert6').removeClass('active6');
        }
      }
    }
  });
  $('.range6, .range-alert6').on('mousedown', function(event) {
    event.stopPropagation();
  });
});


