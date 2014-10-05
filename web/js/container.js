$(function() {
    // Hide/Show dentist info initial
    $('#dentist_info').hide()
    $('#customer_type').change(function() {
	var ct = $("input[name='customer_type']:checked").val();
	if (ct == 2 || ct == 4) {
	    $('#dentist_info').show();
	} else {
	    $('#dentist_info').hide();
	}
    });

    // form hide/Show
    $('#order_form2').hide()
    $('#order_form3').hide()
    $('#next1').click(function() {
	$('#order_form1').hide();
	$('#order_form2').show();
	$('#order_form3').hide();
    });
    $('#prev2').click(function() {
	$('#order_form1').show();
	$('#order_form2').hide();
	$('#order_form3').hide();
    });
    $('#next2').click(function() {
	$('#order_form1').hide();
	$('#order_form2').hide();
	$('#order_form3').show();
    });
    $('#prev3').click(function() {
	$('#order_form1').hide();
	$('#order_form2').show();
	$('#order_form3').hide();
    });
    
});




