# Entry point for the Flask application

from app import create_app

# Initialize the app using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
