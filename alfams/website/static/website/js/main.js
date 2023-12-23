
// Убавляем кол-во по клику
$( document ).ready(function() {
  $('.button-minus').click(function() {
    let $input = $(this).parent().find('.calc');
    let count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    
    
  });
  // Прибавляем кол-во по клику
  $('.button-plus').click(function() {
    let $input = $(this).parent().find('.calc');
    let count = parseInt($input.val()) + 1;
    //count = count > parseInt($input.data('max-count')) ? parseInt($input.data('max-count')) : count;
    $input.val(parseInt(count));
    console.log('+')
  });
  // Убираем все лишнее и невозможное при изменении поля
  $('.calc').bind("change keyup input click", function() {
    if (this.value.match(/[^0-9]/g)) {
        this.value = this.value.replace(/[^0-9]/g, '');
    }
    if (this.value == "") {
        this.value = 1;
    }
    //if (this.value > parseInt($(this).data('max-count'))) {
    //    this.value = parseInt($(this).data('max-count'));
    //}    
  });
});
/*
let iii = window.document.querySelectorAll('.js-cart-item-price')
num_list = []

iii.forEach(element => {
  num = element.textContent;
  num = num.replace(/[^\w\s!?]/g,'');
  num = Number(num)

  num_list.push(num);

});
console.log(num_list)
let sum = num_list.reduce((total, current) => total + current, 0);
console.log(sum)
*/
/*
body.on('input change', '.calc', function () {
  valideInputNumber(this);
  var product = $(this).parents('.cart-item-js'); 
  var productId = +$(this).parents('.cart-item-js').data('product-id');
  var productCount = +$(this).val();
  var newPriceValue = $(this).data('price') || 0;
  var newPrice = product.find('.js-cart-item-price') || null;
  setProductCountCart(productId, productCount);
  if(newPriceValue && newPrice ) {
    var updateNewPrice = parseInt(newPriceValue) * parseInt(productCount);
    var prepareCurrentPrice = parseInt(newPrice.text().replace(/\s+/g, ''));
    $({numberValue: prepareCurrentPrice}).animate({numberValue: updateNewPrice}, {
      duration: 500,
      easing: "swing",
      step: function(val) {
        newPrice.text(getFormattedPrice(Math.ceil(val.toFixed(0))));
      }
    });
  }
});
*/


/*
$( document ).ready(function() {
  $('.button-minus').click(function() {
    let $input = $(this).parent().find('.calc');
    let count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    console.log('-')
  });
  // Прибавляем кол-во по клику
  $('.button-plus').click(function() {
    let $input = $(this).parent().find('.calc');
    let count = parseInt($input.val()) + 1;
    //count = count > parseInt($input.data('max-count')) ? parseInt($input.data('max-count')) : count;
    $input.val(parseInt(count));
    console.log('+')
  });
  // Убираем все лишнее и невозможное при изменении поля
  $('.calc').bind("change keyup input click", function() {
    if (this.value.match(/[^0-9]/g)) {
        this.value = this.value.replace(/[^0-9]/g, '');
    }
    if (this.value == "") {
        this.value = 1;
    }
    //if (this.value > parseInt($(this).data('max-count'))) {
    //    this.value = parseInt($(this).data('max-count'));
    //}    
  });
});
*/