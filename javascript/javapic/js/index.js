//front page with "join now"

// have the background image of the jumbotron change to 
//another image in the folder every 10 seconds

// add an onclick 

document.getElementById("jumbotron").addEventListener("click", rotateImages); 

// need to track the value of i outside the function so it doesn't
// 
i = 1; 

function rotateImages(){ 
    // grab the id from the HTML 
    var jumbo = document.getElementById("jumbotron");
    
    // Make the image change everytime we click on the image
    //rotateImages.style.backgroundImage = "url('images/pdxcg_02.jpg')"

    //concatinate just like gallery 
    var imageStrBeg = "url('images/pdxcg_"; 
    var imageStrEnd = ".jpg')"; 

     if (i <= 9){
        // add 0 to the number 
        i = "0" + i; 
        };

    var singleImage = (imageStrBeg + i + imageStrEnd)
    console.log(singleImage)

    //change jumbo src to equal the concatinated equasion 
    jumbo.style.backgroundImage = singleImage

    // increment 

    i++


    //need to change the style id within the jumbotron 
    
    //var rotateImages = document.getElementById("jumbotron"); 
    // rotateImages.style.background-image = ""
    //document.getElementById('jumbotron').background-image = url("../images/pdxcg_08.jpg")

    //loop through the image folder and display each image in the folder 
    //upon clicking
}

