# Flask Dictionary App

This is a simple Flask web application that allows you to manage a dictionary. You can add, delete, and update words along with their meanings using a web interface.

## Getting Started

### Prerequisites

Make sure you have Python and Flask installed on your system. You can install Flask using the following command:

```bash
pip install flask
```

### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-dictionary-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-dictionary-app
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000) in your web browser.

## Features

### 1. View Dictionary

- Access the dictionary at the home page [http://localhost:5000](http://localhost:5000).
- The dictionary will display existing words along with their meanings.

### 2. Add Word

- Navigate to the 'Add Word' page by clicking the 'Add Word' button.
- Enter a new word and its meaning, then click 'Add'.
- The word will be added to the dictionary.

### 3. Delete Word

- Navigate to the 'Delete Word' page by clicking the 'Delete Word' button.
- Enter the word you want to delete, then click 'Delete'.
- The word will be removed from the dictionary.

### 4. Update Word

- Navigate to the 'Update Word' page by clicking the 'Update Word' button.
- Enter the word and its new meaning, then click 'Update'.
- The meaning of the specified word will be updated.

## Structure

- `app.py`: Contains the Flask application code.
- `templates/index.html`: HTML template for rendering the dictionary and forms.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
