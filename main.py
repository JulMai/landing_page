from flask import Flask, render_template                                                                           
import json                                                                                                     
app = Flask(__name__)                                                                                
                                                                                                     
                                                                                                     
@app.route("/")                                                                                      
def index():                                                                                         
    with open('sites.json') as f:
        dict_sites = json.load(f)    
        return render_template('index.html', dict_sites=dict_sites)                                                                                
                                                                                                     
if __name__ == "__main__":                                                                           
    app.run(host="0.0.0.0", debug=True, port=5000)