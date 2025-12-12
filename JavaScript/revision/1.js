// everything in JS is an object
// there is so many repeatations in the code so in js we use Function ->
function cal(x, y) {
    console.log(x + y)
    console.log(x - y)
    console.log(x * y)
    console.log(x / y)
}
cal(4, 8)

// to know what is the length of the string we use
let a = ["atharv", "shivam", "Ram", "shreyash", "Sham"]
console.log(typeof (a))
console.log(a)
console.log(a.length)

// Basic methods in js
// push() -> adding element in the last
b = a.push("Om")
console.log(a)

// pop() -> removing last element
b1 = a.pop()
console.log(a)

// unshift() -> adding new element in the start
b2 = a.unshift("Tom")
console.log(a)

// shift() -> removing element from the start
b3 = a.shift()
console.log(a)

    // Using switch case 
    // without break statement
    let city = "pune"
    switch (city) {
        case "pune":
            console.log("MH")
        case "rajkot":
            console.log("RJ")
        case "sarojini nagar":
            console.log("DL")
        default:
            console.log("Invalid")
    }

// with Break statement
let city1 = "pune"
switch (city) {
    case "pune":
        console.log("MH")
        break
    case "rajkot":
        console.log("RJ")
        break
    case "sarojini sarojini":
        console.log("DL")
        break
    default:
        console.log("Invalid")
}

// Loop's
// print table of 2
for (let i = 2; i <= 20; i = i + 2) {
    console.log(i)
}

// print table of 2 in reverse
for (let i = 20; i >= 2; i = i - 2) {
    console.log(i)
}

// using break statements
// print 1 to 9 upto 7
for (let i = 1; i <= 9; i++) {
    if (i == 7) {
        break
    }
    console.log(i)
}

for (let i = 1; i <= 9; i++) {
    console.log(i)
    if (i == 7) {
        break
    }
}

// using continue
// print 1 to 9 except 6
for (let i = 1; i <= 9; i++) {
    if (i == 6) {
        continue
    }
    console.log(i)
}

// print age using for loop
let birthyear = [2000, 2001, 2003, 2004]
let ages = []
for (let i = 0; i < birthyear.length; i++) {
    a = 2025 - birthyear[i]
    ages.push(a)
    console.log(ages)
}

// print age using Map() function
// map() -> arrayname.map(function(el,index,arr))
byear = [2000, 2001, 2003, 2004]
let a1 = byear.map(function (el, index, arr) {
    return 2025 - el
})
console.log(a1)

// add @ at the start of element
let arr = [11, 22, 33, 44, 55]
let z = arr.map(function (el, index, arr) {
    return '@' + el
})
console.log(z)

// using Filter() function. It is same as the map()
let num = [100,74,12,77,98,36,85,98,77]
let n = num.filter(function(el,index,arr){
    return el > 75
})
console.log(n)

// adding all array
arr2 = [99,22,33]
total = 0
for(let i = 0; i < arr2.length; i++){
    total = total + arr2[i]
}
console.log(total)

// string
let s = "atharv"
console.log(typeof(s))

// array destructing
let c = [1 , 2 , 3 , 4]
console.log(c)
let [aa , aaa , aaaa , aaaaa] = c
console.log(aaa)

// class
class name{
    fn = "atharv"
    ln = "Penter"
    age = 22
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let ap = new name()
console.log(ap)
ap.fn = "anjali"
console.log(ap)

// Map set
let mapA = new Map(
    [
        [1,'admin'],
        [2,'manager'],
        [3,'customer'],
        [4,'tutor'],
        [true,'other']

    ]
)
console.log(mapA)
console.log(mapA.size)

// Lexical Scope
function additionA(){
    let b = 2
    let b11 = 3
    console.log(a+b)
    function additionB(){
        let b12 = 5
        let b13 = 7
        console.log(b+b11+b12+b13)
        function additionC(){
            let b14 = 6
            console.log(b+b11+b12+b13+b14)
        }
        additionC()
    }
    additionB()
}
additionA()

// Declerations ->
// 1. function declerations
function add(){
    console.log(1+4)
}
add()

// 2. function Expressions
let add1 = function(x,y){
    return x + y
}
add1(4,8)

// 3. Arrow function
let add2 = (x,y) => {
    return x + y
}
add2(4,9)

// difference between function expression and arrow function
var fname = "atharv"
var lname = "penter"
let info = {
    firstName: "anjali",
    lastName: " penter",
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

// Promise has resolve, reject
// Using then
let p = new Promise(function(resolve,reject){
    let q = 10
    let q1 = 10
    if(q == q1){
        resolve("Hello")
    }else{
        reject("bye")
    }
})
p.then(function(str){
    console.log(str)
},function(str){
    console.log(str)
})

// using catch
let p1 = new Promise(function(resolve,reject){
    let q11 = 10
    let q12 = 10
    if(q11 == q12){
        resolve("hello")
    }else{
        reject("bye")
    }
})
p1.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// using then catch finally
let p2 =  new Promise(function(resolve,reject){
    let q21 = 10
    let q22 = 10
    if(q21 == q22){
        resolve("hello")
    }else{
        reject("bye")
    }
})
p.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(){
    console.log("I will always execute")
})