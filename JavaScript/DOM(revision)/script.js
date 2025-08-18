let headone = document.querySelector('h1')
let buttonOne = document.querySelector('button')
buttonOne.addEventListener('click',function(){
    headone.style.color= "orange";
    headone.addEventListener('dblclick',function(){
        headone.style.color = "blue";
    })
})
headone.addEventListener('mouseover',function(){
    headone.style.color = "red";
})
headone.addEventListener('mouseout',function(){
    headone.style.color ="yellow";
})
buttonOne.addEventListener('click',function(){
    window.location.reload();
})