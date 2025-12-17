# 🍳 Recipe Share App - Quick Start Guide

## Installation (5 minutes)

### Step 1: Install Python Requirements
```powershell
# Open PowerShell in the project directory
pip install -r requirements.txt
```

### Step 2: Run Setup
```powershell
python setup.py
```

This will:
- ✅ Create the `uploads` folder
- ✅ Initialize the SQLite database
- ✅ Create a test user (demo/demo1234)

### Step 3: Start the App
```powershell
python app.py
```

You should see:
```
Database initialized!
 * Running on http://127.0.0.1:5000
```

### Step 4: Open in Browser
- Go to **http://localhost:5000**
- You're ready to go! 🎉

---

## Default Test User

**Username:** demo  
**Password:** demo1234  
**Email:** demo@example.com

---

## Features Checklist

### ✅ User Management
- [x] Register with email
- [x] Login with password hashing
- [x] Session handling
- [x] User profile

### ✅ Recipe Submission
- [x] Create new recipe (title, description, ingredients, instructions)
- [x] Edit recipes
- [x] Delete recipes
- [x] Difficulty levels (Easy/Medium/Hard)
- [x] Cooking time & servings

### ✅ File Handling
- [x] Upload recipe images
- [x] Secure filename generation
- [x] File type validation
- [x] File size limits (16MB max)
- [x] Download files

### ✅ Comments & Interaction
- [x] Leave comments on recipes
- [x] View comments with timestamps
- [x] User profile with stats

### ✅ Security
- [x] Password hashing (Werkzeug)
- [x] CSRF protection ready
- [x] HTTPOnly cookies
- [x] Input validation
- [x] Path traversal prevention

---

## Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application (all routes) |
| `models.py` | Database models (User, Recipe, Comment) |
| `config.py` | Configuration settings |
| `requirements.txt` | Python dependencies |
| `setup.py` | Setup script |
| `.env` | Environment variables |
| `templates/` | HTML templates (9 files) |
| `uploads/` | Uploaded files (auto-created) |

---

## Common Tasks

### Create a Recipe
1. Login (or use demo/demo1234)
2. Click "+ New Recipe"
3. Fill in details:
   - Title (min 5 chars)
   - Description
   - Ingredients (one per line)
   - Instructions
   - Cooking time (optional)
   - Servings (optional)
   - Difficulty level
   - Image (optional)
4. Click "Create Recipe"

### View All Recipes
- Home page shows all recipes
- Click "View Recipe" to see details
- Leave comments on any recipe

### Manage Your Recipes
- Click "My Recipes" in navigation
- Edit or delete your recipes
- See view count and comments

### Security Notes
- Passwords: Min 8 characters, hashed with Werkzeug
- Files: Renamed automatically, type validated
- Sessions: 7-day timeout, HTTPOnly cookies

---

## Configuration

Edit `config.py` to change:

```python
# Session timeout
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# File size limit (default: 16MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Allowed file types
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'jpg', 'jpeg', 'png', 'gif', 'doc', 'docx'}
```

---

## Database

**Type:** SQLite (recipe_app.db)  
**Tables:** users, recipes, comments

To reset database:
```powershell
Remove-Item recipe_app.db
python app.py
```

---

## Troubleshooting

### "ModuleNotFoundError"
```powershell
pip install -r requirements.txt
```

### "database is locked"
Close all other instances of the app and try again.

### File upload not working
Check that `uploads/` folder exists with write permissions.

### Can't login
Make sure you ran `setup.py` to create the test user.

---

## Production Deployment

Before deploying to production:

1. **Change SECRET_KEY** in `.env`:
   ```
   SECRET_KEY=your-very-long-random-key-here
   ```

2. **Use production config** in `app.py`:
   ```python
   app.config.from_object(config['production'])
   ```

3. **Set HTTPS** and secure cookies

4. **Use a real database** (PostgreSQL, MySQL):
   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/dbname'
   ```

5. **Use a production WSGI server**:
   ```powershell
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

---

## Support & Documentation

- Full docs: See `README.md`
- Code comments: Review `app.py`
- Security info: See "Security Features" in README.md

---

**Happy Recipe Sharing! 🍽️**
