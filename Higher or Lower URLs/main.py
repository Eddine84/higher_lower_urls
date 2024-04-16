from flask import Flask
import random



app = Flask(__name__)

choosed_number = random.randint(0,10)
print(choosed_number)

@app.route('/')
def guess_number():

 return "<h1>Guess a number between 0 and 9</h1> " \
        "<img style='width:100px' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>" \
        f"<h1>{choosed_number}</h1>"


@app.route('/<int:number>')
def play(number):

 if number > choosed_number:
  return "<h1>too big<h1> " \
         "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
 elif number < choosed_number:
        return "<h1>too small<h1/> " \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
 elif number == choosed_number:
   return "<h1>Correct<h1/> " \
          "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
 
 



if __name__ == "__main__":
 app.run(debug=True)