//Using FOR Loops with break statements-------->
//Print 1 to 5
for(let i=1; i<=5;i++){
    console.log(i)
}

//print in reverse
for(let i2=5;i2>=1;i2--){
    console.log(i2)
}

//print table of 5
for(let i3 = 5; i3 <= 50; i3 = i3 + 5){
    console.log(i3)
}

//print table of 5 in reverse
for(let i4=50; i4 >= 5; i4 = i4 - 5){
    console.log(i4)
}

//Using break statements in for loop ---->
//Using console.log before if statement
for(let i5 = 1; i5 <= 5; i5++){
    console.log(i5)
    if(i5 == 3){
        break
    }
}

//Using if statement before console.log
for(let i6=1; i6<=5; i6++){
    if(i6==4){
        break
    }
        console.log(i6)
}

//print 1 to 10 in reverse
for(let i7=10; i7>=1; i7 = i7 -1){
    if(i7 == 5){
        break
    }
    console.log(i7)
}

//Using for() loops with continue statements----->
//print 1 to 5
for(let i8=1; i8<=5;i8++){
    if(i8 == 3){
        continue
    }
    console.log(i8)
}

//print table of 5 without 25
for(let i9=5; i9<=50;i9=i9+5){
    if(i9==25){
        continue
    }
    console.log(i9)
}