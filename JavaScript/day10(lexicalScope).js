function additionA(){
    let a  = 10 
    let b = 5
    console.log(a + b)
    function additionB(){
        let s = 6
        let t  = 8
        console.log(a + b + s + t)
        function additionC(){
            let h = 9
            console.log(a+b+s+t+h)
        }
        additionC()
    }
    additionB()
}
additionA()
