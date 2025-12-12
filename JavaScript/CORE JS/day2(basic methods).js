//Methods in javascript------->
//push() is used to add element at the last of array
//pop() is used to remove element from the last 
//unshift() is used to add element at the start
//shift() is used to remove element from the start
//include() is used to check if the element is present in the array & returns Boolean value
//reverse() is used to reverse all array
//join() is used to join two arrays
//indexOf() is used to find the index of array
//Concat() is used to join two arrays





//Program 1 --->
//using push()
let names = ["atharv","Aditya","shivam","shreyas"]
console.log(names)
console.log(names.length)
console.log(names[3])
let a = names.push("Om")
console.log(a)
console.log(names)

//Program 2 -->
//using pop()
let b = names.pop()
console.log(b)
console.log(names)

//Program 3 -->
//using unshift()
let c = names.unshift("Pranav")
console.log(c)
console.log(names)

//Program 4 -->
//using shift()
let d = names.shift()
console.log(d)
console.log(names)

//Program 5 -->
//using include() which returns true as its boolean value
let e = names.includes("shivam")
console.log(e)

//program 6 -->
//using include() which returns False as its boolean value
let f =  names.includes("Ram")
console.log(f)

//Prpgram 7 -->
//using reverse()
let g = names.reverse()
console.log(g)

//Program 8 -->
//using indexOF()
let h = names.indexOf("shivam")
console.log(h)

//Program 9 -->
let i = [11,22,33]
let j = [44,55,66]
let k = i.concat(j)
console.log(k)