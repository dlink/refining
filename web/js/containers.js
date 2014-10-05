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
	if (!validateForm1()) {
	    return;
	}
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


    // textButtons treatment
    $('.textButton').hover(function() {
	$(this).css('cursor', 'pointer');
	$(this).css('text-decoration', 'underline');
    }, function() {
	$(this).css('cursor', 'default');
	$(this).css('text-decoration', 'none');
    })
});


/**
 * Validate Form1
*/
function validateForm1() {
    // Unset color of fields:
    $('#customer_type').css('color', '');
    $('#dentist_name_container').css('color', '');
    $('#dentist_phone_container').css('color', '');

    // Check fields set those to red that are not valid
    valid = true

    if (!$("input[name='customer_type']:checked").val()) {
	$('#customer_type').css('color', 'red');
	valid = false;
    }

    // alert($('#dentist_info').css('display'));
    if ($('#dentist_info').css('display') != 'none') {
	if (!$("input[name='dentist_name']").val()) {
	    $('#dentist_name_container').css('color', 'red');
	    valid = false;
	}
	if (!$("input[name='dentist_phone']").val()) {
	    $('#dentist_phone_container').css('color', 'red');
	    valid = false;
	}
    }
    return valid;
}
