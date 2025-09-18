// Program -->
function createUser(){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            resolve("User Created")
        },3000)
    })
}
function GetInfo(){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            resolve("Get Info")
        },2000)
    })
}
function GetId(){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            resolve("Get Id")
        },1000)
    })
}
createUser()
.then(function(str){
    console.log(str)
    return(GetInfo)
})
.then(function(str){
    console.log(str)
    return(GetId)
})
.then(function(str){
    console.log(str)
})
.catch(function(str){
    console.log(str)
})
.finally(function(str){
    console.log("I will always exceuted....")
})