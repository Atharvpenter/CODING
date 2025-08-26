// Setter ----> Used to update a property.
// getter ----> Used to access a property.

// Program for setter and getter --->
class Person{
    setFn(fn){
        this.firstname = fn
    }
    setLn(ln){
        this.lastname = ln
    }
    getFn(){
        return this.firstname
    }
}
atharv1 = new Person()
atharv1.setFn = "atharv"
atharv1.setLn = "Penter"
console.log(atharv1)