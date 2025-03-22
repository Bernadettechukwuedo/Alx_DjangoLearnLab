# Blog Application (Django)

This Django-powered blog application allows users to create, edit, and delete blog posts, as well as comment on them. It includes user authentication, post tagging, and a search functionality.

## Features

- **User Authentication**

  - Registration, login, and logout functionality.
  - Only authenticated users can create, update, or delete posts and comments.

- **Blog Post Management**

  - `PostListView`: Displays a list of all blog posts.
  - `PostDetailView`: Displays the details of a single post.
  - `PostCreateView`: Allows authenticated users to create a post.
  - `PostUpdateView`: Allows post authors to edit their posts.
  - `PostDeleteView`: Allows post authors to delete their posts.

- **Comment System**

  - Users can create, update, and delete comments on blog posts.
  - `CommentCreateView`: Authenticated users can add comments.
  - `CommentListView`: Displays comments for a specific post.
  - `CommentUpdateView`: Allows the comment author to edit their comment.
  - `CommentDeleteView`: Allows the comment author to delete their comment.

- **Tagging System**

  - Users can filter posts by tags.
  - `PostByTagListView`: Displays all posts associated with a specific tag.

- **Search Functionality**
  - Users can search for posts by title, content, tags, or author.

## URL Endpoints

| URL                           | View                | Description                               |
| ----------------------------- | ------------------- | ----------------------------------------- |
| `/profile/`                   | `profile()`         | Displays the user's profile.              |
| `/register/`                  | `register()`        | Handles user registration.                |
| `/login/`                     | `login_user()`      | Handles user login.                       |
| `/logout/`                    | `logout_user()`     | Logs out the user.                        |
| `/posts/`                     | `PostListView`      | Lists all posts.                          |
| `/posts/<pk>/`                | `PostDetailView`    | Displays a single post.                   |
| `/posts/new/`                 | `PostCreateView`    | Allows users to create a post.            |
| `/posts/<pk>/edit/`           | `PostUpdateView`    | Allows post authors to edit their post.   |
| `/posts/<pk>/delete/`         | `PostDeleteView`    | Allows post authors to delete their post. |
| `/posts/tag/<slug:tag_slug>/` | `PostByTagListView` | Displays posts filtered by tag.           |
| `/search/?q=<query>`          | `search_results()`  | Searches for posts based on user input.   |

## Installation

1. Clone the repository:
   ```bash
   git https://github.com/Bernadettechukwuedo/Alx_DjangoLearnLab.git
   cd django_blog
   cd blog
  pip install -r requirements.txt
   python manage.py runserver
   ```
