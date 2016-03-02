//front page with "join now"

// have the background image of the jumbotron change to 
//another image in the folder every 10 seconds

// first step to project, add an onclick: 
//document.getElementById("jumbotron").addEventListener("click", rotateImages); 

setInterval(rotateImages, 10000); 

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
    
    // if the number is equal to 42, add one to it to skip it and make it 43
    if (i === 42){
        i++; 

    // else if the number is less than 9, add 0 to the number 
    } else if (i <= 9){
        // add 0 to the number 
        i = "0" + i; 
    }; 

    //concatinate the string together to make the image number increment 
    var singleImage = (imageStrBeg + i + imageStrEnd)
    //console.log(singleImage)

    //change jumbo src to equal the concatinated equasion 
    jumbo.style.backgroundImage = singleImage

    //if i - the number of photo - is equal to 60, change it to equal one
    // so it loops back 
    if (i === 60){
        i = 1
    }

    // increment 
    i++


    //need to change the style id within the jumbotron 
}

