
from main import Main
from flask import Flask, request, render_template, send_file
#from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/")
#@cross_origin()
def home():
	return render_template("index.html")

@app.route("/download")
def download_output_file():
    path = "outputfiles/output1.txt"
    return send_file(path,as_attachment=True)

@app.route("/download1")
def download_impacts_file():
    path = "outputfiles/impactfile1.txt"
    return send_file(path,as_attachment=True)


@app.route("/predict", methods = ["GET", "POST"])
#@cross_origin()
def predict():
    main_obj = Main()
    try:
        
        if request.method == "POST":
            try:
                
                file = request.files["inputfile"]
                analysis_type = request.form["analysis"]
                Static_impacts = request.form["r1"]
                dynamic_impacts = request.form["r2"]
                impact_file_download = request.form["r3"]
                impacted_elements_download = request.form["r4"]
                
                copy,static,move,call,procs,dynamic= False,False,False,False,False,False
                im_ele,im_file = False,False
                if analysis_type =="cycy" or analysis_type == "cycb":
                    copy=True
                elif analysis_type == "cbcb":
                    move,call = True,True
                elif analysis_type == "procs":
                    procs = True
                    
                if Static_impacts =="yes":
                    static = True
                if dynamic_impacts == "yes":
                    dynamic = True
                    
                if impacted_elements_download == "yes":
                    im_ele = True
                    
                if impact_file_download == "yes":
                    im_file = True
    
                main_obj.sent_file(file,copy,static,move,call,dynamic,im_ele,im_file,procs)
            except:
                print("error in data")

    except:
            print("error in loading form")

    data_to_pass = main_obj.data_to_pass
    del main_obj
    
            
    return render_template("output.html",data = data_to_pass)
            
            
if __name__ == "__main__":
	app.run(debug=True)