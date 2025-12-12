// string
let a = "atharv"
console.log(a)

// in js to reduce repeatation we used function
function cal(x,y){
    console.log(x + y)
        console.log(x - y)
}
cal(7,9)

// object
let a1 = ["atharv","ram"]
console.log(a1)

// basic methods in js
// push()
// pop()
// unshift()
// shif()

let a2 = ["atharv","ram","sham","Madhur"]
b = a2.push("DON")
console.log(a2)

b1 = a2.pop()
console.log(b1)
console.log(a2)

b2 = a2.unshift("DON")
console.log(a2)

b3 = a2.shift()
console.log(a2)

// switch case
let city = "pune"
switch(city){
    case "pune":
        console.log("MH")
    case "mumbai":
        console.log("MH")
    case "gandhinagar":
        console.log("MH")
    default:
        console.log("Invalid city name.....")
}

// switch case using break and continue
let city1 = "pune"
switch(city1){
    case "pune":
        console.log("MH")
        break
    case "mumbai":
        console.log("MH")
        break
    case "gandhinagar":
        console.log("MH")
        break
    default:
        console.log("Invalid city name.....")
}

// using loops 
// print table of 2 
for(let i = 2; i <= 20; i = i + 2){
    console.log(i)
}

// print it in reverse
for(let i = 20; i >= 2; i = i - 2){
    console.log(i)
}

// using break and continue statement
for(let i = 1; i <= 9; i++){
    if(i == 5){
        break
    }
    console.log(i)
}

for(let i = 1; i <= 9; i++){
    if(i == 5){
        continue
    }
    console.log(i)
}

// print age 
byear = [1999,2000,2001,2002,2003,2004,2005]
age = []
for(let i = 0; i < byear.length; i++){
    a = 2025 - byear[i]
    age.push(a)
    console.log(age)
}

// map() -> map(function(el,index,arr))
let byear1 = [1999,2000,2001,2002,2003,2004,2005]
let age1 = byear1.map(function(el,index,arr){
    return 2025 - el
})
console.log(age1)

