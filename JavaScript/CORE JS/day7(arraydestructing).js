//array destructing is used to remove array values from array.
let num = [1,2,3]
console.log(num)
let [a , b, c] = num
console.log(a)

//Program -->
let names = ["atharv","om","shreyash","shivam"]
let [ a1 , b1 , c1 , d1 ] = names
console.log(b1)

//program--->
let name = [["atharv","Shivam"],["aditya","om"],["shreyas","pranav"]]
let [a2 , b2 , c2] = name
console.log(c2)
console.log(a2)

//program creating variables -->
let info = {
    firstname : "atharv",
    lastname : "penter",
    age : 21
}
let {firstname : fn, lastname : ln, age:age} = info
console.log(fn)
console.log(age)

//Program 2 -->
let info1 = {
    student1:{
    fn : "atharv",
    ln : "penter",
    age : 21
    },
    student2 :{
        fn1 : "shivam",
        ln2 : "More",
        age : 22
    }
}
let {student1 :{fn:f1, ln:l1,age:age1},student2 :{fn1:f2, ln2:l2,age:age2}} = info1
console.log(fn)
console.log(age2)
console.log(l2)