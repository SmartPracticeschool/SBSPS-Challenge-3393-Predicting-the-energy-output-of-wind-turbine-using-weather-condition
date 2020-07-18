from flask import Flask , render_template , request
app = Flask(__name__) # interfacee between by server and my application wsgi
import pickle
model=pickle.load(open('Energy1.pkl','rb'))
@app.route('/') # bind to an url 
def helloworld():
    return render_template("Web-App.html")
@app.route('/predict',methods = ['POST','GET']) # bind to an url 
def predict():
    p = request.form["ws"]
    q = request.form["tpc"]
    r = request.form["wd"]
    w = request.form["w"]
    if(w=="Cloudy"):
        w1,w2,w3,w4=1,0,0,0
    if(w=="Rainy"):
        w1,w2,w3,w4=0,1,0,0
    if(w=="Sunny"):
        w1,w2,w3,w4=0,0,1,0
    if(w=="Windy"):
        w1,w2,w3,w4=0,0,0,1
    t = [[int(w1),int(w2),int(w3),int(w4),int(p),int(q),int(r)]]
    y = model.predict(t)
    return render_template("Web-App.html", y="The predicted energy would be:" +str(y[0]))

@app.route('/user')#url
def user():
    return "predicted value"

if __name__ == '__main__' :
    app.run(debug =True)