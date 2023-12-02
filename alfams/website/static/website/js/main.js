
    //$('#button-minus').click(function(){
    // $("#calc").val(parseInt($("#calc").val())-1);
    //});
    //$('#button-plus').click(function(){
    // $("#calc").val(parseInt($("#calc").val())+1);
    //}); 

//$('.button-minus').on('click', function(){
//        $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) - 1)
//})
//$('.button-plus').on('click', function(){
//        $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) + 1)
//})

$(document).on('click', '.button-minus', function () {
    var $input = $(this).parent().find('input');
    var count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    $input.attr('value', count);
    $input.change();
    return false;
  });

  $(document).on('click', '.button-minus', function () {
    var $input = $(this).parent().find('input');
    var count = parseInt($input.val()) + 1;
    count = count > ($input.attr("maxlength")) ? ($input.attr("maxlength")) : count;
    $input.val(count);
    $input.attr('value', count);
    $input.change();
    return false;
  });