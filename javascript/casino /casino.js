// Number of times we are going to loop 

var number = 5; 

var inputField = document.getElementById("num-loops"); 
var counter = document.getElementById("counter");

function die() {
    // math.floor rounds the numbers down, math.random randomizes it, *6 is how many sides 
    // the dice will have, the +1 increment it so it doesn't start randomizing at 0, instead
    // at 1. 
    dieNumber = Math.floor((Math.random() * 6) + 1); 
    return dieNumber; 
}; 

function loopClick() {
    number = inputField.value; 
    counter.innerHTML = ""; 

    for (var i=0; i < number; i++){
        // print something to the console on the browser: console.log(i) OR: 
        counter.innerHTML += "<img src='dice/" + die() + ".png' alt='A die.' /><br/>"; 
    };     
}; 

// Add click listener 
document.getElementById("loop-btn").onclick = loopClick;  

//     number = inputField.value; 
//sets the value to 10: inputField.value=10
// gets the valye from inputField: inputField.value

