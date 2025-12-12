// Resolve , Reject
// Program 1 ->
// Using resolve,reject,then

let p = new Promise(function(resolve,reject){
    let a = 10
    let b = 10
    if(a == b){
        resolve("Hello")
    }
    else{
        reject("Bye")
    }
})
p.then(function(str){
    console.log(str)
},function(str){
    console.log(str)
})

// Program 2 ->
// Using resolve,reject,then,catch

let p1 = new Promise(function(resolve,reject){
    let a1 = 10
    let b1 = 10
    if(a1 == b1){
        resolve("Hello")
    }
    else{
        reject("Bye")
    }
})
p1.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})

// Program 3 ->
// Using resolve,reject,then,catch,finally

let p2 = new Promise(function(resolve,reject){
    let a2 = 10
    let b2 = 10
    if(a2 == b2){
        resolve("hello")
    }
    else{
        reject("Bye")
    }
})
p2.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(){
    console.log("I will always execute....")
})