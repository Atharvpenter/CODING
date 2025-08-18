//check which is greater
let a = 19
let b = 10
if(a>b){
    console.log("a is Greater")
}
else{
    console.log("b is greater")
}

//Using of switch Case()
//One input and multiple outcomes----->
//program 1 -->
//without using break statements.
let city = "Indore"
switch(city){
    case "pune":
        console.log("MH")
    case "Indore":
        console.log("MP")
    case "jaipur":
        console.log("RJ")
    default:
        console.log("incorrect city name ..")
}

//Program 2 -->
//with break statements
let city1 = "pune"
switch(city1){
    case "pune":
        console.log("MH")
        break
    case "Jaipur":
        console.log("RJ")
        break
    case "GandhiNagar":
        console.log("GJ")
        break
        default:
            console.log("Incorrect city name.")
}

//Multiple inputs and one outcomes------>
//Program 3 ->
let city3 = "Udaipur"
switch(city3){
    case "pune":
    case "mumbai":
        console.log("MH")
        break
        case "Jaipur":
        case "Udaipur":
            console.log("RJ")
            break
            case "Gandhinagar":
                case "zxy":
                    console.log("GJ")
                    break
                    default:
                        console.log("incorrect city.")
}