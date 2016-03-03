//Establish the event listener for when they click an item
// Add the click event hangler to the "Add-item" button 

var addItemButton = document.getElementById("add-item"); 
addItemButton.onclick = addItem; 

var addStockButton = document.getElementById("add-stock"); 
addStockButton.onclick = addStock; 

var addRemoveButton = document.getElementById("remove-stock"); 
addRemoveButton.onclick = removeStock; 

var addDeleteButton = document.getElementById("del-item"); 
addDeleteButton.onclick = deleteItem; 


window.onload = loadDataWithAJAX; 

// make a global list to store all the inventory 
var products = []; 

/* Toggles the inStock status on the selected row inside of inventory. 
 * list, which is in the table body
 */



 function addStock() { 
    // NOT allowed to use querySelectorAll()

    // find all the selected things 
    var checkedbox = getSelectedRowBoxes(); 

    //loop through all elements and extract the info.
    for (var i=0; i<checkedbox.length; i++){

        var status = checkedbox[i].parentNode.nextSibling.nextSibling.nextSibling; 
        status.textContent = "Yes"; 
        status.className = "true"; 

        var prodID = checkedbox[i].parentNode.parentNode.id; 
        products[prodID].inStock = true; 

            // change the inStock value of the selected things    
            //for (var 1=0; i<checked.length; i++)
            };

    saveData(); 
    }; 



function removeStock(){ 
// USE querySelectorAll() 
    var removeBox = getSelectedRowBoxes(); 
   
    // SEE ALL OTHER WAYS TO SOLVE LINE 68 IN NOTEBOOK (var removeBox)

    for (var i=0; i<removeBox.length; i++) {
        var status = removeBox[i].parentNode.parentNode.children[3]; 
        status.textContent = "No"; 
        status.className = "false"; 
    }

    saveData(); 
}; 



function addItem() {
    // assigning a variable to catch the input from html 
    // "name" is the elemtent ID name in the html 
    var materialName = document.getElementById("name").value; 
    // console.log("Inside addItem function");      - printing in JS, a reference to the object in the browser
    var price = document.getElementById("price").value; 
    //console.log(price); 
    var inStock = document.getElementById("in-stock").checked; // if checked it returns true 
    //console.log(inStock); 

    // Create a new instance of the Product object with the new Item's info 

        var newProd = new Product(materialName, price, inStock); 
        //console.log(newProd); 

        products.push(newProd); 

        displayInventory(); 
        saveData(); 
       
}; 



// Delete the selected rows from the inventory 
function deleteItem(){
    // first, determine all the selected rows 
    var removeBox = getSelectedRowBoxes(); 

    // delete the Product objects that corresponds to those rows 
    // from the Producsts array 
    // looop through backwards
    for (var i = removeBox.length -1; i >= 0; i--){
        //Get the id on the row that the checkbox is in 
        var prodId = parseInt(removeBox[i].parentNode.parentNode.id); 

        // Delete the product that cooresponds thay row
        // Dete the Product at the index (id = index) 
        delete products[prodId]; 
        products.splice(prodId, 1); 
        };


    //Rerender the HTML list, using displayInventory
    displayInventory(); 
    saveData(); 

}; 



// a helper function to get all the checked boxes in the HTML's inventory
// aka previously written code
function getSelectedRowBoxes(){
    var removeBox = document.querySelectorAll("input:checked:not(#in-stock)"); 
    return removeBox; 
}; 




// Adds all the items in the products array to the HTML.
function displayInventory(){

    var inventory =  document.getElementById("inventory"); 
    inventory.innerHTML = ''; 

    // Loop through the products array, adding each Products to the 
    // inventory table, in the html. 

    for (var i = 0; i < products.length; i++){
        // Make a new row for the Product i 
        var newRow = document.createElement("TR"); 
        newRow.id = i; 

        //Make a TD for the checkbox 
        var checkbox = document.createElement("TD"); 
        // Make the actual checkbox 
        var innerCheckbox= document.createElement("INPUT"); 
        // Set the input type to the checkbox 
        innerCheckbox.type = "checkbox"; 
        // Add the checkbox into the TD 
        checkbox.appendChild(innerCheckbox); 

        // Make a TD for the mertial name 
        var materialName = document.createElement("TD"); 
        materialName.textContent = products[i].prodName; 

        // Make a TD for the price
        var price = document.createElement("TD"); 
        price.textContent = products[i].price; 

        // Make a TD for the stock toggle 
        var inStock = document.createElement("TD"); 
        // IIFE
        // Set the TD's text content to either yes or no, 
        // based on the product at index i's inStock property 
        inStock.textContent = (function(inStock){
            if (inStock){
                return "Yes"; 
            }
            return "No"; 
        }(products[i].inStock)); 
        // set the class name on the TD: 
        inStock.className = products[i].inStock; 
        // above code it like using HTML, hard coding to set it 
        // below is same exact thing but lettig javascript is setting 
        // the class name for you:
        // inStock.setAttribute("class", products[i].inStock); 


        // add all the TD's to the TR 
        newRow.appendChild(checkbox); 
        newRow.appendChild(materialName); 
        newRow.appendChild(price); 
        newRow.appendChild(inStock); 

        // Add the new row to the actual TBODY in the HTML 
        inventory.appendChild(newRow); 
    }; 

    saveData(); 
}


//getting information user is imputting and storing it in JS so its not 
// deleted next time they come back to the website 

// to start we need to make the object constructor for the products 
function Product(prodname, price, inStock){ 
    this.prodName = prodname; 
    this.price = price; 
    this.inStock = inStock; 

    this.setStock = function(stock) {
        this.inStock = stock; 
    }

}; 

// Saves the current state of products 
function saveData(){ 
    // Transform the products array into a JSON string 
    var productJSON = JSON.stringify(products); 
    console.log(productJSON); 


    // Save that JSON string to a local storage (aka local memory of the browser)
    localStorage.setItem("price-list", productJSON); 


}

// Loads the current state of the products array 
function loadData (){

    //Load the data from local storage 
    var productJSON = localStorage.getItem("price-list"); 
   // console.log("Loaded Data", productJSON)

    // Parse it into a JS data type and save to the global array 
    products = JSON.parse(productJSON)
    console.log(products); 

    //Double check that products is set to a list if null
    if (!products){
        products = []; 
    }

    //Update the rendered display 
    displayInventory(); 

}

// Load the data from json file on the server with AJAX. 
function loadDataWithAJAX(){

    // Create new XMLHttpRequest object
    var request = new XMLHttpRequest(); 

    // add the call info 
    request.open('GET', 'data.json', true); 

    // set to an annonymous function 
    request.onload = function (){
        if (request.status === 200){
            // response.Text is going to hold the info we get back from the server 
            var prodJSON = request.responseText; 
            products = JSON.parse(prodJSON); 
            displayInventory(); 


    }

}
    // Actually send out the request 
    request.send(); 

}









