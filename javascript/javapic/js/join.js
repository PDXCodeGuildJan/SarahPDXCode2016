//"join us" popup that asks for user info 

// form validation should have all fields marked "required" required, 
//and all email fields should require and check for proper email syntax.

// any validation errors should be presented clearly to the user so that 
//they may correct them

// on completion of the form, navigate the user to the gallery, 
//passing their name to the page





// add form validation that works in all major browsers 
//(you'll need to deactivate browser validate to check this)
function disableFormValidation(){ 
    var form = document.getElementById("signup"); 
    form.noValidate = true; 
    //console.log(disableFormValidation); 
}; 

disableFormValidation(); 
// get code to store information first 

//function to check the name is correct 
// alert if name isn't correct 
function name(){ 

    //grab the value they input in the name box 
    var nameCheck = document.getElementById("signup"); 
    nameCheck.name.value; 

    if (name.length > 2){
        alert ("The name needs to have at least two charcters. Please try again.")
    }

    // temporarily store information to be able to check it 

    //check to see if name is all letters and no characters  

    // alert if input is anything other than letters 
    //return true or false 

}; 
//

// function to check the user name input 
// alert is userName isn't correct 
function userName(){ 

    // temporarily store information to be able to check it 

    //make sure username is enough characters and matches what I set is required 

    //alert if username isn't enough characters 

    // return true or false 

}; 


//function to check to see if the email is correct 
// regex.test to check the email - use regex101.com to help
function emailCheck(){

}; 

//overall function to make sure all of above are valid and can use the 
function verifyAllForSubmit(){


}; 



// set onlick for submit button 
//prevent.default needs to be applied so it doesn't refresh by itself
document.getElementById("submit").addEventListener("click", verifyAllForSubmit).preventDefault(); 











