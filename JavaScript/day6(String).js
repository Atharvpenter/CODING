// What is String?
// something which is written in quotes is a string.
// It is a sequence of character used to represent text.
// any element in single quote'', double quote "", reverse quote`` is a String.

let a = 'atharv'
console.log(a)
console.log(typeof a)

//number + number --> number
//string + number --> string
//number + string --> string
//string + string --> string

//Program ------->
let b = 10
let c = 20
let d = 'hello'
console.log(b+c+d)
//10+20+hello
//30hello

//Program-->
let ap = 40
let pa = 10
let q = 'hello'
console.log(q+ap+pa)
//hello+40+10
//hello4010

//String concat ->
let firstName = "atharv"
let lastName = "penter"
// i want to make it like my firstname is atharv and lastname is penter.
console.log("my firstname is "+firstName+" and lastName is "+lastName)
console.log(`My firstName is ${firstName} and My lastName is ${lastName}`)

// Does String stores it value by index?
let city = "pune"
console.log(city[0])  //p
// Yes string stores value by index.

// Methods of String ----->
//toUpperCase() is used to Capital all letters in array.
//toLowerCase() is used to Lower all letters in array.
//startswith() is used to check if element starts with specific letter.
//Endswith() is used to check if element ends with specific letter.
//trim() is used to remove spaces between array.
//trimstart() is used to remove elements from the right side.
//trimEnd() is used to remove elements from left side.
//Replace() is used to an element in array with new arrat element.
//split() is used to split elements in array.
//repeat() is used to repeat a particular array.
//reverse() is used to reverse all elements in array.




//program for toUppercase()->
let city1 = "pune"
let fn = city1.toUpperCase()
console.log(fn)

//Program for lowercase()->
let fn1 = city1.toLowerCase()
console.log(fn1)

//Program for startswith()->
let fn2 = city1.startsWith('p')
console.log(fn2)

//Program for endswith()->
let f3 = city1.endsWith('e')
console.log(f3)

//Prgram for trim()->
let city2 = " goa "
console.log(city2.trim())

//Program for trimStart()->
console.log(city2.trimStart())

//Program for trimEnd()->
console.log(city2.trimEnd())

//Program for replace()->
let name = "My name is atharv penter graduated bachelor"
console.log(name.replace("atharv", "penter"))

//Program for split()->
let name1 = "atharvpenter@gmail.com"
console.log(name.split('@'))

//Program for repeat()->
let name2 = "atharv"
console.log(name2.repeat(3))






