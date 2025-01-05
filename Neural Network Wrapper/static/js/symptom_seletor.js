/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$('#symptomForm').validate({
  rules: {
    'symptomsCheckboxGroup[]': {
      required: true,
      minlength: 1,
      maxlength: 2
    }
  },
//
//  messages: {
//    datetimepicker: {
//      required: "Please enter a date."
//    },
//    commercialText: {
//      required: "Please enter your message."
//    },
//    terms: {
//      required: "Please agree to terms."
//    },
//    'audit[]': {
//      required: "Please check at least 1 option.",
//      minlength: "Please check at least {0} option."
//    }
//  },
//
//  submitHandler: function(symptomForm) {
//    var text = $("#customtext").val();
//    var date = $("#datetimepicker").val();
//    var stand = 2;
//    $.ajax({
//      url: 'savedatanow.php',
//      type: "POST",
//      data: {
//        text: text,
//        date: date,
//        stand: stand
//
//      },
//      dataType: 'text',
//      success: function(response) {
//
//        alert(response);
//      }
//    });
//    //alert('outside ajax');
//  },
//
//  highlight: function(element) {
//    $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
//  },
//  unhighlight: function(element) {
//    $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
//  },
//
//  errorClass: 'help-block',
//  errorPlacement: function(error, element) {
//    if (element.parent('.form-group').length) {
//      error.insertAfter(element.parent());
//    } else {
//      error.insertAfter(element.parent());
//    }
//    if (element.attr('name') == 'number[]') {
//      error.insertAfter('#checkboxGroup');
//    } else {
//      error.appendTo(element.parent().next());
//    }
//  }

});