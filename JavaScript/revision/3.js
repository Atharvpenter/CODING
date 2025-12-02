// in js if we want to reduce typing extra code we use funtion 
function cal(x,y){
    console.log(x + y)
    console.log(x - y)
}
cal(4,9)

// string
let a = "atharv"
console.log(typeof(a))

// object
let a1 = ["atharv","ram","sham","Madhur"]
console.log(typeof(a1))
console.log(a1.length)

// methods in js
// push() , pop(), unshift(), shift()
// push() -> adds elements inthe last
let a2 = ["atharv","ram","sham","Madhur"]
b1 = a2.push("Krish")
console.log(a2)

// pop() -> remove's last element
b2 = a2.pop()
console.log(a2)

// unshift() -> adds element in the start
b2 = a2.unshift("Krish")
console.log(a2)

// shift() -> removes the start element
b2 = a2.shift()
console.log(a2)

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

// using break statement
let city1 = "sarojini nagar"
switch (city1) {
    case "pune":
        console.log("MH")
        break
    case "rajkot":
        console.log("RJ")
        break
    case "sarojini nagar":
        console.log("DL")
        break
    default:
        console.log("Invalid")
}

// unsing for loops in js
// print table of 2 using forloops
for(let i = 2; i <= 20; i = i + 2){
    console.log(i)
}

// print table of 2 in reverse
for(let i = 20; i >= 2; i = i - 2){
    console.log(i)
}

// using break statements in for loops
// print 1 to 9 upto 6
for(let i = 1 ; i <= 9; i++){
    if(i == 6){
        break
    }
    console.log(i)
}

// using continue statement in for loops
for(let i = 1; i <= 9; i++){
    if(i == 6){
        continue
    }
    console.log(i)
}

// print age using for loops
let birthyear = [1999,2000,2001,2002,2003,2004,2005,2006]
let age = []
for(let i = 0; i < birthyear.length; i++){
    a = 2025 - birthyear[i]
    age.push(a)
    console.log(age)
}

// map()  funtion -> map(function(el,index,arr))
// print age using map() function
let birthyear1 = [1999,2000,2001,2002,2003,2004,2005,2006]
let ages = birthyear1.map(function(el,index,arr){
    return 2025 - el
})
console.log(ages)

// add @ in the start using map() function
let num = [11,22,33,44,55,66,77,88,99]
let a3 = num.map(function(el,index,arr){
    return '@' + el
})
console.log(a3)

// filter() function is same as map() function
// add all numbers in an array
let numb = [1,9,3,7,5,9,8]
let total = 0
for(let i = 0; i < numb.length; i++){
    total = total + numb[i]
}
console.log(total)

// array destruction
let arr = [1, 2, 3, 4, 5]
let [aa,aa1,aa2,aa3,aa4] = arr
console.log(aa3)

// class
class name{
    fn = "atharv"
    ln = "penter"
    age = 23
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let ap = new name()
console.log(ap)
ap.fn="anjali"
console.log(ap)

// lexical scope
function addA(){
    s = 2
    s1 = 4
    console.log(s+s1)
    function addB(){
        s2 = 6
        s3 = 8
        console.log(s+s1+s2+s3)
        function addC(){
            s4 = 10
            console.log(s+s1+s2+s3+s4)
        }
        addC()
    }
    addB()
}
addA()

// declerations
// function decleration
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

// promises
let p = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("Hello")
    }else{
        reject("Bye")
    }
})
p.then(function(str){
    console.log(str)
},function(str){
    console.log(str)
})

// using catch in promises
let p1 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("Hello")
    }else{
        reject("Bye")
    }
})
p1.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// using then, catch, finally in promises
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







