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
}; 

disableFormValidation(); 

//function to check the name is correct, alert if name has less than 1 character
function personalName(){ 

    //grab the value they input in the name box 
    var nameCheck = document.getElementById("signup").name.value;

    //store locally to load on gallery.html
    localStorage.setItem("nameCheck", nameCheck); 

    //check to see if name has more than one character 
    if (nameCheck.length > 1){
        return true; 
    } else{
        alert("Please input a name greater than one character"); 
    return false; 
    }

    }; 

// testing to see if returns true or false:
//document.onclick = function() {console.log("The personal name", personalName())}; 

// function to check the user name input 
// alert is userName isn't correct aka user doesn't any characters 
function theUserName(){ 

    //Grab the value they put in for their username 
    var getUserName = document.getElementById("signup").username.value; 

    // check to see if username has more than one character 
    //make sure username is enough characters and matches what I set is required 
    if (getUserName.length > 5){
        return true; 
    } else {
        //alert if username isn't enough characters and return false
        alert("Please create a username that has more than five characters"); 
    return false; 
    }
    }; 
 
// testing to see if returns true or false:
//document.onclick = function() {console.log("The user name", theUserName())}; 

//function to check to see if the email is correct - will return true to false. 
function emailCheck(){

    //Grab the value they put in for their email. 
    var getemailCheck = document.getElementById("signup").email.value; 
    // Regex code to see if they match my requirements - no spaces or @ before 
    //or after the @ required in the email. See notes in notebook for details. 
    var chkEmail = /^[^@\s]+@[^@\s]+\.[^@\s]+$/; 

    if (chkEmail.test(getemailCheck)){
        return true; 
    } else {
        alert("Your email input was not entered correctly. Please try again. Example: name@gmail.com"); 
    return false; 
    }
    }; 

   // testing to see if returns true or false:
   //document.onclick = function() {console.log("email check", emailCheck())}; 

function verifyAllForSubmit(event){
//function that ties all above functions together and runs if all are true. 
//Redirects to gallery.html 

    event.preventDefault(); 

    nameVer = personalName(); 
    userNameVer = theUserName(); 
    emailCheckVer = emailCheck();  

    // if all of the above is true, then send the button to... 
    if (nameVer && userNameVer && emailCheckVer){
        window.location = "gallery.html"; 
    }
    
    }; 


// set onlick for submit button 
//prevent.default needs to be applied so it doesn't refresh by itself
// turning off the default routing of where the form is going 
document.getElementById("submit").addEventListener("click", verifyAllForSubmit); 












