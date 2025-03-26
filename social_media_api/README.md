# Social Media API

This is a Django REST Framework (DRF) API for user authentication and profile management.

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd social_media_api
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```sh
   python manage.py migrate
   ```


4. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## User Registration & Authentication

### Register a User
**Endpoint:** `POST /register/`

**Payload:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "bio"  :"string"
}
```

### Login a User
**Endpoint:** `POST /login/`

**Payload:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "token": "Your token",
  "user": {
    "id": "user id",
    "email": "user@example.com"
  }
}
```

### Access Profile (Requires Authentication)
**Endpoint:** `GET /profile/`

**Headers:**
```sh
Authorization: Token your-auth-token
```

**Response:**
```json
{
  "id": 1,
  "bio": "",
  "profile_picture": null,
  "follower_count": 0,
  "following_count": 0
}
```

## User Model Overview
The `User` model extends Django's `AbstractUser` and includes the following fields:

- `email`: User's email address (unique, required)
- `bio`: Short user bio
- `follower` : Users that follow the user
- `profile_picture`


## Notes
- The API uses Django Rest Framework's Token Authentication.
- Ensure that every request to protected endpoints includes a valid token in the `Authorization` header.

