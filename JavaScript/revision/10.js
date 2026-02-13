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
