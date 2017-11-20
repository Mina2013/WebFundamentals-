var num = 0;
var names =['james', 'jill','jane','jack'];
for (var num =0; num <= arr.lenght; num++); 
{
  if (num ==6) 
  {
    break;
    // if you have additional code down here, it will never run!
  }
  console.log(num, ">", [arr]);
  num = num + 1;          // if we break, we leave the WHILE loop so these lines won’t run
}