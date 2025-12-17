# Recipe Share Web Application

A secure web application for sharing food recipes built with Python Flask.

## Features

### ✅ User Management
- **Register**: Create new user account with validation
  - Username must be at least 3 characters
  - Email must be unique
  - Password must be at least 8 characters
  
- **Login**: Secure login with password hashing
  - Passwords hashed using Werkzeug security
  - Session-based authentication
  - Remember me functionality
  
- **Session Handling**: 
  - HTTPOnly and Secure cookies
  - CSRF protection
  - Session timeout (7 days by default)

### 📝 Data Submission
- **Recipe Form**: Submit recipes with:
  - Title, description, ingredients, instructions
  - Cooking time, servings, difficulty level
  - Image upload with sanitization
  
- **Comments**: Leave feedback on recipes
  - Max 500 characters per comment
  - Comment display with timestamps

### 📁 File Management
- **File Upload**: 
  - Secure filename generation (prevents path traversal)
  - File type validation (pdf, txt, jpg, jpeg, png, gif, doc, docx)
  - File size limit (16MB max)
  - Stored in secure uploads folder
  
- **File Download**: 
  - Secure file download with path validation
  - Download as attachment

## Project Structure

```
project-web-secure/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── README.md              # This file
├── uploads/               # Uploaded files (auto-created)
└── templates/             # HTML templates
    ├── base.html          # Base template
    ├── index.html         # Home page
    ├── register.html      # Registration
    ├── login.html         # Login page
    ├── new_recipe.html    # Create recipe
    ├── view_recipe.html   # View recipe details
    ├── edit_recipe.html   # Edit recipe
    ├── my_recipes.html    # User's recipes
    ├── profile.html       # User profile
    ├── 404.html           # Not found page
    └── 500.html           # Server error page
```

## Installation & Setup

### 1. Clone/Setup the Project
```bash
cd project-web-secure
```

### 2. Create Virtual Environment
```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Or Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python app.py
```

The app will create `recipe_app.db` automatically on first run.

### 5. Run the Application
```bash
python app.py
```

The app will be available at: **http://localhost:5000**

## Database Models

### User Model
- `id`: Primary key
- `username`: Unique username (min 3 chars)
- `email`: Unique email address
- `password_hash`: Hashed password (using Werkzeug)
- `created_at`: Account creation timestamp

### Recipe Model
- `id`: Primary key
- `title`: Recipe title
- `description`: Recipe description
- `ingredients`: Ingredients list
- `instructions`: Cooking instructions
- `cooking_time`: Time in minutes
- `servings`: Number of servings
- `difficulty`: Easy/Medium/Hard
- `image_filename`: Recipe image filename
- `created_at`, `updated_at`: Timestamps
- `user_id`: Foreign key to User

### Comment Model
- `id`: Primary key
- `content`: Comment text
- `created_at`: Comment timestamp
- `user_id`: Foreign key to User
- `recipe_id`: Foreign key to Recipe

## Security Features

### Password Security
- Passwords hashed using Werkzeug `generate_password_hash()`
- Minimum 8 characters required
- Never stored in plain text

### File Upload Security
- Files renamed with random names (prevents overwrite)
- File type whitelist validation
- File size limit (16MB)
- Path traversal prevention with `secure_filename()`

### Session Security
- HTTPOnly cookies (prevents XSS)
- Secure flag for HTTPS
- SameSite policy (Lax)
- Session timeout (7 days)

### Input Validation
- Form validation on both client and server side
- SQL injection prevention (SQLAlchemy ORM)
- CSRF protection with Flask-WTF (can be added)
- XSS prevention with template auto-escaping

### Database Security
- SQLAlchemy ORM prevents SQL injection
- Foreign key constraints
- Cascade delete for data integrity

## API Endpoints

### Public Routes
- `GET /` - Home page with recipe listing
- `GET /register` - Registration page
- `POST /register` - Submit registration
- `GET /login` - Login page
- `POST /login` - Submit login
- `GET /recipe/<id>` - View recipe details
- `GET /upload/<filename>` - Download file

### Protected Routes (Login Required)
- `POST /logout` - Logout user
- `GET /recipe/new` - Create recipe form
- `POST /recipe/new` - Submit new recipe
- `GET /recipe/<id>/edit` - Edit recipe form
- `POST /recipe/<id>/edit` - Update recipe
- `POST /recipe/<id>/delete` - Delete recipe
- `GET /my-recipes` - View user's recipes
- `POST /recipe/<id>/comment` - Add comment
- `GET /profile` - View user profile

## Configuration

### Development (default)
```python
DEBUG = True
SESSION_COOKIE_SECURE = False  # For local development
```

### Production
```python
DEBUG = False
SESSION_COOKIE_SECURE = True   # Requires HTTPS
```

Change in `config.py`:
```python
app.config.from_object(config['production'])
```

## Default Admin Setup (Optional)

To create a test user, add this to `app.py` after `db.create_all()`:

```python
if not User.query.filter_by(username='testuser').first():
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    print("Test user created: username=testuser, password=password123")
```

## Dependencies

- **Flask** 2.3.3 - Web framework
- **Flask-SQLAlchemy** 3.0.5 - ORM and database
- **Flask-Login** 0.6.2 - User session management
- **Werkzeug** 2.3.7 - WSGI utilities and password hashing
- **python-dotenv** 1.0.0 - Environment variable management

## Usage Examples

### Register
1. Go to http://localhost:5000/register
2. Fill in username, email, password
3. Click Register

### Login
1. Go to http://localhost:5000/login
2. Enter credentials
3. Optionally check "Remember me"

### Create Recipe
1. Click "+ New Recipe" in navigation
2. Fill in recipe details
3. Upload image (optional)
4. Submit

### Share Recipe
- View recipe details on recipe page
- Share the recipe URL
- Leave comments for feedback

### Download Files
- Click recipe image to download
- Files are automatically sanitized

## Troubleshooting

### Database Issues
Delete `recipe_app.db` and run `python app.py` again to reinitialize.

### File Upload Not Working
Check that `uploads/` folder exists and has write permissions.

### Session Not Persisting
Set `SESSION_COOKIE_SECURE = False` in `DevelopmentConfig` for local testing.

## Future Enhancements

- [ ] Recipe ratings/stars
- [ ] Search functionality
- [ ] Recipe categories/tags
- [ ] Email verification
- [ ] Password reset
- [ ] Social sharing
- [ ] Recipe favorites
- [ ] Admin dashboard
- [ ] API endpoints
- [ ] Mobile responsive improvements

## License

This project is free to use and modify.

## Support

For issues or questions, please check the code comments or review the security documentation.
