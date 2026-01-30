// everything in js is an object

const { jsx } = require("react/jsx-runtime")

// using function to reduce repeatations in the code
function cal(x,y){
    console.log(x+y)
}
cal(9,3)

// string
let a = "atahrv"
console.log(typeof(a))

// obj
let a1 = ["atahv","af"]
console.log(typeof(a1))

// basic methods in js
// push, pop,unshift,shift
let a2 = ["atharv","ram","sham"]
b1 = a2.push("Krushna")
console.log(a2)

b2 = a2.pop()
console.log(a2)

b3 = a2.unshift("krushna")
console.log(a2)

b4 = a2.shift()
console.log(a2)

// using switch case
let city = 'pune'
switch(city){
    case 'pune':
        console.log("MH")
    case 'jaipur':
        console.log("RJ")
    case 'Ujjain':
        console.log("MP")
    default:
        console.log("Invalid city name .....")
}

// using breaks statement in switch case
let city1 = 'jaipur'
switch(city1){
    case 'pune':
        console.log("MH")
    case 'jaipur':
        console.log("RJ")
    case 'Ujjain':
        console.log("MP")
    default:
        console.log("Invalid city name .....")
}

// using loops in js
// print 1 to 10
// for(r = 1; r <= 10; r++){
//     console.log(i)
// }

// print table of 2
// for(let i = 2; i <= 20; i = i + 2){
//     console.log(i)
// }

// print table of 2 in reverse
// for(let i = 20; i <= 2; i = i -2){
//     console.log(i)
// }

// calculate age using loops
birthyear = [1998,1999,2000,2001,2002,2003]
age = []
for(let z = 0; z < birthyear.length; z++){
    a = 2025 - birthyear[i]
    age.push(a)
    console.log(age)
}

// map() function
// map(function(el,index,arr))
by = [1998,1999,2000,2001,2002,2003]
age = by.map(function(el,index,arr){
    return 2025 - el
})
console.log(age)

// Reduce() function
// reduce(function(accumulator,el,index,arr))
// Add all numbers given
let number = [33,88,55,66]
let v = number.reduce(function(acc,el,index,arr){
    return acc + el
})
console.log(v)

// forEach() function 
// add welcome for all elements
let cities = ["pune","mumbai","delhi","Nashik"]
let vv = cities.forEach(function(el,index,arr){
    console.log("Welcome " + el)
})

// flat()
// add multiple array in single array
let city4 = [["pune","mumbai"],["Udaipur","jaipur"],["sangamner","nashik"]]
let av = city4.flat()
console.log(av)

// Slice()
// slice(StartIndex,EndIndex(not included))
//index         0   1   2   3   4   5   6   7
let number1 = [ 1 , 4 , 3 , 5 , 6 , 7 , 8 , 5]
//index        -7  -6  -5  -4  -3  -2  -1   0
let q = number1.slice(2)
console.log(q)
console.log(number1.slice(-7,6))
console.log(number1.slice(-6,-5))

// sum of all numbers
let digit = [22,33,44,55,77]
let total = 0
for(let i =0; i<digit.length;i++){
    total = total + digit[i]
}
console.log(total)

// array destruction
let arr = [1 , 2 , 3 , 4 , 5]
let [t1 , t2 , t3 , t4 , t5] = arr
console.log(t3)
console.log(t1)

// class
class name{
    fn = "Atharv"
    ln = "Penter"
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let ap = new name()
console.log(ap)

// lexical scope
function addA(){
    e1 = 3
    e2 = 9
    console.log(e1 + e2)
    function addB(){
        e3 = 4
        e4 = 8
        console.log(e1 + e2 + e3 + e4)
        function addC(){
            e5 = 9
            console.log(e1 + e2 + e3 + e4 + e5)
        }
        addC()
    }
    addB()
}
addA()

// declerations
// function declerations
let add = function(){
    console.log(9+3)
}
add()

// function expression
let add1 = function(x,y){
    console.log(x+y)
}
add1(4,6)

// arrow function
let add2 = (x,y) =>{
    console.log(x+y)
}
add2(4,9)

// promises
let p = new Promise(function(resolve,reject){
    let a = 10
    let b = 15
    if(a == b){
        resolve("Hello")
    }else{
        reject("Bye")
    }
})
p.then(function(str){
    console.log(str)
}, function(str){
    console.log(str)
})

// Using .then, .catch, .finally
let p1 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("Hello")
    }else{
        reject("Bye")
    }
})
.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(str){
    console.log("I will always execute")
})