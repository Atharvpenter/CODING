let ullist = document.querySelector('ul')
let inputElement = document.querySelector('input')
let buttonA = document.querySelector('button')
buttonA = addEventListener('click',function(){
    let text = inputElement.value
    let newElement = document.createElement('li')
    newElement.textContent = text
    ullist.appendChild(newElement)
    inputElement.value=""
})