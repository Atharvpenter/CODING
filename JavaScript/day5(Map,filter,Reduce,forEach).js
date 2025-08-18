//Calculate Birthyears---->
let birthyear = [2000,2001,2003,2004]
let ages = []
for(let i = 0; i < birthyear.length; i++){
    a = 2025 - birthyear[i]
    ages.push(a)
    console.log(ages)
}

//Using Map() function------>
//Map() has functions with 3 parameters which are [el,index,array]
//Maps function is used as --> arrayname.map(function(el,index,arr))
//print $ at the start of an array using map functions---->
let arr = [11,22,33,44,55]
let b = arr.map(function(el,index,arr){
    return '@' + el
})
console.log(b)

//calculate age using map function->
let byear = [2000,2001,2002,2003]
let c = byear.map(function(el,index,arr){
    return 2025 - el
})
console.log(c)


//Using filter() function ----->
//filter function is same as map functions
//check greater than 75
let num = [100,74,12,77,98,36,85,98,77]
let n = num.filter(function(el,index,arr){
    return el > 75
})
console.log(n)

//bank balance
let transcation = [77,45,1,-8,-70,100]
let deposit = transcation.filter(function(el){
    return el > 0
})
console.log(deposit)
let withdrawl = transcation.filter(function(el){
    return el < 0
})
console.log(withdrawl)


//add all elements in the array
let numbers = [33,99,88]
let total = 0
for(let i = 0; i < numbers.length; i++){
    total = total + numbers[i]
}
console.log(total)

//Using Reduce() function --->
//Reduce funtion is used as -> arrayname.reduce(function(accumulator,el,index,arr))
let q = numbers.reduce(function(acc,el,index,arr){
    return acc + el
})
console.log(q)

//Using forEach function--->
//Used to apply to array elements
//ForEach function is used as -> arrayname.forEach(function(el,index,arr))
let cities = ["Pune","mumbai","Sangamner","Nashik"]
let ab = cities.forEach(function(el,index,arr){
    console.log('Welcome ' + el)
})

//print 1 at every starting elements in the array
let w = ["art","Science","IT","Mathematics"]
let r = w.forEach(function(el,index,arr){
    console.log('1. ' + el)
})


//Using flat() function ---->
//adds all multiple array in single array
let city = [["pune","mumbai"],["Udaipur","jaipur"],["sangamner","nashik"]]
let ac = city.flat()
    console.log(ac)


//Using slice() function ---->
//It is used to remove or extract array from start index to end index
//Slice function is used as -> arrayname.slice(startIndex,endIndex(which is not include))
//Program -->
//index        0   1   2   3   4   5   6   7
let number = [ 1 , 4 , 3 , 5 , 6 , 7 , 8 , 5]
//index       -7  -6  -5  -4  -3  -2  -1   0
let v = number.slice(2)
console.log(v)
console.log(number.slice(-7,6))
console.log(number.slice(-6,-5))
