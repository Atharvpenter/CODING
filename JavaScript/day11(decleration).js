// Function Decleration ---->
function add(){
    console.log(5+6)
}
add()

// Function Expression ---->
let add1 = function (x, y) {
    return x + y
}
add1()

// Arrow function ---->
let add2 = (x, y) => {
    return x + y
}
add2(23, 4)

// Difference between Arrow function and function expression.
// Function Expression ---->

var fname = "atharv"
var lname = "penter"
let info = {
    firstName: "kshitij",
    lastName: "Gade",
    displayName: function () {
        console.log(this)
        console.log(this.firstName + this.lastName)
        let displayTwo = function(){
            console.log(this.firstName + this.lastName)
        }
        displayTwo()
    }
}
info.displayName()


// Arrow function ---->

let info1 = {
    firstName : "atharv",
    lastName : "penter",
    displayName : function () {
        console.log(this.firstName + this.lastName)
        let displayTwo = () =>{
            console.log(this.firstName + this.lastName)
        }
        displayTwo()
    }
}
info1.displayName()
