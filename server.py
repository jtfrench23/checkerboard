from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', columns=8, rows=8, colorOne='black', colorTwo='red')
@app.route('/<int:columns>')
def column_number(columns):
    return render_template('index.html', columns=columns, rows=8)
@app.route('/<int:columns>/<int:rows>')
def column_and_row(columns,rows):
    return render_template('index.html', columns=columns, rows=rows)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

