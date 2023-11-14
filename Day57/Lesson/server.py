from flask import Flask, render_template
import random
import time


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)
    
if __name__ =="__main__":
  app.run(debug=True)
  
  
@app.route('/blog')
def blog():
  blog_url=""
  blog_data= requests.get(blog_url)
  all_posts = blog_data.json
  
  return render_template("blog.html", posts=all_posts)
  

if __name__ == "__main__":
    app.run(debug=True)
