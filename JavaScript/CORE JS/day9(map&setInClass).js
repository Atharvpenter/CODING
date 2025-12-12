//Map() can be define with,
//map() does not store duplicate values
//with values
//program-->
let mapA = new Map(
    [
        [1,'admin'],
        [2,'manager'],
        [3,'customer'],
        [4,'tutor'],
        [true,'other']

    ]
)
console.log(mapA)
console.log(mapA.size)


//without values
//program-->
let mapB = new Map()
mapB.set([11,2,33],'marks')
mapB.set({fn:'atharv', ln:'penter'},'info')
console.log(mapB)

//Map() has different methods in it,
//clear,delete,get

//program-->
let mapc = new Map(
    [
         [1,'admin'],
        [2,'manager'],
        [3,'customer'],
        [4,'tutor'],
        [true,'other']
    ]
)
//mapc.clear()
//console.log(mapc)

mapc.delete(2)
console.log(mapc)

//Set is same as map in class
let setA = new Set()
console.log(setA)
setA.add(11)
setA.add(12)
setA.add(13)
setA.add(14)
console.log(setA)