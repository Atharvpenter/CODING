// What is Spread and Rest Operators ?
// both use the same syntax (...)
// Spread Operators -> is used to expand an array or object into individual elements.
// Rest Operators ----> is used to collect the rest of the items into an array.

// [1,2,3,4] -> 1,2,3,4 ------> Spread Operators.
// 1,2,3,4 -> [1,2,3,4] ------> Rest Operators.

function addAll(...a){
    console.log(a)
    return a.reduce(function(acc,el){
        return acc + el
    },0)
}
let q33 = addAll(12,3,4,5,6,7,8,9,9,4) // rest operator
console.log(q33)

let cities = ["pune","mumbai","banglore","kolkata"] // Spread operator
function printFirstTwo(a,b){
    console.log(a,b)
}   
printFirstTwo(...cities)

let names = ["atharv","Kshitij","Ranvir"]
function printFirstTwo1(a,b,c){
    console.log(a,b,c)
}
printFirstTwo1(...names)

// ----------
let a = [11,22,33]
let a1 = [44,55,66]
let b = [...a,...a1]
console.log(b)

let c = a.concat(a1)
console.log(c)

// ------------------
let info = {
    fn : "atharv",
    ln : "penter"
}

let info1 = {
    city : "pune",
    language : "Marathi"
}

let a3 = {...info , ...info1}
console.log(a3)

let names1 = ["chinmay","sarika","poorva","ram"]
let [a11,...b11]= names1
console.log(a11)
console.log(b11)