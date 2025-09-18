// Promises ->
function CreateUser(){
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
            resolve("Get If")
        },1000)
    })
}

async function getInfoUser() {
    let str = await createUser()
    console.log(str)
    let str2 = await getId()
    console.log(str2)
    let str3 = await getInfo()
    console.log(str3)

}
getInfoUser()
