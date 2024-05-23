from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form
form_html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Simple Form</title>
  </head>
  <body>
    <h1>Enter your details</h1>
    <form action="/submit" method="post">
      Name: <input type="text" name="name"><br>
      Email: <input type="text" name="email"><br>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
"""

@app.route('/')
def form():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    # Write the data to a file
    with open('data.txt', 'a') as file:
        file.write(f'Name: {name}, Email: {email}\n')
    
    return f'Thank you {name}! Your data has been saved.'

if __name__ == '__main__':
    app.run(debug=True)
