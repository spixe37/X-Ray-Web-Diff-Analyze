/* Loading of page */
function init() {
    //alert("Loaded");
    
    // ListBox
    list = document.getElementById("list1");
    // Remove ListBox's childs
    removeChilds(list);
    
    // Adding options
    for(var i=9; i >= 1; i--) {
        var option = document.createElement("option");
        option.text = i;
        list.add(option, list[i-1]);
    }
    
    // Sorting ListBox
    sortSelect(list);
    
    // First call text fields function on start
    createText(1)
}

// Adding initialization on start
window.onload = init;

// Creating text fields
function createTextFields(count) {
    
    // Fix null exception
    if(count === undefined)
        count = 1;
    
    // ListBox
    list = document.getElementById("list1");
    // Text form
    text = document.getElementById("text1");
    
    // Getting selected option
    var optionNumber = +list.options[list.selectedIndex].value;
    // Remove Field's childs
    removeChilds(text);
    
    // Adding inputs
    for(var i=0; i < optionNumber; i++) {
        
        // Creating input
        var input = document.createElement("input");
        // Adding class to input
        input.classList.add("form-control");
        // Adding type to input
        input.type = "text";
        input.placeholder = "Введите значение";
        text.appendChild(input);
    }
    //alert(optionNumber);
}

function removeChilds(selfElem) {
    while (selfElem.hasChildNodes()) {
                selfElem.removeChild(selfElem.lastChild);
    }
}

/* https://stackoverflow.com/questions/278089/javascript-to-sort-contents-of-select-element*/
function sortSelect(selElem) {
    var tmpAry = new Array();
    for (var i=0;i<selElem.options.length;i++) {
        tmpAry[i] = new Array();
        tmpAry[i][0] = selElem.options[i].text;
        tmpAry[i][1] = selElem.options[i].value;
    }
    tmpAry.sort();
    while (selElem.options.length > 0) {
        selElem.options[0] = null;
    }
    for (var i=0;i<tmpAry.length;i++) {
        var op = new Option(tmpAry[i][0], tmpAry[i][1]);
        selElem.options[i] = op;
    }
    return;
}