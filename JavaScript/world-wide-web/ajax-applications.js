//AJAX APPLICATION CODE SAMPLES//


//Function requesting and retrieving data from a text document (data.txt):
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "data.txt", true);
  xhttp.send();
}


//Creating XMLHttpRequest with a callback function, and retrieving data from two text documents (data.txt and data_2.txt):
loadDoc("data.txt", myFunction1);

loadDoc("data_2.txt", myFunction2);

function loadDoc(url, cFunction) {
  var xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      cFunction(this);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}

function myFunction1(xhttp) {
  // action goes here
}
function myFunction2(xhttp) {
  // action goes here
}


//Retrieve content from a (PHP) database:
function getData(str) {
  var xhttp;
  if (str == "") {
    document.getElementById("txtHint").innerHTML = "";
    return;
  }
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("txtHint").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "database.php?q="+str, true);
  xhttp.send();
}


//Function displaying XML data in an HTML table:
function loadXMLDoc() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myFunction(this);
    }
  };
  xmlhttp.open("GET", "data.xml", true);
  xmlhttp.send();
}
function myFunction(xml) {
  var i;
  var xmlDoc = xml.responseXML;
  var table="<tr><th>ELEMENT_1</th><th>ELEMENT_2</th></tr>";
  var x = xmlDoc.getElementsByTagName("MAIN_ELEMENT");
  for (i = 0; i <x.length; i++) {
    table += "<tr><td>" +
    x[i].getElementsByTagName("ELEMENT_1")[0].childNodes[0].nodeValue +
    "</td><td>" +
    x[i].getElementsByTagName("ELEMENT_2")[0].childNodes[0].nodeValue +
    "</td></tr>";
  }
  document.getElementById("demo").innerHTML = table;
}
