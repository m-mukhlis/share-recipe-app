# Recipe Share App - Complete Route Reference

## Public Routes (No Login Required)

### Home & Discovery
- **GET `/`**
  - Home page with all recipes
  - Paginated (6 per page)
  - Browse recipes from all users

### Authentication
- **GET `/register`**
  - Registration form
  - Field validation (username 3+, password 8+, unique email)
  
- **POST `/register`**
  - Submit registration
  - Creates user with hashed password
  - Redirects to login on success

- **GET `/login`**
  - Login form
  - Remember me checkbox

- **POST `/login`**
  - Authenticate user
  - Creates session (7-day timeout)
  - Supports "next" parameter for redirects

### Recipe Details
- **GET `/recipe/<recipe_id>`**
  - View full recipe details
  - See all comments
  - User info and recipe metadata

### File Downloads
- **GET `/upload/<filename>`**
  - Download uploaded files
  - Security: filename sanitization
  - Path traversal prevention

---

## Protected Routes (Login Required)

### Authentication
- **GET `/logout`**
  - Destroy user session
  - Redirect to home

### Recipe Management
- **GET `/recipe/new`**
  - Create recipe form
  - Multipart form (file upload)

- **POST `/recipe/new`**
  - Create new recipe
  - Process file upload
  - Validate all fields
  - Redirect to recipe view

- **GET `/recipe/<recipe_id>/edit`**
  - Edit recipe form
  - Show current recipe data
  - Display existing image

- **POST `/recipe/<recipe_id>/edit`**
  - Update recipe details
  - Optional new image upload
  - Update timestamp

- **POST `/recipe/<recipe_id>/delete`**
  - Delete recipe (author only)
  - Remove uploaded image
  - Delete all comments

### User Recipe List
- **GET `/my-recipes`**
  - View user's recipes only
  - Paginated (6 per page)
  - Edit/delete buttons visible

### Comments
- **POST `/recipe/<recipe_id>/comment`**
  - Add comment to recipe
  - Max 500 characters
  - Must be logged in

### User Profile
- **GET `/profile`**
  - View user stats
  - Recipe count
  - Comment count
  - Member since date

---

## Error Handlers

- **404 Not Found** - `/templates/404.html`
- **500 Server Error** - `/templates/500.html`

---

## Form Fields by Endpoint

### POST /register
```
username (required, min 3)
email (required, valid email)
password (required, min 8)
confirm_password (required, min 8)
```

### POST /login
```
username (required)
password (required)
remember (optional checkbox)
```

### POST /recipe/new
```
title (required, min 5)
description (required)
ingredients (required, multiline)
instructions (required, multiline)
cooking_time (optional, integer)
servings (optional, integer)
difficulty (optional, default "Medium")
image (optional, file upload)
```

### POST /recipe/<id>/edit
```
title (required, min 5)
description (required)
ingredients (required, multiline)
instructions (required, multiline)
cooking_time (optional, integer)
servings (optional, integer)
difficulty (optional)
image (optional, file upload)
```

### POST /recipe/<id>/comment
```
content (required, max 500)
```

---

## Response Codes & Redirects

| Route | Method | Success | Redirect |
|-------|--------|---------|----------|
| /register | POST | 302 | /login |
| /login | POST | 302 | /recipe/new (next param) or / |
| /logout | GET | 302 | / |
| /recipe/new | POST | 302 | /recipe/{id} |
| /recipe/{id}/edit | POST | 302 | /recipe/{id} |
| /recipe/{id}/delete | POST | 302 | /my-recipes |
| /recipe/{id}/comment | POST | 302 | /recipe/{id} |

---

## HTTP Methods Used

| Method | Purpose |
|--------|---------|
| GET | Display pages, download files |
| POST | Submit forms, authentication, create/update data |

*Note: DELETE method not used (uses POST with hidden method parameter for CSRF compatibility)*

---

## Query Parameters

- **`page`** - Pagination (index, my-recipes)
  - Example: `/?page=2`

- **`next`** - Redirect after login
  - Example: `/login?next=/recipe/new`

---

## Flash Messages

Flash messages are used for user feedback:

| Type | Message |
|------|---------|
| success | Account created, recipe saved, etc. |
| danger | Validation errors, permission errors |
| info | Logout message |

Messages auto-dismiss with Bootstrap alert close button.

---

## Security Features per Route

### Authentication Routes
- ✅ Password validation (min 8 chars)
- ✅ Password hashing (Werkzeug)
- ✅ Duplicate username/email check
- ✅ Session timeout (7 days)
- ✅ HTTPOnly cookies

### Recipe Routes
- ✅ Login required (except view)
- ✅ Author authorization check (edit/delete)
- ✅ Input validation & sanitization
- ✅ CSRF ready (implement form tokens)

### File Routes
- ✅ Secure filename generation
- ✅ File type whitelist validation
- ✅ File size limit (16MB)
- ✅ Path traversal prevention
- ✅ Unique random filenames

### Comment Routes
- ✅ Login required
- ✅ Length validation (max 500)
- ✅ HTML auto-escape in templates

---

## Pagination Configuration

- Items per page: **6**
- Available for: Home page, My Recipes
- Uses SQLAlchemy `paginate()`

Example:
```
GET /?page=1  # First page
GET /?page=2  # Second page
```

---

## File Upload Configuration

| Setting | Value |
|---------|-------|
| Max Size | 16MB |
| Storage | `uploads/` folder |
| Naming | Random hex + extension |
| Allowed Types | pdf, txt, jpg, jpeg, png, gif, doc, docx |

---

## Database Relationships

```
User (1) ──────────→ (N) Recipe
                      ↓
                    (N) Comment ←─────── (N) User
```

- User has many recipes
- User has many comments
- Recipe has many comments
- Comment belongs to one recipe and one user

---

## Template Variables Passed

### base.html (All templates)
- `current_user` - Flask-Login user object

### index.html
- `recipes` - Paginated recipe query

### view_recipe.html
- `recipe` - Recipe object
- `comments` - Comment list

### my_recipes.html
- `recipes` - User's paginated recipes

### profile.html
- `recipe_count` - Integer
- `comment_count` - Integer

### new_recipe.html, edit_recipe.html
- `recipe` - Recipe object (edit only)

---

## URL Structure Examples

```
http://localhost:5000/                          # Home
http://localhost:5000/register                  # Register
http://localhost:5000/login                     # Login
http://localhost:5000/recipe/1                  # View recipe 1
http://localhost:5000/recipe/new                # Create recipe
http://localhost:5000/recipe/1/edit             # Edit recipe 1
http://localhost:5000/recipe/1/comment          # Add comment to recipe 1
http://localhost:5000/upload/abc123def.jpg      # Download image
http://localhost:5000/my-recipes                # My recipes
http://localhost:5000/profile                   # User profile
```

---

## Session & Cookie Information

**Session Duration:** 7 days  
**Cookie Name:** `session`  
**Cookie Flags:**
- HttpOnly: ✅ (prevents XSS)
- Secure: ❌ (local dev), ✅ (production)
- SameSite: Lax (prevents CSRF)

---

**Last Updated:** December 2024  
**Framework:** Flask 2.3.3  
**Auth:** Flask-Login 0.6.2
