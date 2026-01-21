// in js if we want to reduce typing extra code we use function
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

// object
let a1 = ["atharv","kunal","akhil"]
console.log(typeof(a1))

// method in js
// push(), pop(), shift(), unshift()
let a2 = ["atharv","kunal","akhil","Om"]
b = a2.push("Ram")
console.log(a2)

b1 = a2.pop()
console.log(a2)

b2 = a2.unshift("Sham")
console.log(a2)

b3 = a2.shift()
console.log(a2)

// Using switch case 
let city = "pune"
switch(city){
    case "pune":
        console.log("MH")
    case "jaipur":
        console.log("RJ")
    case "surat":
        console.log("GJ")
    default:
        console.log("Invalid cityname ......")
}

// using break statement in switch case
let city1 = "jaipur"
switch(city1){
    case "pune":
        console.log("MH")
        break
    case "jaipur":
        console.log("RJ")
        break
    case "surat":
        console.log("GJ")
        break
    default:
        console.log("Invalid cityname ......")
}

// Using for loops
// print table of 7 using for loops
for(let i = 7; i <= 70; i = i + 7){
    console.log(i)
}

// print table of 7 in reverse
for(let i = 70; i >= 7; i = i - 7){
    console.log(i)
}

// Using break and continue statements in loops
// print 1 to 10 upto 7
for(let i = 1; i <= 7; i++){
    if(i==8){
        break
    }
    console.log(i)
}

// print 1 to 10 upto 7
for(let i = 1; i <= 7; i++){
    if(i == 7){
        continue
    }
    console.log(i)
}

// print age using for loops
birthyear = [1999,2000,2001,2002,2003,2004,2005,2006]
age = []
for(let i = 0; i < birthyear.length; i++){
    a = 2025 - birthyear[i]
    age.push(a)
    console.log(age)
}

// Using map() function
// map(function(el,index,arr))
// print age using map() function
by = [1999,2000,2001,2002,2003,2004,2005,2006]
age = by.map(function(el,index,arr){
    return 2025 - el
})
console.log(age)

// add @ in the start of the element
let num = [11,22,33,44,55]
let aaa = num.map(function(el,index,arr){
    return '@' + el
})
console.log(aaa)

// array destructing
let arr = [11,22,33,44]
let [r,t,y,u] = arr
console.log(t)

// promises
// using .then function
let p = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a=n){
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

// using .catch() function
let p1 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a=b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
p.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// using .finally
let p2 = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a=b){
        resolve("HELLO")
    }else{
        reject("BYE")
    }
})
p.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(str){
    console.log("I will always exceute")
})