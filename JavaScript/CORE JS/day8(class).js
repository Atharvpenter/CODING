//What is class?
//-> a class is blueprint for object.

//program->
class person{
    fn = undefined
    ln = undefined //properties
    displayName(){ //method
        console.log(this.fn + this.ln) //this=person
    }
}
let atharv = new person()
console.log(atharv)
atharv.fn = 'ram'
atharv.ln = 'seeta'
console.log(atharv)

atharv.displayName()

//Program-->
class student{
    fn = 'atharv'
    ln = 'penter'
    class = 10
    displayname(){
        print(this.fn + this.ln + this.class)
    }
}
let a = new student()
console.log(a)
atharv.fn = "ram"
atharv.ln = "seeta"
atharv.displayName()





