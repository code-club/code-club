from flask import Flask, render_template, request, redirect
from foo import Foo

app = Flask("Meta foomash")

@app.route('/')
def index():
    foos = Foo.get_two_foos()
    return render_template('index.html', foos=foos, list_foos=Foo.get_liste())

@app.route('/vote', methods = ["GET"])
def vote():
    foo = Foo.get_by_name(request.args['name'])
    other = Foo.get_by_name(request.args['other'])
    foo.a_vaincu(other)
    return redirect("/")
    

if __name__ == "__main__" :
    Foo.ajouter(Foo('ciblout'))
    Foo.ajouter(Foo('remram'))
    Foo.ajouter(Foo('lily'))
    
    app.debug = True
    app.run()