let heading = document.querySelector('h1')
let inputA = document.querySelector('input')
let buttonA = document.querySelector('button')
buttonA = addEventListener('click',function(){
    let colorText = inputA.value
    heading.style.color = colorText
    input.value = ""
})