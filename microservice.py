from math import sin
from flask import Flask

app = Flask(__name__)

@app.route("/numericalintegralservice/<lower>/<upper>/")
def numericalintegralservice(lower, upper):
    lower = float(lower)
    upper = float(upper)
    N = 10
    R = ""
    for i in range(6):
        S = 0
        l = (upper - lower) / N
        for j in range(N):
            S += l * abs(sin(lower + l * j))
        R += "N=" + str(N) + ": " + str(S) + "    "
        N *= 10
    return(R)
