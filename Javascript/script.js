var num = 23;
var name = 'Todd';
var booly = false; 
var und = undefined;
var arr = [1, 'words', [1,2,3], (0 === 1), true];
// console.log(arr[2][2]);
var myInfo = {
    name: 'Todd',
    age: 33,
    hobbies: ['sports', 'coding', 'brewing']
}
// console.log(myInfo.name);


// For numbers 1 thru 100, print "fizz" if the number is evenly divisible by 3, "buzz" by 5, "fizzbuzz" by both,
// or just the number if nothing else happens.
function fizzbuzz(start, end){
    // var num = 50;
    for (var i = start; i <= end; i++){
        if (i % 3 == 0 && i % 5 == 0){
            console.log('fizzbuzz');
        }
        else if (i % 3 == 0){
            console.log('fizz');
        }
        else if (i % 5 == 0){
            console.log('buzz');
        }
        else{
            console.log(i);
        }
    }
}

fizzbuzz(50, 79);