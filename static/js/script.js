let num_products = 0;
let list_products = []
$(document).ready(function() {
    $('.btn').on('click', function (e) {
        let id = $(this).data("value");  
        let item = [
             $( "input[name=name_product"+id+"]" ).val(),
             $( "input[name=value_product"+id+"]" ).val()
        ]
        list_products.push(item)
        $( "input[name=data]" ).val(list_products)
    });  


});

