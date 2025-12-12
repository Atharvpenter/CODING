let headOne = document.querySelector('h1')
let input = document.querySelector('input')
let buttonOne = document.querySelector('button')
buttonOne.addEventListener('click',function(){
    let colorText = input.value
    headOne.style.color= colorText
    input.value=""
})