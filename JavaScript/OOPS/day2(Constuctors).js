// Constructors in Oops in js ?
// it is automatically called when new object is created using keyword NEW.

// Program 1 -->
class Person{
    constructor(fn,ln){
    fn = undefined
    ln = undefined
    }
    displayName(){
        console.log(this.fn + this.ln)
    }
}
atharv1 = new Person("amol","rao")
pp1 = new Person("aa0","bb1")
console.log(atharv1)
console.log(pp1)
pp1.displayName()