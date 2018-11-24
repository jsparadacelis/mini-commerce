let num_products = 0;

$("#btn-p1").click(
    function(){
        num_products++;
        $("input[name=num]").val(num_products);
    }
);

