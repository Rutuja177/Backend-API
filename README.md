# Flask Backend API for CRUD Operations

This project showcases a RESTful API that allows performing CRUD operations - Create, Read, Update, and Delete - on user data.

## Installation and Setup

To get started with the API, follow these steps:

1. Install Python: Make sure you have Python installed on your system.

2. Install Flask: This project utilizes Flask as the web framework. Install Flask by running the following command in your terminal or command prompt:
   ```
   pip install Flask
   ```

3. Clone the Repository: Clone the "Flask_Backend-API" repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/Flask_Backend-API.git
   ```

4. Start the Flask Server: Navigate to the cloned directory and start the Flask server by executing the following command:
   ```
   python API_call.py
   ```

## Testing the API

After starting the Flask server, you can test the API using one of the following methods:

1. Web Browser: Open your web browser and navigate to http://localhost:5000/. This will display the homepage of the Flask application, indicating that the server is up and running.

2. Postman: Use Postman, a popular API testing tool, to test all CRUD operations. The following endpoints are available for testing:

   - View All Users: GET http://localhost:5000/
   - View User by ID/name: GET http://localhost:5000/"id" OR http://localhost:5000/"name" (replace "id" with the user's ID)
   - Create User: POST http://localhost:5000/create
   - Update User: PUT http://localhost:5000/updateRecord
   - Delete User: DELETE http://localhost:5000/delete (please provide user ID in the request payload)

## Tech Stack

The API is built using Python and the Flask web framework.
for testing: POSTMAN

## Sample Usage

You can download the zip file of this project and run the command `python app.py` in your terminal or command prompt. This will start the API server, and you can then test the APIs locally on http://localhost:5000/ using Postman.

Feel free to use this API to test your own projects or explore how CRUD operations can be implemented using Flask.

For any questions or feedback, please reach out to the project contributors.

Happy coding!
