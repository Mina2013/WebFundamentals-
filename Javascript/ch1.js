
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
replace negative nums with "big"
function posbig(arr){
    for (var i=0; i<arr.length; i++){
        if (arr[i]>0){
            arr[i]="big"
    }
   } {


   console.log(arr);
 }
posbig([-1,3,5,-5]);
 Create a function that takes array of numbers. The function should print
 the lowest value in the array, and return the highest value in the array.      
 function printreturn(arr){
     min= Math.min.apply(Math, arr)
     max= Math.max.apply(Math, arr)
    console.log(min);
    return max;   
 }    
  printreturn([-1,0,3])             
function smallbig(arr){
    min=0;
    for (var i=0; i<arr.length; i++){
         //console.log(arr[i]);
     }
     if(arr[i]<arr.length){
     }
    console.log([i]);
    console.log(arr);
    
}
smallbig([3,2,3])
Build a function that takes array of numbers.
the function should print second-to-last value in the array, and return first odd value in the array.
function secondtolast(arr){
  odd=[]
  for(var i=0; i<arr.length;i++){
       if (arr[i] % 2===1){
       odd.push(arr[i]);
       break;
       }
        }
  console.log(arr[arr.length-2]);
  console.log(odd);
}
secondtolast([3,8,20,6,1]);
****Wes's code */

function secondToLast2(arr) {
  console.log(arr[arr.length-2]);
  for(var i = 0; i < arr.length; i++) {
      if(arr[i] % 2 === 1) {
          console.log(arr[i]);
          return arr[i];
      }
  }
}
var test = [3, 4, 7, 10, 1092, 3, 44, 2];
console.log(secondToLast2(test))
**Given array, create a function to return a new array where each value in the original has been doubled.
***Calling double([1,2,3]) should return [2,4,6] without changing original.
function doublearr(arr){
 var newarr=[];
  for(var i =0; i<arr.length; i++){
   newarr.push(arr[i]*2);
   //return newarr;
       }
       return newarr;
     //console.log(newarr);
}
//doublearr([10,9,8]);
var test =[2,3,4];
console.log(doublearr(test));

Given array of numbers, create function to replace last value with number of positive values.
Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
function poppush(arr){
  count=0;
  for(var i =0; i<arr.length; i++){
   if (arr[i]>0){
        count= count+1;
        arr[arr.length-1]=count;
      } 
  }
     return arr;
}
//poppush([-1,1,1,1]);
 var test =[-1,1,1,1];
 console.log(poppush(test));

Create a function that accepts an array. Every time that array has three odd values in a row, 
print "That’s odd!" Every time the array has three evens in a row, print "Even more so!" 
function evenodd(arr){
  count=0;
  for(var i=0; i<arr.length; i++){
    if (arr[i]%2==1){
       count=count+1;
       if (count===3){
         console.log("that'a is odd", count);
       }
     } else if (arr[i]%2===0){
    count=count+1;
  if (count===3){
    console.log("that'a is odd", count);
}
}
}
}
   evenodd([2,2,4,0]);
Given arr, add 1 to odd elements ([1], [3], etc.), console.log all values and return arr. 
function incrument(arr){
     for(var i=0; i<arr.length; i++){
             if (arr[i]%2===1){
         arr[i]++;
         //console.log(arr[i])
       }
       console.log(arr[i])
    }
    return arr;
    }
    
     var test =[1,4,5,8];
     console.log(incrument(test));

Build function that accepts array. Return a new array with all values except first, adding 7 to each. 
Do not alter the original array.
function seven(arr){
  var newarr=[];
  for (var i=1; i<arr.length; i++){
   newarr.push(arr[i]);
  }
  newarr.push(7);
  console.log(arr, newarr);
}
seven([1,0,2,3,4])

Given array, write a function to reverse values, in-place. Example:
reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3]. 
function reverse(arr){
  temp= arr[arr.length-1]
  temp1= temp1 =arr[arr.length-2]
  for (var i=arr.length-2/2; i>0; i--){
  arr[arr.length-1]= arr[0];
  arr[arr.length-2]=arr[arr.length-3];
  }
  arr[0]=temp;
  arr[arr.length-3]=temp1
  return arr;
//console.log(arr, temp, arr[arr.length-3]);
}
var test=[1,2,3,4];
console.log(reverse(test));
Given an array, create and return a new one containing all the values of the provided array, 
made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5]. 
function negative(arr){
  for (var i=0; i<arr.length; i++){
      if(arr[i]>0){
         arr[i]= -arr[i];
     // arr.push(arr[i]*(-1));
  }
 }
return arr;
}
var test=[1,-3,5];
console.log(negative(test));

Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". 
If no array elements are "food", then print "I'm hungry" once. 

Swap Toward the Center
Given array, swap first and last, third and third-to-last, etc. 
Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true]. Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

function swap(arr){
temp=arr[0];
temp1= arr[arr.length-3]
    arr[0]= arr[arr.length-1];
  arr[arr.length-1]=temp;
  arr[arr.length-3]= arr[arr.length-4];
    for (var i=arr.length/2; i<0; i--){
    }
  arr[arr.length-4]=temp1;
  //}
console.log(arr);
}
//swap(["true",42,"Ada",2,"pizza"]);
swap([1,2,3,4,5,6])

//Given array arr and number num, multiply each arr value by num, and return the changed arr
function multiply(arr,num){
for (var i =0; i< arr.length; i++){
  arr[i]=arr[i]*num;
  // console.log(arr[i], arr.length);
}
return arr;
//console.log(arr);
}
var num=3;
var test =[2,4,3];
console.log(multiply(test,num));