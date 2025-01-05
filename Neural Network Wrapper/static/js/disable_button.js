/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * *
 * Disable submit button on symptoms page until at least one checkbox is selected
 
$('#submit_button1').prop("disabled", true);
$('#submit_button2').prop("disabled", true);*/
$('#submit_button').prop("disabled", true);

$('input:checkbox').click(function() {
    if ($(this).is(':checked')) {
        $('#submit_button').prop("disabled", false);
        /*$('#submit_button1').prop("disabled", false);
        $('#submit_button2').prop("disabled", false);*/
    } 
    else {
        if ($('.chk').filter(':checked').length < 1){
            $('#submit_button').attr('disabled',true);            
        }
    }
});

