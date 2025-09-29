// What is short Circuit in React.js ?
// a short-circuit is a quick way to conditionally render elements using JavaScript logical.
// AND(&&) or OR(||) operators instead of writing a full if-else or ternary expression.



// Short Circuit for AND(&&) Operators ------>
let a = 2 > 1 && 'Hello'
console.log(a)

let a1 = 1 > 2 && 'Wrong'   // if the condition is not right it will give false as o/p.
console.log(a1)

let a2 = 8 && 'Bye'
console.log(a2)

let a3 = "" && "Over"
console.log(a3)


// Short Circuit for OR(||) Operators ------>
let a4 = 8 || 7 > 3   // In this condition single left element is printed.
console.log(a4)

let a8 = 1 > 5 || 6   // In this condition single right element is printed.
console.log(a8)

let a5 = 2 > 5 || 3 < 8   // If both conditions are true it give True.
console.log(a5)

let a6 = 1 < 4 || 2 > 9   // Single condition is true then all will be true.
console.log(a6)

let a7 = 5 < 1 || 1 > 8   // If both conditions are false it give false.
console.log(a7)

let q75 = null ?? 10
console.log(q75)