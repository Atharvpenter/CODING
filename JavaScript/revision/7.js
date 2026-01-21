// everything in javascript is an object
// avoid repeatations in code we use function()
function cal(x,y){
    console.log(x+y)
    console.log(x-y)
    console.log(x*y)
    console.log(x/y)
}
cal(4,9)

// string
let a = "atharv"
console.log(typeof(a))

// object
let a1 = ["atharv","kunal","akhil"]
console.log(typeof(a1))

// Basic methods in js
// pop(),push(),unshift(),shift()
// push() ->
let a2 = ["atharv","Kunal","akhil"]
b = a2.push("Kshitij")
console.log(a2)

// pop() ->
b1 = a2.pop()
console.log(a2)

// unshift() ->
b2 = a2.unshift("kshitij")
console.log(a2)

// shift() ->
b3 = a2.shift()
console.log(a2)

// using switch case
let city = "Pune"
switch(city){
    case "Pune":
        console.log("MH")
    case "Jaipur":
        console.log("RJ")
    case "Surat":
        console.log("GJ")
    default:
        console.log("Incorrect city name ....")
}

// using break and continue statement in switch case
let city1 = "Jaipur"
switch(city1){
    case "Pune":
        console.log("MH")
        break
    case "Jaipur":
        console.log("RJ")
        break
    case "Surat":
        console.log("GJ")
        break
    default:
        console.log("Incorrect city name ....")
}

// using loops in js
// print table of 4
for(let i = 4; i <= 40; i = i + 4){
    console.log(i)
}

// print table of 4 in reverse
for(let i = 40; i > 0; i = i - 4){
    console.log(i)
}

// using break and continue statement in loops
// print 1 to 10 upto 7
for(let i = 1; i <= 10; i++){
    if(i == 8){
        break
    }
    console.log(i)
}

// print 1 to 10 except 7
for(let i = 1; i <= 10; i++){
    if(i == 7){
        continue
    }
    console.log(i)
}

// calculate age using loops
birthyear = [1999,2000,2001,2002,2003,2004,2005,2006]
age = []
for(let i = 0; i < birthyear.length; i++){
    a = 2025 - birthyear[i]
    age.push(a)
    console.log(age)
}

// map() function
// map(function(el,arr,index))
// now calculate age using map() function
by = [1999,2000,2001,2002,2003,2004,2005,2006]
age = by.map(function(el,index,arr){
    return 2025 - el
})
console.log(age)

// Add $ at start of all elements in the array
num = [11,22,33,44,55,66]
z = num.map(function(el,index,arr){
    return '$' + el
})
console.log(z)

// sum of all number
let digits = [1,2,3,4,5,6,7,8,9,10]
let total = 0
for(let i = 0; i < digits.length; i++){
    total = total + digits[i]
}
console.log(total)

// array destruction
let arr = [1 , 2 , 3 , 4 , 5]
let [c1 , c2 , c3 , c4 , c5] = arr
console.log(c3)
console.log(c1)

// class 
class name{
    fn = "atharv"
    ln = "penter"
    age = 22
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let ap = new name()
console.log(ap)

// lexical scope
function addA(){
    s = 1
    s1 = 9
    console.log(s + s1)
    function addB(){
        s2 = 8
        s3 = 5
        console.log(s + s1 + s2 + s3)
        function addC(){
            s4 = 9
            s5 = 3
            console.log(s + s1 + s2 + s3 + s5)
        }
        addC()
    }
    addB()
}
addA()

// declerations
// function declerations
let add = function(){
    console.log(2+3)
}
add()

// function expression
let add1 = function(x,y){
    console.log(x + y)
}
add1(2,5)

// arrow function
let add2 = (x,y) =>{
    console.log(x + y)
}
add2(9,3)

// promises
// using .then
let p = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
p.then(function(str){
    console.log(str)
}, function(str){
    console.log(str)
})

// using .then and .catch
let p1 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// using .then, .catch, and .finally
let p2 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("HELLO")
    }else{
        reject("BYE")
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