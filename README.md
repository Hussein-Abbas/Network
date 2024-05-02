# Social Network Project

This project is part of the CS50W course and implements a basic social network using Django, Python, JavaScript, HTML, and CSS. Users can create posts, follow other users, like posts, edit their own posts, and view posts from users they follow.

## Getting Started

To get started with this project, follow these instructions:

1. Clone this repository to your local machine: git clone https://github.com/Hussein-Abbas/Network.git
2. Navigate to the project directory: cd Network
3. Install the project dependencies: pip install -r requirements.txt
4. Apply database migrations: python manage.py migrate
5. Run the development server: python manage.py runserver

8. Visit http://127.0.0.1:8000/ in your web browser to access the application.

## Project Structure

- **network**: Django application directory containing the project's Python code.
- `views.py`: Contains view functions for handling HTTP requests.
- `models.py`: Defines database models for users and posts.
- `urls.py`: Contains URL patterns for routing requests to appropriate views.
- **templates/network**: Contains HTML templates for rendering pages.
- **static/network**: Contains static files such as CSS and JavaScript.
- **scripts.js**: Contains JavaScript code for client-side functionality.
- **styles.css**: Contains CSS styles for the user interface.
- **requirements.txt**: Lists all project dependencies.

## Features

- **New Post**: Users can create new text-based posts.
- **All Posts**: Displays all posts from all users, with the most recent posts first.
- **Profile Page**: Displays posts of a specific user, along with follower/following counts.
- **Following Page**: Displays posts from users that the current user follows.
- **Pagination**: Pagination for displaying posts.
- **Edit Post**: Users can edit their own posts.
- **Like and Unlike**: Users can like/unlike posts asynchronously without page reload.

## Acknowledgements
Many thanks to the CS50W staff for the high quality of education and the assignments for our rapid development.
