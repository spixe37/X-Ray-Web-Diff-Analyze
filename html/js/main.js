/* Constants */
const TEXT_ENTER_MESSAGE = "Введите значение";
const BUTTON_ENTER = "Ввод";
const BUTTON_EMPTY_FIELDS = "Заполните поля"
const BUTTON_CLEAR = "Очистить"

/* Loading of page */
function init() {
    //alert("Loaded");
    
    // Clear button
    clearf = document.getElementById("clearf");
    clearf.value = BUTTON_CLEAR;
    
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
    createTextFields(1)
    
    //Check Button
    checkbutton();
}

// Adding initialization on start
window.onload = init;

// Add Ajax And write Servlet
function sendInfo() {
    
    if(!checktext())
        return;
    var body = [];
    
    text = document.getElementById("text1")
    for(var i=0; i < text.childNodes.length; i++) {
        body.push(document.getElementsByClassName('intext')[i].value);
    }
    
    jbody = JSON.stringify(body);
    //alert(jbody);
    
    var xhr = new XMLHttpRequest();
    
    
    xhr.open("POST", "/xray-1.0/" + "?info=" + jbody, true)
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("outtext").innerHTML = xhr.responseText;
        }
    }
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.send();
    
}
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
        
        // Adding classes to input
        input.classList.add("form-control");
        input.classList.add("intext");
        
        // Adding type to input
        input.type = "text";
        
        input.change = checkbutton();
        
        input.onchange = checkbutton();
        
        // Adding placeholder
        input.placeholder = TEXT_ENTER_MESSAGE;
        
        // Adding input
        text.appendChild(input);
    }
    //alert(optionNumber);
}

// Set button types
function checkbutton() {
    
    // Send button
    btn = document.getElementById("chkbutton");
    
    // Checking text fields for length
    if(!checktext()) {
        btn.classList.remove("btn-success");
        btn.classList.add("btn-danger");
        btn.lastChild.data = BUTTON_EMPTY_FIELDS;
    } else {
        btn.classList.remove("btn-danger");
        btn.classList.add("btn-success");
        btn.lastChild.data = BUTTON_ENTER;
    }
}

// Cheking empty fields
function checktext() {
    check = true;
    text = document.getElementById("text1")
    for(var i=0; i < text.childNodes.length; i++) {
        if(document.getElementsByClassName('intext')[i].value.length <= 0){
            check = false;
            break;
        }
    }
    return check;
}

// Clearing fileds
function clearfields(){
    arr = document.getElementsByClassName('intext')
    for(var i=0; i < arr.length; i++){
        arr[i].value=null;
    }
    checkbutton();
}

/* Utils
--------------------------------------------------------
*/

// Removing childs
function removeChilds(selfElem) {
    while (selfElem.hasChildNodes()) {
                selfElem.removeChild(selfElem.lastChild);
    }
}

// Check empty
function isEmpty(item) {
    
    // Removing spaces
    item = item.trim();
    
    if(item.length > 0)
        return true;
    return false;
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