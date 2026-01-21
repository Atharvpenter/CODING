// if there are too many repeatations in the program then we use function to avoid the repeatations
function cal(x,y){
    console.log(x+y)
    console.log(x-y)
    console.log(x*y)
    console.log(x/y)
}
cal(9,4)

// string
let a = "atharv"
console.log(typeof(a))

// basic methods in js are
// push(), pop(), unshift(), shift()
let a1 = ["atharv","shreyash","Om","kunak"]
z = a1.push("Ram")
console.log(a1)

// pop()
z2 = a1.pop()
console.log(a1)

// unshift()
z3 = a1.unshift("Ram")
console.log(a1)

// shift()
z4 = a1.shift()
console.log(a1)

// using switch cases
let city = "Pune"
switch(city){
    case "Pune":
        console.log("MH")
    case "Gandhinagar":
        console.log("GJ")
    case "Jaipur":
        console.log("RJ")
    default:
        console.log("Incorrect city name .......")
}

// using break statement in swwitch case
let city1 = "Gandhinagar"
switch(city1){
    case "Pune":
        console.log("MH")
        break
    case "Gandhinagar":
        console.log("GJ")
        break
    case "Jaipur":
        console.log("RJ")
        break
    default:
        console.log("Incorrect city name .......")
}

// using loops in js
// print table of 2
for(let i = 2; i <= 20; i = i + 2)
    console.log(i)

// print table of 2 in reverse
for(let i1 = 20; i1 > 2; i1 = i1 - 2){
    console.log(i1)
}

// using break and continue statement in loops
// print 1 to 10 upto 5
for(let i = 1; i <= 10; i++){
    if(i == 6){
        break
    }
    console.log(i)
}

// print 1 to 10 except 5
for(let i = 1; i <= 10; i++){
    if(i == 5){
        continue
    }
    console.log(i)
}

// print age using for loops
by = [1999,2000,2001,2002,2003,2004,2005,2006]
age = []
for(let i = 0; i < by.length; i++){
    a = 2025 - by[i]
    age.push(a)
    console.log(age)
}

// Map() function
// using map() = map(function(el,arr,index))
// print age using map() function
birthyear = [1999,2000,2001,2002,2003,2004,2005,2006]
ages = birthyear.map(function(el,arr,index){
    return 2025 - el
})
console.log(ages)

// add @ in the start of any elements
num = [11,22,33,44,55,66]
let aa = num.map(function(el,index,arr){
    return '@' + el
})
console.log(aa)

// filter() function is same as map() functions
// print all numbers total using filter() function
let numb = [1,9,3,7,5,9,8]
let total = 0
for(let i = 0; i < numb.length; i++){
    total = total + numb[i]
}
console.log(total)

// array destruction
let arr = [1 ,2, 3, 4, 5]
let [aa1 , a2, a3, a4, a5] = arr
console.log(a4)
console.log(aa1)
console.log(a5)

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
// function decleration
// 1. function decleration
function add(){
    console.log(2+8)
}
add()

// 2. function expression
let add1 = function(x,y){
    return x + y
}
add1(2,8)

// 3. Arrow function
let add2 = (x,y) => {
    return x + y
}
add2(8,4)

// promises
// Using .then
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
},function(str){
    console.log(str)
})

// using .then and catch
let p1 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
p1.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// using .then, .catch, .finally
let p2 =  new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
p2.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(str){
    console.log(" I will always execute")
})