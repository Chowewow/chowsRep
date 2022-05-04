function answer(){
    let parseEquation = new RegExp('[0-9]+|[*/+-]','g')
    let equation = [document.getElementById('inp').value.matchAll(parseEquation)];
    console.log(equation);
    // let parseNumbers = new RegExp('[0-9]+', 'g');
    // let parseMultDiv = new RegExp('[*/]','g');
    // let parsePlusSub = new RegExp('[+-]', 'g');
    // let numArray = document.getElementById("inp").value.replace(/ /g, '');
    // console.log(numArray);
    // console.log(numArray.search(parseMultDiv))
    // while(numArray.search(parseMultDiv) != -1){
    //     parseInt(numArray[numArray.search(parseMultDiv) - 1]) * parseInt(numArray[numArray.search(parseMultDiv) + 1])
    // }

    // if (elementArray.findIndex('*') != - 1){
    //     numArray[elementArray.findIndex('*')] = numArray[elementArray.findIndex('*')] * numArray[elementArray.findIndex('*') + 1];
    //     numArray[elementArray.findIndex('*') + 1]
    // }
    // while (index < elementArray.length){
    //     e
    // }

}