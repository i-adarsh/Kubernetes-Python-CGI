from flask import Flask,render_template,request,url_for

app=Flask("My_k8s_App")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/docker")
def docker():
    return render_template("docker.html")

@app.route("/kubernetes")
def kubernetes():
    return render_template("kubernetes.html")

@app.route("/teams")
def team():
    return render_template("team.html")

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000,debug=True)
