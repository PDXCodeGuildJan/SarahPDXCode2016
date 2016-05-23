//front page with "join now"

// have the background image of the jumbotron change to 
//another image in the folder every 10 seconds

// first step to project, add an onclick: 
//document.getElementById("jumbotron").addEventListener("click", rotateImages); 

//function that rotates the images every 10 seconds 
setInterval(rotateImages, 10000); 

// need to track the value of i outside the function
i = 1; 

//create function to rotate the images in the jumbotron
function rotateImages(){ 

    // grab the id from the HTML 
    var jumbo = document.getElementById("jumbotron");
    
    // Step one: Make the image change everytime we click on the image
    //rotateImages.style.backgroundImage = "url('images/pdxcg_02.jpg')"

    //break down the string just like I did in the gallery 
    var imageStrBeg = "url('images/pdxcg_"; 
    var imageStrEnd = ".jpg')"; 
    
    // Since there is no number 42, if the number is equal to 42, 
    //add one to it to skip it and make it 43
    if (i === 42){
        i++; 

    // else if the number is less than 9, add 0 to the number to make 
    //it match file name
    } else if (i <= 9){
        // add 0 to the number 
        i = "0" + i;
    };

    //concatinate the string together to make the image number increment and 
    // hold into variable
    var singleImage = (imageStrBeg + i + imageStrEnd)
    //console.log(singleImage)

    //change jumbo url to equal the concatinated equasion 
    jumbo.style.backgroundImage = singleImage

    //if i - the number of photo - is equal to 60, change it to equal one
    // so it loops back 
    if (i === 60){
        i = 1
    }

    // increment each photo 
    i++
}

