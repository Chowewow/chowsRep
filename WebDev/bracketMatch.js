function myFunction(input) {
if(input.length == 0){
    alert('Enter Code');
    
} else{
    let openCount = 0;
    let closedCount = 0;
    let code = input;
  
    for (let i = 0; i < code.length; i++) {
      if (code.charAt(i) == "{") {
        openCount += 1;
      } else if (code.charAt(i) == "}") {
        closedCount += 1;
      }
    }
  
    console.log(openCount, closedCount);
    document.getElementById("answer").innerHTML = openCount == closedCount;
    console.log(openCount == closedCount);
  }
}
 
