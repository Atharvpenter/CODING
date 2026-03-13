// everthing js is an object
// string
let a = "atharv"
console.log(typoof(a))

// obj
let a1 = ["athav","ar"]
console.log(typeof(a1))

// using function in js to reduce repeatations
function add(x,y){
    console.log(x+y)
}
add(2,9)

// basic operations in js
// push(), pop(), unshift(), shift()
let a2 = ["arha","aad","aae"]
b = a2.push("as")
console.log(a2)

b1 = a2.pop()
console.log(a2)

b2 = a2.unshift("aa3")
console.log(a2)

b3 = a2.shift()
console.log(a2)

// using switch case
let city ='pune'
switch(city){
    case 'pune':
        console.log("MH")
    case 'jaipur':
        console.log("RJ")
    case 'ujjain':
        console.log("MP")
    default:
        console.log("Invalid cityname.....")
}

// using break statement in switch case
let city1 ='pune'
switch(city1){
    case 'pune':
        console.log("MH")
        break
    case 'jaipur':
        console.log("RJ")
        break
    case 'ujjain':
        console.log("MP")
        break
    default:
        console.log("Invalid cityname.....")
}

// using loops js
// print 1 to 10
for(let i = 1; i <= 10; i++){
    console.log(i)
}

// print table of 3
for(let i = 3; i <= 30; i = i + 3){
    console.log(i)
}

// print table of 3 in reverse
for(let i = 30; i <= 3; i = i - 3){
    console.log(i)
}

// calculate age using loops
birthyear = [1989,1999,200,2001,2002,2003]
age = []
for(let i = 0; i < birthyear.length; i++){
    a = 2025 - birthyear[i]
    age.push(a)
    console.log(age)
}

// map() function
// map(function(el,index,arr))
let byear = [1989,1999,200,2001,2002,2003]
let agee = byear.map(function(el,index,acc){
    return 2025 - el
})
console.log(agee)

// reduce() function
// redunce(function(,acc,el,index,arr))
// add all number given
let number = [1,2,6,5,9,8,4,6]
let v = number.map(function(el,index,arr){
    return acc + el
})

// flat()
// add multiple array for all elements
let cities = [["pune","mumbai"],["Udaipur","jaipur"],["sangamner","nashik"]]
let aa = cities.flat()
console.log(aa)

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