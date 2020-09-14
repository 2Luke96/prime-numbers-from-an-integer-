from flask import Flask , render_template, redirect, request

app = Flask(__name__)
from itertools import permutations 
import numpy as np

@app.route('/')
def home():
    return render_template('index.html')

def gfg1(prime):
    lis = [] 
    # getting input with name = fname in HTML form 
    #prime = request.form.get("fname") 
    for i in range(1,len(str(prime))+1):
        perm = permutations([*(str(prime))],i)
        for j in perm: 
            x = int("".join(j))
            if x > 1:
                for i in range(2,x):
                    if (x % i) == 0: #not a prime number
                        break
                else:
                   lis.append(x)
    return ("List of Prime Numbers" + str(lis) + "   ,  " + " MEAN :" + str(np.mean(lis)) +"  ,  " + "MEDIAN :" + str(np.median(lis)))

@app.route("/gfg", methods =["POST"])
def gfg():
    result = request.form.get("NUMBER")
    result1 = gfg1(result)              
    return render_template("index.html", predict = '{}'.format(result1))

if __name__ == "__main__":
    app.run(debug = True)