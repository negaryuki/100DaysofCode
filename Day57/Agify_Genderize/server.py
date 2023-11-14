import flask
import requests

app = Flask(__name__)
    
@app.route('/guess/<name>')
def guess(name):
  gender_url =f"http://api.genderize.io?name={name}"
  gender_response = requests.get(gender_url)
  gender_data= gender_response.json()
  gender = gender_data["gender"]
  
  age_url= f"https://api.agify.io?{name}"
  age_reponse = requests.get(age_url)
  age_data = age_reponse.json()
  age = age_data["age"] 
   
  return render_template("index.html", name =name, gender=gender, age=age)
    
    
if __name__ =="__main__":
  app.run(debug=True)
