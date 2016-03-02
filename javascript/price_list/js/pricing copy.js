//start scheduling events we want to trigger events 

//Establish the event listener for when they click an item
// Add the click event hangler to the "Add-item" button 

var addItemButton = document.getElementById("add-item"); 
addItemButton.onclick = addItem; 

var addStockButton = document.getElementById("add-stock"); 
addStockButton.onclick = addStock; 

var addRemoveButton = document.getElementById("remove-stock"); 
addRemoveButton.onclick = removeStock; 

// make a global list to store all the inventory 
var products = []; 

/* Toggles the inStock status on the selected row inside of inventory. 
 * list, which is in the table body
 */

 function addStock() { 
    // NOT allowed to use querySelectorAll()

    // find all the selected things 
    var checkedBoxestoremove = document.getElementsByTagName("input"); 

    // make an empty list that will contain all the boxes?      
    // var emptyboxes = []; 

    // Which things are buttons? Which buttons are checked?

    // make an empty list that will contain all the boxes once checked? 
    var checkedboxes = []; 

    //loop through all elements and extract the info.
    for (var i=0; i<checkedbox.length; i++){
        
        // make an if statement that specifies which input we want to use 
        if (checkedbox[i].checked === true){
            // start a loop that identifies whether the box is checked or not 
                // Make a list for the checked boxes to go into 
            checkedboxes.push(checkedbox[i]); 

        var status = checkedbox[i].parentNode.nextSibling.nextSibling.nextSibling; 
        status.textContent = "Yes"; 
        status.className = "true"; 

            console.log("This should be checked boxes", checkedboxes)

            // change the inStock value of the selected things    
            //for (var 1=0; i<checked.length; i++)
            };
    };
};
    


    //Update the display? Depends on previous step.


    // if (checkedbox[i].type === "checkbox"){
    //         // start a loop that identifies whether the box is checked or not 
    //         if (checkedbox[i].checked){
    //             // Make a list for the checked boxes to go into 
    //             checkedboxes.push(checkedbox[i]); 
                  
    //             console.log("This should be checked boxes", checkedboxes)


function removeStock(){ 
// USE querySelectorAll()

    // 
    var removeBox = document.querySelectorAll("input:checked:not(#in-stock)"); 
    // console.log("This should be the remove box", removeBox)
    // SEE ALL OTHER WAYS TO SOLVE LINE 68 IN NOTEBOOK (var removeBox)


    for (var i=0; i<removeBox.length; i++) {
        var status = removeBox[i].parentNode.parentNode.children[3]; 
        status.textContent = "No"; 
        status.className = "false"; 
        console.log('These are the boxes being removed', removeBox); 
    }; 
    // var checkedBoxestoremove = []; 
    // for (var i=0; i<removeBox.length; i++){ 
    //     if (removeBox[i].type === "checkbox"){
    //         if (removeBox[i].checked){
    //             checkedBoxestoremove.pop(removeBox[i]); 

}

function addItem() {
    // assigning a variable to catch the input from html 
    // "name" is the elemtent ID name in the html 
    var materialName = document.getElementById("name").value; 
    // console.log("Inside addItem function");      - printing in JS, a reference to the object in the browser
    var price = document.getElementById("price").value; 
    //console.log(price); 
    var inStock = document.getElementById("in-stock").checked; // if checked it returns true 
    //console.log(inStock); 

    var inventory = document.getElementById("inventory"); 

    var newRow = "<tr><td>" + "<input type='checkbox'/>" + "</td><td>" + materialName + "</td><td>" + price + "</td>" + 
            "<td class='" + inStock + "'>"; 

        if (inStock) {
            newRow += "Yes"; 
        } else {
            newRow += "No"; 

        }
        newRow += " </td></tr> "; 

        inventory.innerHTML += newRow;  

    // Create a new instance of the Product object with the new Item's info 

        var newProd = new Product(materialName, price, inStock); 
        //console.log(newProd); 

        
        products.push(newProd); 
}


//getting information user is imputting and storing it in JS so its not 
// deleted next time they come back to the website 

// to start we need to make the object constructor for the products 

function Product(prodname, price, inStock){ 
    this.prodname = prodname; 
    this.price = price; 
    this.inStock = inStock; 

    this.setStock = function(stock) {
        this.inStock = stock; 
    }

}










