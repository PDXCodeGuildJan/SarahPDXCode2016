// Create a very basic forum, using HTML, CSS, and Javascript, 
//with a Google Spreadsheet as a database. Users will fill out a simple 
//form to submit their posts to the forum, which will load all of the posts 
//stored in the 'database'.

//This single page website will be created completely from scratch. 
// You will create the HTML, CSS, and Javascript needed. Below is the API 
//information you need to post and get from then spreadsheet.

// send data to Google ** CORS error will say this failed even if it doesn't 

//-----------------------------------------------------------------------//



// Step 1: Adding to spreadsheet aka post to the spreadsheet 
    // GETting the data from speadsheet into console.log 
    // Post hard coded Javascript to spreadsheet 

//trigger when submit button is clicked...
var submit = document.getElementById("submit"); 
submit.addEventListener("click", getBoxInfo)


// Function that grabs the information from the title and text box
function getBoxInfo (event){ 

    //prevent it from autosubmitting form 
    event.preventDefault(); 

    //get the data value out of the form fields 
    var titleBox = document.getElementById("title").value; 
    var textBox = document.getElementById("post").value; 
        console.log(titleBox); 
        console.log(textBox); 
}


 //Get the data from the spreadsheet 
function getTheInfo(){

   // AJAX call to get the data from the google spreadsheet
    $.ajax({
        url: "https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script", 
        type: 'get', 
        // tell jQuey that we are expecting JSONP 
        dataType: "jsonp", 
        // get the data from the AJAX call and drill down into the info you want from it
        success: function(data){ 
            // store in a variable the loction of the information you would like 
            var postList = data.feed.entry;

            // call function to pass object list to it 
            showPost(postList)
        }, 
        error: function(){
            console.log("Get was unsuccessful")
        }
    }); 

}


function showPost(postList){ 
   
    var postBeg = "<p>"
    var postContent = ''
    var postEnd = "</p>"

    // loop through data to pull out specific pieces 
    for (var i = 0; i < postList.length; i++){
        postContent += 
        postBeg +
        postList[i].gsx$timestamp.$t + "<br>" + 
        postList[i].gsx$title.$t + "<br>" + 
        postList[i].gsx$post.$t 
        +
        postEnd;
     // grab the id in the HTML - where we want the posts to go
    document.getElementById("posts").innerHTML = postContent; 

    console.log(postList, "Get was successful"); 

    }

}; 

window.getTheInfo(); 





