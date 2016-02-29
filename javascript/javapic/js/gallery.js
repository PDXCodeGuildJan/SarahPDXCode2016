// Javapic develop something beautiful page 

//create on click event listener 
//Format: element.addEventListener('event', functionName[flowBool]); 
window.addEventListener('load', showGalleryImgs); 

// update the slogan to add a ", user_name", with the user's name

//loop through the image folder and display each image in the folder
function showGalleryImgs(){
   // alert("This is a test popup"); 

    // make empty lists to put the image strings in
    var oneImage = ""; 
    var allImages = ""; 

    //grab the id from HTML
    var showGalleryImgs = document.getElementById("gallery"); 

    //<img src="images/pdxcg_01.jpg"/> 
    // final = front + middle + end 
        // change the middle 

    //By putting in <li> into the HTML string, it creates a <li> element before and after each img string. 
    //This can be done with other HTML elements, esentially a whole webpage can be built in these strings (Pg 223)
    var imageStrBeg = "<li><img src='images/pdxcg_"; 
    //no need to indictae the middle string, we do so below
    var imageStrEnd = ".jpg'/></li>"; 

    //iterate through each photo number 
    // loop through each image and put eat new one in a new string 
    for (var i = 1; i <= 60; i++){
        // if the variable being iterated is less than 10 (i.e. containes a 0)
        if (i <= 9){
            // add 0 to the number 
            i = "0" + i; 
        }; 

        // elif if the number is 42, do something else 

        console.log("Printing the image string to make sure it is correct", imageStrBeg, i, imageStrEnd) 

        // concatinate them back together in a string variable  
        oneImage = (imageStrBeg + i + imageStrEnd); 
            //put them into a array each time they iterate 

        // add one image to another and put them in the empty string made in the beginning 
        allImages += oneImage; 
     };

    console.log(allImages); 

    // access each image stored in the element gallery 
    showGalleryImgs.innerHTML = allImages

}; 
    
// when the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes:
// add the functionality so that if a user clicks on an image, the lightbox appears with that image loaded in: 
// 1) make an onlickevent - if click anywhere on page, it changes the class = 'display-none' to "display-img'

function lightBox(event){ 
    //event is like self, specific to this function only 
    //alert("This is for the lightBox function!")

   //console.log(event.target)
   //event = click, target = what you are point out 

   // if click on the photo, capture src of it, make that source the picture 
    var imageClick = event.target.src

    // if click anywhere between the photos, make nothing happen 
   if (imageClick){

   //grab the id from HTML, change class name 
       var imageShow = document.getElementById("image_show"); 
       imageShow.className = "display_img"; 

        // taking the element id's first child - img - change pic is the div 
        //changing the src to reflect the one that is being clicked on
        imageShow.firstChild.src = imageClick
    }
}
document.addEventListener('click', lightBox); 



//If click outside photo, image disapears - class goes back to display none
function closePhotoviewing(){ 
    //alert("This is closePhotoviewing")
   
     // add an event listener to the div 
    var imageDisapear = document.getElementById("image_show"); 
   
    // if we click anywhere outside the photo... 
    if (imageDisapear){
    //grab the id from HTML, change class name 
        imageDisapear.setAttribute("class", "display_none"); 
    }
    // if you click on the photo, do nothing 

    // if you click anywhere else besides the photo - change the display_img back to display_none inclass 
}
image_show.addEventListener('click', closePhotoviewing); 








