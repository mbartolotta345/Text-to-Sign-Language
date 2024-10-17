from flask import Flask, render_template, request

#initializes application
app = Flask(__name__)

def word_list(word: str) -> list[str]:
    '''Takes the word input and converts it into a list of each letter'''
    return list(word)

def letter_to_image(letters: list[str]) -> list[str]:
    '''Converts a list of letters into a list of corresponding ASL image filenames'''
    image_list = []
    for letter in letters:
        image_filename = f"{letter}.png"
        image_list.append(image_filename)  # Add the image filename to the list
    return image_list  # Return the list of image filenames

@app.route('/', methods=['GET', 'POST'])  # Define the route for the homepage
def index():
    images = []
    if request.method == 'POST':  # Check if the request method is POST
        word = request.form['word']  # Get the word input from the form
        letters = word_list(word.lower())
        images = letter_to_image(letters)
    return render_template('index.html', images=images)  # Render the index template with images

if __name__ == '__main__':
    app.run(debug=True, port=8000)