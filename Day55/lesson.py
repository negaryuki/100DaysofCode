from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
      
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper
      
def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a Paragraph</p>' \
           '<img src="https://media.giphy.com/media/c76IJLufpNwSULPk77/giphy.gif" width=200>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)

## Advanced Decorators:
  
class User:
  def __init__(self,name):
    self.name = name
    self.is_logged_in = False
    
def is_authenticated_decorator(function):
  def wrapper(*args,**kwargs):
    if args[0].is_logged_in == True:
      function(arg[0])
  return wrapper()


@is_authenticated_decorator
def create_blog_post(user):
  print(f"This is {user.name}'s new blog post")
  
new_user = User("Negar")
new_user.is_logged_in = True
create_blog_post(new_user)
