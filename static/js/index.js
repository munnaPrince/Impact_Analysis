
function getFileExtension(){
	var filename = document.getElementById("inputfile");
	var extension = filename.value.split(".").pop()
	if(extension == "txt"){
		return true;
	}
	alert("Invalid file type. Please upload .txt file");
	filename.value = ""
	return false;

}


