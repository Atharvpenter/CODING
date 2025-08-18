// How to define string
//Anything inside quotes is a string.
let a = "atharv"
console.log(a)
console.log(typeof a)

//Array destructing is is used to remove array value from array
// Used separate elements for arrays.
let a1 = [11,22,33]
let [a11,b11,c11] = a1
console.log(b11)

// Class is a blueprint of objects.
class Person{
    fn = undefined
    ln = undefined
    displayName(){
        console.log(this.fn + this.ln)
    }
}
let atharv = new Person()
console.log(atharv)
atharv.fn = 'atharv'
atharv.ln = 'penter' 
console.log(atharv)

//Using Map in class
//Map can be used with values and also without values.
let MapA = new Map(
    [
        [1,'admin'],
        [2, 'user'],
        [3, 'customer'],
        [true, 'other']
    ]
)
console.log(MapA)
console.log(MapA.size)

//without values.
//let mapB = new Map(
mapB.set([11,2,33],'marks')
//mapB.set({fn:'atharv', ln:'penter'},'info')
//console.log(mapB)

//set
