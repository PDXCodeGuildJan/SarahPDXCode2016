// Javapic develop something beautiful page 

//create on click event listener 
//Format: element.addEventListener('event', functionName[flowBool]); 
window.addEventListener('load', showGalleryImgs); 

// update the slogan to add a ", user_name", with the user's name


//loop through the image folder and display each image in the folder

function showGalleryImgs(){
    alert("This is a test popup"); 

    // <img src="images/pdxcg_01.jpg">
    var oneImage = ""; 
    var allImages = []; 


    //grab the id from HTML
    var showGalleryImgs = document.getElementById("gallery"); 

    //<img src="images/pdxcg_01.jpg"/> 
    // final = front + middle + end 
        // change the middle 

    var imageStrBeg = "<img src='images/pdxcg_'"; 

    var imageStrEnd = ".jpg/>"; 

    

    //iterate through each photo number 

    // loop through each image and put eat new one in a new string 
    for (var i = 1; i <= 60; i++){
        // if the variable being iterated is less than 10 (or contained a 0)
        if (i <= 9){
            // add 0 to the number 
            i = "0" + i;
        }; 

        // elif if the number is 42, do something else 

        // concatinate them back together in a string variable  
        oneImage = (imageStrBeg + i + imageStrEnd); 
            //put them into a array each time they iterate 
        allImages.push(oneImage); 


    }; 

    console.log(allImages)

    // associate each new variable with a new photo 

}; 
    
 
    // put them into an unordered list 

    // make them display properly 
    //create a variable that put the image in the spot and creates another variable 


// add the functionality so that if a user clicks on an image, the lightbox appears with that image loaded in
  
// when the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes





