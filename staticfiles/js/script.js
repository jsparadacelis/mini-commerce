let num_products = 0;

$(".btn_set_cant").click(
    function(){
        num_products++;
        $("input[name = cant_product]").val(num_products);  
    }
);

