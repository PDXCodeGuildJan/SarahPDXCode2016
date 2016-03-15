// Create a very basic forum, using HTML, CSS, and Javascript, 
//with a Google Spreadsheet as a database. Users will fill out a simple 
//form to submit their posts to the forum, which will load all of the posts 
//stored in the 'database'.

//This single page website will be created completely from scratch. 
// You will create the HTML, CSS, and Javascript needed. Below is the API 
//information you need to post and get from then spreadsheet.

//-----------------------------------------------------------------------//



// Step 1: Adding to spreadsheet aka post to the spreadsheet 
    // GETting the data from speadsheet into console.log 
    // Post hard coded Javascript to spreadsheet 

//trigger when submit button is clicked...
var submit = document.getElementById("submit"); 
//console.log(submit)

submit.addEventListener("click", getBoxInfo)

function getBoxInfo (event){ 
// Function that grabs the information from the title and text box

//prevent it from autosubmitting form 
event.preventDefault(); 

//get the data out of the form
var titleBox = document.getElementById("title").value; 
var textBox = document.getElementById("text-box").value; 

// send data to Google ** CORS error will say this failed even if it doesn't 
// console.log(titleBox)
// console.log(textBox)

}

// function postTheInfo(){
    //function that makes the AJAX call to post the stuff 


// }

function getTheInfo(){

    //Get the data from the spreadsheet 
        //specifiy which data to get from the spreadsheet 

    $.ajax({
        url: "https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script", 
        // tell jQuey that we are expecting JSONP 
        dataType: "jsonp", 
        //data:{ //the data being sent to the server with the request 
        success: function(data){ 
            console.log(data)
            console.log("Get was successful")}, 
        error: function(){
            console.log("Get was unsuccessful")},


    }); 

}

window.getTheInfo(); 

function displayData (data){


}

// Step2: Getting the (XML) data posts/Build CSS/HTML (AJAX)



// Step3: POSTing the posts (XML) 