// Print table of 2 using for loop --->
for (let i = 2; i <= 20; i = i + 2)
    console.log(i)

// Print table of 2 in reverse using for loop --->
for (let i2 = 20; i2 >= 2; i2 = i2 - 2)
    console.log(i2)

// Print numbers upto 10 using break statement --->
for (let i3 = 1; i3 <= 5; i3++) {
    console.log(i3)
    if (i3 == 3) {
        break
    }
}

// Print numbers upto 10 using break statement --->
for (let i4 = 1; i4 <= 10; i4++) {
    if (i4 == 5) {
        break
    }
    console.log(i4)
}

// Print numbers upto 6 using continue statement --->
for (let i5 = 1; i5 <= 6; i5++) {
    if (i5 == 4) {
        continue
    }
    console.log(i5)
}

// String --> ''
a = 'atharv'
console.log(a)
console.log(typeof (a))

// Array ---> []
let names = ['atharv', 'penter']
console.log(names)
console.log(typeof (names))

// Oject --->
let info = {
    'fn': 'atharv',
    'ln': 'penter'
}
console.log(info)
console.log(typeof (info))

// switch cases ---->
// Check greater number
n = 10;
m = 9;
if (n < m) {
    console.log("n is greater...")
}
else {
    console.log("m is greater")
}

// Case 1 ----------------->
let city = "Indore"
switch (city) {
    case "Pune":
        console.log("MH")
    case "Indore":
        console.log("GJ")
    default:
        console.log("incorrect city name ....")
}

// Case 2 -----------------> Using break statement.
let city1 = "indore"
switch (city1) {
    case "pune":
        console.log("MH")
        break;
    case "indore":
        console.log("GJ")
        break;
    default:
        console.log("Incorrect city name ...")
}

// Case 3 ------------->>>> Multiple inputs and single output
let city2 = "pune"
switch (city2) {
    case "pune":
    case "mumbai":
        console.log("MH")
        break;
    case "Jaipur":
    case "rajkot":
        console.log("RJ")
        break;
    default:
        console.log("Incorrect city name.....")
}