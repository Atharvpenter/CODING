// If there is too many repeatations in the code in js we use function to stop the repeatations
function cal(x,y){
    console.log(x+y)
    console.log(x-y)
}
cal(8,1)

// string
a = "string"
console.log(typeof(a))

// to check length of array we use
a1 = ["atharv","atharva","Kunal","tanish"]
console.log(a1.length)

// basic methods in js
// push() -> adds new element in the last
b = a1.push("akhil")
console.log(a1)

// pop() -> removes last element
b1 = a1.pop()
console.log(a1)

// unshift() -> adds new element in the start
b2 = a1.unshift("akhil")
console.log(a1)

// shift() -> removes starting element
b3 = a1.shift()
console.log(a1)

// using switch cases ->
let city = "pune"
switch(city){
    case "pune":
        console.log("MH")
    case "banglore":
        console.log("HY")
    default:
        console.log("Invalid cityname")
}

// using break statement in the switch case
let city1 = "pune"
switch(city1){
    case "pune":
        console.log("MH")
        break
    case "banglore":
        console.log("HY")
        break
    default:
        console.log("Invalid cityname")
}

// loops in js
// print table of 2
for(let i = 2; i <= 20; i = i + 2){
    console.log(i)
}

// print it in reverse
for(let i = 20; i >= 2; i = i - 2){
    console.log(i)
}

// using break and continue statements in loops
// print 1 to 9 upto 7
for(let i = 1; i <= 9; i++){
    if(i == 8){
        break
    }
    console.log(i)
}

// print 1 to 9 except 7
for(let i = 1; i <= 9; i++){
    if(i == 7){
        continue
    }
    console.log(i)
}

// print age using for loops
by = [1999,2002,2004,2006,2007]
ag = []
for(let i = 0; i <= by.length; i++){
    a = 2025 - by[i]
    ag.push(a)
    console.log(ag)
}

// using map() function
byear = [1999,2002,2004,2006,2007]
age = byear.map(function(el,index,arr){
    return 2025 - el
})
console.log(age)

// filter() funciton is same as the map()
// array destructing
let arr = [11,22,33,44]
console.log(arr)
let [c1 , c2, c3, c4] = arr
console.log(c3)

// class
class person{
    "fn"="atharv"
    "ln"="penter"
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let ap = new person()
console.log(ap)
console.log(typeof(ap))

// declearations ->
// 1.function declerations
function add(){
    console.log(1+5)
}
add()

// function expression
function adds(x,y){
    console.log(x + y)
    console.log(x - y)
}
adds(8,7)

// Arrow function
let add2 = (x,y) => {
    return x + y
}
add2(4,9)

// promises
let p = new Promise(function(resolve,reject){
    let q = 10
    let q1 = 10
    if(q == q1){
        resolve("hello")
    }else{
        reject("bye")
    }
})
p.then(function(str){
    console.log(str)
},function(str){
    console.log(str)
})

