# Project Django Netflix

## Description
### This project is a web application developed in Django, inspired by the Netflix interface. It allows users to create profiles, add movies, and watch videos.

## Main Features
### User Authentication: Utilizes Django's authentication system and the allauth library for user login and registration.

### Profile Management: Users can create profiles for different family members, each with their own name and parental control settings.

### Movie Listing: Displays a list of available movies to watch.

### Movie Details: When selecting a movie, users can view detailed information about it, such as title, description, and playback options.

### Video Playback: Allows users to watch movies and series directly on the platform.

## Project Structure
### admin.py: This file registers data models in Django's admin panel, allowing system administrators to manage the application's data through a user-friendly interface.

### forms.py: Defines forms used for user interactions. For example, the profile creation form is defined here, allowing users to create customized profiles.

### models.py: Contains the definition of data models for the project. This includes models such as CustomUser to represent system users, Profile to represent profiles associated with users, and Movie to represent available movies for viewing.

### urls.py: Manages application routes, mapping URLs to specific view functions. For example, when a user accesses the home page, the URL is mapped to the corresponding view function to render the correct page.

### views.py: Contains view classes and functions that process user requests and return appropriate responses. For example, the MovieListView class is responsible for displaying the list of available movies.

## templates
### base.html: This file is the base template used for all other pages of the application. It defines common layout elements such as the header and footer, which are shared by all pages.

### index.html: This page is the application's home page. It displays an attractive header with featured sections for spotlighted movies.

### movieList.html: This page displays a list of available movies for viewing. It may include information such as title, description, and playback options.

### moviesDetails.html: This page shows detailed information about a selected movie, such as title, description, and playback options.

### partius.html: This page is a navigation bar containing login/logout options and a button to access the profile registration page.

### profilecreate.html: This file contains a form for creating a new user profile. It may include fields for profile name, parental control settings, etc.

## Differences from Project 2 and 4
### Integration of Additional Models: This project includes models such as Profile and Video to manage user profiles and videos associated with movies.

### Addition of Video Playback Features: Implements video playback functionality, allowing users to watch movies and series directly on the platform.

### Design Customization: Pages have been styled to resemble the Netflix interface, with visual elements creating a similar browsing experience.

### Increased Complexity of Features: This project adds more features, such as the ability to create user profiles and set parental control settings, making it more complex compared to Project 2 and 4.

## How to Run the Project
### Clone this repository to your local machine.
### Ensure you have Python and Django installed.
### Navigate to the project's root directory in the terminal.
### Run python manage.py migrate to apply migrations.
### Run python manage.py runserver to start the development server.
### Open a web browser and access http://localhost:8000/ to see the project running.

## Conclusion
### This project offers a Netflix-like experience, allowing users to create profiles, explore a variety of movies, and watch videos directly on the platform. With a well-organized structure and a range of features, it's a great demonstration of web development with Django.


# "Please understand that I chose to incorporate the movie trailer as a symbolic representation, as sharing the full movie would be a copyright violation. I opted for this approach as a way to respect the laws and rights of the creators while still aiming to share the essence of the Netflix."


### video: https://youtu.be/KqocQtl6WfI