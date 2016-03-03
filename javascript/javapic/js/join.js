//"join us" popup that asks for user info 

// form validation should have all fields marked "required" required, 
//and all email fields should require and check for proper email syntax.

// any validation errors should be presented clearly to the user so that 
//they may correct them

// on completion of the form, navigate the user to the gallery, 
//passing their name to the page

//--------------------------------------------------------------------//
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
    var nameCheck = document.getElementById("signup").name.value;

    //check to see if name has more than one character 
    if (nameCheck.length > 1){
        return true; 
    } else 
        alert("Please input a name greater than one character"); 
    return false; 
    }; 
//
    //document.onclick = function() {console.log(name())}; 


// function to check the user name input 
// alert is userName isn't correct 
function userName(){ 

    var getUserName = document.getElementById("signup").username.value; 

    // check to see if username has more than one character 
    //make sure username is enough characters and matches what I set is required 
    if (getUserName.length > 5){
        return true; 
    } else 
        //alert if username isn't enough characters 
        alert("Please create a username that has more than five characters")
    return false; 
    }; 


//function to check to see if the email is correct 
// regex.test to check the email - use regex101.com to help
function emailCheck(){

    var emailCheck = document.getElementById("signup").email.value; 

    if (emailCheck)

}; 

//overall function to make sure all of above are valid and can use the 


function verifyAllForSubmit(event){
    event.preventDefault(); 

    nameVer = name()
    userNameVer = userName
    

    if // nameVer & username and email check all do this... else... do something else 

}; 

// set onlick for submit button 
//prevent.default needs to be applied so it doesn't refresh by itself
// turning off the default routing of where the form is going 
document.getElementById("submit").addEventListener("click", verifyAllForSubmit); 










