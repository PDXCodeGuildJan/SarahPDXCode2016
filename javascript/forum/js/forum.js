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

    //get the data out of the form
    var titleBox = document.getElementById("title").value; 
    var textBox = document.getElementById("post").value; 
        console.log(titleBox); 
        console.log(textBox); 
}


 //Get the data from the spreadsheet 
function getTheInfo(){
   
    $.ajax({
        url: "https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script", 
        // tell jQuey that we are expecting JSONP 
        type: 'get', 
        dataType: "jsonp", 
        //data:{ //the data being sent to the server with the request 
        success: function(data){ 
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

    var entirePost = ""; 

   
    var postBeg = "<p>"
    var postContent = ''
    var postEnd = "</p>"

    // loop through data to pull out specific pieces 
    for (var i = 0; i < postList.length; i++){
        postContent += [
        data.feed.entry[i].gsx$post.$t, 
        data.feed.entry[i].gsx$timestamp.$t, 
        data.feed.entry[i].gsx$title.$t, 
        ].join(); 
     // grab the id in the HTML - where we want the posts to go
    document.getElementById("posts").innerHTML = postBeg + postContent + postEnd; 

    }


    console.log(postList, "Get was successful")



window.getTheInfo(); 


// Step2: Getting the (XML) data posts/Build CSS/HTML (AJAX)

// 
// }

// Step3: POSTing the posts (XML) 