from flask import Flask, render_template, request, redirect, url_for
from colorama import Fore, Style

app = Flask(__name__)

class SimpleDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, word, meaning):
        self.dictionary[word] = meaning
        return f"{Fore.GREEN}Added:{Style.RESET_ALL} {word} - {meaning}"

    def delete_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            return f"{Fore.RED}Deleted:{Style.RESET_ALL} {word}"
        else:
            return f"{Fore.YELLOW}{word} not found in the dictionary.{Style.RESET_ALL}"

    def update_word(self, word, new_meaning):
        if word in self.dictionary:
            self.dictionary[word] = new_meaning
            return f"{Fore.BLUE}Updated:{Style.RESET_ALL} {word} - {new_meaning}"
        else:
            return f"{Fore.YELLOW}{word} not found in the dictionary.{Style.RESET_ALL}"

    def get_dictionary(self):
        return [(word, meaning) for word, meaning in self.dictionary.items()]

my_dictionary = SimpleDictionary()

@app.route('/')
def index():
    return render_template('index.html', dictionary=my_dictionary.get_dictionary())

@app.route('/add', methods=['POST'])
def add():
    word = request.form['word']
    meaning = request.form['meaning']
    message = my_dictionary.add_word(word, meaning)
    return redirect(url_for('index', message=message))

@app.route('/delete', methods=['POST'])
def delete():
    word = request.form['word']
    message = my_dictionary.delete_word(word)
    return redirect(url_for('index', message=message))

@app.route('/update', methods=['POST'])
def update():
    word = request.form['word']
    new_meaning = request.form['new_meaning']
    message = my_dictionary.update_word(word, new_meaning)
    return redirect(url_for('index', message=message))

if __name__ == '__main__':
    app.run(debug=True)
