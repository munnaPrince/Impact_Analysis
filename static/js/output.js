var myVar = {{ data | tojson }}
console.log("myVar is");
console.log(myVar);

if(myVar.im_ele=="yes"){
document.getElementsByClassName("outputButton").disabled = false;
}
if(myVar.im_file=="yes"){
document.getElementsByClassName("ImpactsButton").disabled = false;
}
