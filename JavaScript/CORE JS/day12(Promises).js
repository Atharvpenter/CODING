// What is Promises -> 
// Is an object that represents the eventual completion of an asynchronous operation.
// Types ->
// Synchronous -> Code executes line by line, one after another.
// Asynchronous -> Code that tasks don’t block the execution of the program.

// Program ->
// Async
function getInfo(){
    setTimeout(function(){
        console.log("User Created")
    },3000)
    setTimeout(function(){
        console.log("Get Info")
    },2000)
    setTimeout(function(){
        console.log("Get Id")
    },1000)
}
getInfo()

// Simple way to do it ->
function GetInfo(){
    setTimeout(function(){
        console.log("User Created")
        setTimeout(function(){
            console.log("Get Info")
            setTimeout(function(){
                console.log("Get Id")
            },3000)
        },2000)
    },1000)
}
GetInfo()