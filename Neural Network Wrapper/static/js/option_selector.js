/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//Populates sex items list if the animal type is selected
function populateSex(getTypeOption, setSexOptions) {
    var getTypeOption = document.getElementById(getTypeOption);
    var setSexOptions = document.getElementById(setSexOptions);
    setSexOptions.innerHTML = "";
    
    if (getTypeOption.value !== "") {
         var optionArray = ["|--Select Sex--", "Male|Male", "Female|Female"];
    } 
    
    for (var option in optionArray) {
        var pair = optionArray[option].split("|");
        var newOption = document.createElement("option");
        newOption.value = pair[0];
        newOption.innerHTML = pair[1];
        setSexOptions.options.add(newOption);
    }

}


//Checks whether all the selections are done in the dropdown menu items on the basic information page
function check_signup_inputs() {
    var nameInput = document.getElementById('name').value;
    var telephoneInput = document.getElementById('telephone').value;
    var cnicInput = document.getElementById('cnic').value;
    var locationInput = document.getElementById('location').value;
    var hospitalInput = document.getElementById('hospital').value;
    var dinInput = document.getElementById('din').value;
    var emailInput = document.getElementById('email').value;
    var passwordInput = document.getElementById('password').value;
    var passwordConfirmationInput = document.getElementById('password_confirmation').value;
   
    if(nameInput === ""){        
        alert("Enter you name");
        document.getElementById('name').focus();
        return false;
    }
    else if (telephoneInput == ""){
        alert("Enter your phone number" );
        document.getElementById('telephone').focus();
        return false;
    }
    else if (locationInput === ""){
        alert("Select your locatoin");
        document.getElementById('location').focus();
        return false; 
    }
    
    else if (hospitalInput === ""){
        alert("Enter the hospital name you are working in");
        document.getElementById('hospital').focus();
        return false; 
    } 
    
    else if(emailInput === ""){        
        alert("Enter your email");
        document.getElementById('email').focus();
        return false;
    }
    
    else if (passwordInput === ""){
        alert("Enter the  password");
        document.getElementById('password').focus();
        return false; 
    }
    else if (passwordConfirmationInput === ""){
        alert("Enter Password Confirmation");
        document.getElementById('password_confirmation').focus();
        return false; 
    }
    
    
    var ispasswordMatched= passwordInput.localeCompare(passwordConfirmationInput);
    if(ispasswordMatched == -1){
        alert("Password mismatch! Enter correct password");
        document.getElementById('password_confirmation').focus();
        return false;
    }
}


function check_login_inputs() {
    var emailInput = document.getElementById('email').value;
    var passwordInput = document.getElementById('password').value;
    
    if (emailInput === ""){
        alert("Enter a valid email");
        document.getElementById('email').focus();
        return false; 
    }
    else if (passwordInput === ""){
        alert("Enter password");
        document.getElementById('password').focus();
        return false; 
    }
    return true;
}

//Populates age items list if the animal sex is selected
function populateAge(getSexOption, setAgeOption) {
    var getSexOption = document.getElementById(getSexOption);
    var setAgeOption = document.getElementById(setAgeOption);
    setAgeOption.innerHTML = "";
    if (getSexOption.value !== "") {
        var optionArray = ["|--Select Age--", "New Born|New Born", "Growing|Growing", "Adult|Adult"];
    } 
    
    for (var option in optionArray) {
        var pair1 = optionArray[option].split("|");
        var newOption1 = document.createElement("option");
        newOption1.value = pair1[0];
        newOption1.innerHTML = pair1[1];
        setAgeOption.options.add(newOption1);
    }

}

//Populates breed items list if the animal age is selected
function populateBreed(getAgeOption, setBreedOption) {
    var getAgeOption = document.getElementById(getAgeOption);
    var setBreedOption = document.getElementById(setBreedOption);
    setBreedOption.innerHTML = "";
    if (getAgeOption.value !== "") {
        var optionArray = ["|--Select Breed--", "Local|Local", "Imported|Imported", "Crossbred|Crossbred"];
    } 
    
    for (var option in optionArray) {
        var pair1 = optionArray[option].split("|");
        var newOption1 = document.createElement("option");
        newOption1.value = pair1[0];
        newOption1.innerHTML = pair1[1];
        setBreedOption.options.add(newOption1);
    }
}

//Checks whether all the selections are done in the dropdown menu items on the basic information page
function check_inputs() {
    var typeSelecter = document.getElementById('typeSelection').value;
    var sexSelecter = document.getElementById('sexSelection').value;
    var ageSelecter = document.getElementById('ageSelection').value;
    var breedSelecter = document.getElementById('breedSelection').value;
   // var hygieneSelecter = document.getElementById('hygieneSelection').value;
   
    if(typeSelecter === ""){        
        alert("Select animal's species");
        document.getElementById('typeSelection').focus();
        return false;
    }
    if (sexSelecter === ""){
        alert("Select animal's sex");
        document.getElementById('sexSelection').focus();
        return false; 
    }
    else if (ageSelecter === ""){
        alert("Select animal's age");
        document.getElementById('ageSelection').focus();
        return false; 
    }
    else if (breedSelecter === ""){
        
        alert("Select animal's breed");
        document.getElementById('breedSelection').focus();
        return false; 
    }
   
    return true;
}

//Urdu Version - Checks whether all the selections are done in the dropdown menu items on the basic information page
function check_inputsUrdu() {
    var typeSelecter = document.getElementById('typeSelection').value;
    var sexSelecter = document.getElementById('sexSelection').value;
    var ageSelecter = document.getElementById('ageSelection').value;
    var breedSelecter = document.getElementById('breedSelection').value;
   // var hygieneSelecter = document.getElementById('hygieneSelection').value;
   
    if(typeSelecter === ""){        
        alert("جانور کی قسم کا انتخاب کریں");
        document.getElementById('typeSelection').focus();
        return false;
    }
    if (sexSelecter === ""){
        alert("جانور کی جنس کا انتخاب کریں");
        document.getElementById('sexSelection').focus();
        return false; 
    }
    else if (ageSelecter === ""){
        alert("جانور کی عمر کا انتخاب کریں");
        document.getElementById('ageSelection').focus();
        return false; 
    }
    else if (breedSelecter === ""){
        
        alert("جانور کی نسل کا انتخاب کریں");
        document.getElementById('breedSelection').focus();
        return false; 
    }
   
    return true;
}


/* Checks whether atleast one symptom is selected before form submission*/

function check_selection() {    
    if ($('.chk').filter(':checked').length < 1){
        alert("Select atleast one symptom");
        document.getElementById('checkBoxGroup').focus();
        return false; 
    }
    return true;
}

/*Urdu Version - Checks whether atleast one symptom is selected before form submission*/
function check_selectionUrdu() {    
    if ($('.chk').filter(':checked').length < 1){
        alert("بیماری کی تشخیص کے لیے مناسب علامات کا انتخاب کریں");
        document.getElementById('checkBoxGroup').focus();
        return false; 
    }
    return true;
}

/* Checks whether atleast two symptoms are selected before form submission*/

function check_two_selections() {    
    if ($('.chk').filter(':checked').length < 2){
        alert("Select atleast two symptom");
        document.getElementById('checkBoxGroup').focus();
        return false; 
    }
    return true;
}

/*Urdu Version - Checks whether atleast two  symptoms are selected before form submission*/
function check_two_selectionsUrdu() {    
    if ($('.chk').filter(':checked').length < 2){
        alert("بیماری کی تشخیص کے لیے کم از کم دو علامات کا انتخاب کریں");
        document.getElementById('checkBoxGroup').focus();
        return false; 
    }
    return true;
}