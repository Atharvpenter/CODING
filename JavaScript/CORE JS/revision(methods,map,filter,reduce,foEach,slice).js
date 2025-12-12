// Basic methods in js ---------->
// pop(),push(),shift(),unshift(),include(),reverse(),indexof()
// Pop() removes last element
// push() adds new element to last
// unshift() adds new element at the start
// shift() removes start element
// reverse() used to reverse the string
// indexOf() checks the index in string

let name = ['atharv','shreyash','om','shivam']
i = name.pop()
console.log(i)
console.log(name)

i2 = name.push('ram')
console.log(name)

i3 = name.shift()
console.log(name)

i4 = name.unshift('Krishna')
console.log(name)

i6 = name.reverse()
console.log(name)

i7 = name.indexOf('ram')
console.log(i7)

// Calculate age
byear = [1999,1952,1974,1973]
ages = []
for(let i = 0; i < byear.length; i++){
    a = 2025 - byear[i]
    ages.push(a)
    console.log(ages)
}

// Map = function(el,index,arr)
// print byear using map function --------->
byear1 = [2000,2001,2002,2003]
let a1 = byear1.map(function(el,index,arr){
    return 2025 - el
})
console.log(a1)

// filter = fucntion(el,index,arr)
let num = [70,88,49,22,87,26,21,40,77,99]
let n = num.filter(function(el,index,arr){
    return el > 70
})
console.log(n)

// reduce = function(acc,el,index,arr)
let num1 = [70,88,49,22,87,26,21,40,77,99]  //add all element
let aa = num1.reduce(function(acc,el,index,arr){
    return acc + el
})
console.log(aa)

// add all element in the array ----------->
let number = [15,15,15]
let total = 0
for(let i22 = 0; i22 < number.length; i22++){
    total = total + number[i]
}
console.log(total)

// forEach()
let names = ['atharv','Siva','shivam']
e = names.forEach(function(el,index,arr){
    console.log('welcome ' + el)
})

// slice()
let ab = [1,2,3,4,5,6,7,8,9]
console.log(ab.slice(0,3))
console.log(ab.slice(2,6))