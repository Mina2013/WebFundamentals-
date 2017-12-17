
function behappy(num)
{
    for (num=0; num<= 98; num++){
        console.log("Good Morning!");
    }
}   
behappy(98);

count =-300
for(var i=-300; i<0; i++){
    if (i%!3==0){
        count++;
    }
    if (i ===-3){
        break;
    }
    if (i===-6){
        break;
    }
    console.log(i)
}

var num= 2000;
while(num<5281){
    console.log(num);
//     num=num+1;
// }
function birthday(x,y){
    if (x==04 && y==26){
        console.log("how did you know?");
    }
    else{
    console.log("just another day...");
}
}
birthday(03,12)

function leap(year){
    if (year%!4==0){
        console.log("this is leap year");
    }
    if(year%!100==0){
        console.log("this is not leap yeat");
    }
}
leap(2002);
var num = 512;
count =0
for (var num=512; num< 4096; num++){
    if (num % 5 === 0){
        console.log(num);
        num++;
        count++;
    }
}
console.log("the sum is:", count);

for (var num=6; num< 60000; num++){
    while (num % 6 === 0){
        console.log(num);
        num++;
        }
}
print 1-10 and dojo

for (var num= 1; num<100; num++){
     if (num % 5 === 0){
       console.log("Coding",num);
      //   num++;
      }
        if (num % 10 ===0 && num % 5 ===0){
         console.log("Dojo", num);
        }
     }

all numbers form -300k-300k and the sum
count= 0
for (var num= -300000; num <300000; num++){
     if (num % 2 === 0){
       console.log(num);
         num++;
        count= count+num;         
      }
   }
     console.log("the sum is", count);

arr=[10]
newarr=[]
for (var i = arr ; i >=0; i--){
    //if (i >=0){
       //console.log(i);
       newarr.push(i);
       
    }


         console.log(newarr);

//}
        
arr=[1,2]
console.log(arr[0]);
return arr[1];
arr = ["hello",1,2,3]
sum = 0
for (var i=0; i<= arr.length; i++){
    sum = sum+arr[0];
    //console.log(sum);
    //console.log(arr.length)
}
console.log(sum);
console.log(arr.length);

x=[1,3,5,7,9,13]

function greatervalues(arr){
    var newarr=[]
for (var i=0; i<=arr.length; i++){
    if (arr[i]>arr[2]){
        //console.log([i]);
        i++
      }
      //console.log(newarr)
}

console.log([newarr])
}
greatervalues([1,3,5,7,9,13])
console.log(newarr);

//program to pass num to arr
passingnums(1,3);
function createArr(num1, num2) {
    var newArr = [];
    if(num1 === num2) {
        console.log("jinx!");
    }
    for(var i = 0; i < num1; i++) {
        newArr.push(num2);
    }
    console.log(newArr);
    return newArr;
}

createArr(3, 10);

function firstvalue(arr) {
    var newArr = [];
    if(arr[0]>arr.length){
        console.log("Too big");
    }
    if(arr[0]<arr.length){
        console.log("Too small");
    }
    if (arr[0]===arr.length){
        console.log("Just Right!");
    }
}
firstvalue([2,1]);

convert from farenheight to degrees

function fahrenheitToCelsius(fahrenheit){
  
    Celsius = (fahrenheit-32)*0.5556;
   //for (Celsius=0; Celsius<=fahrenheit;Celsius++);
    console.log("the temperatur in Celsius is:",Celsius);

}
 fahrenheitToCelsius(80);

convert temperatures
function fahrenheitToCelsius(celsius){
    
    fahrenheit= (celsius*1.8)+32;
     //for (Celsius=0; Celsius<=fahrenheit;Celsius++);
      console.log("the temperatur in fahrenheit:", fahrenheit);
  
  }
  fahrenheitToCelsius(6);