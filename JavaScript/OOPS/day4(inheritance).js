// Inheritance is used in oops using EXTEND keyword inside class


// Single-Level Iheritance------->
// program --->
// class Student{
//     fn = "atharv"
//     ln = "penter"
//     age = 22
// displayName(){
//     console.log(this.fn + this.ln)
// }
// }
// class teacher extends Student{
//     sal = 10000
// }

// let ap = new teacher()
// console.log(ap.fn)
// console.log(ap.ln)
// console.log(ap.age)
// console.log(ap.sal)
// ap.displayName()

// Program 2 ----> same as program 1 but added constructor in class
class Student{
    constructor(fn,ln,age){
    fn = "atharv"
    ln = "penter"
    age = 22
    }
displayName(){
    console.log(this.fn + this.ln)
}
}
class teacher extends Student{
    sal = 10000
}

let ap = new teacher()
console.log(ap.fn)
console.log(ap.ln)
console.log(ap.age)
console.log(ap.sal)
ap.displayName()