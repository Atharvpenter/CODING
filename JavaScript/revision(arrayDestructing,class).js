// Array destructing
let num = [1, 2, 3]
let alpha = [a, b, c] = num
console.log(b)
console.log(a)

// class
let info = {
    'firstname': 'atharv',
    'lastname': 'penter',
    'age': 22
}
let { 'firstname': fn, 'lastname': ln, age: age } = info
console.log(ln)

let info1 = {
    student1: {
        fn: "atharv",
        ln: "penter",
        age: 21
    },
    student2:{
        fn:"shreyas",
        ln:"dhole",
        age:22
    }
}
let {student1:{fn:fn1, ln:ln1, age:age1},student2:{fn:fn2, ln:ln2, age:age2}} = info1
console.log(fn1)
console.log(age2)
console.log(ln2)

// Class --------->
class person{
    fn = undefined
    ln = undefined
    displayname(){
        console.log(this.fn + this.ln)
    }
}
let atharv = new person()
atharv.fn = 'atharv'
atharv.ln = 'penter'
console.log(fn)