#!/usr/bin/env python
"""
Quick setup script for Recipe Share Application
Run: python setup.py
"""

import os
import sys

def create_directories():
    """Create necessary directories"""
    os.makedirs('uploads', exist_ok=True)
    print("✅ Created 'uploads' directory")

def check_requirements():
    """Check if requirements are installed"""
    try:
        import flask
        import flask_sqlalchemy
        import flask_login
        print("✅ All dependencies are installed")
        return True
    except ImportError:
        print("❌ Missing dependencies. Run: pip install -r requirements.txt")
        return False

def initialize_database():
    """Initialize the database"""
    try:
        from app import app, db
        with app.app_context():
            db.create_all()
            print("✅ Database initialized successfully")
            print("📊 Database file: recipe_app.db")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False
    return True

def create_test_user():
    """Create a test user (optional)"""
    try:
        from app import app, db
        from models import User
        
        with app.app_context():
            if not User.query.filter_by(username='demo').first():
                user = User(username='demo', email='demo@example.com')
                user.set_password('demo1234')
                db.session.add(user)
                db.session.commit()
                print("✅ Test user created:")
                print("   Username: demo")
                print("   Password: demo1234")
            else:
                print("ℹ️  Test user already exists")
    except Exception as e:
        print(f"⚠️  Could not create test user: {e}")

def main():
    print("=" * 50)
    print("🍳 Recipe Share Application Setup")
    print("=" * 50)
    print()
    
    # Step 1: Create directories
    print("Step 1: Creating directories...")
    create_directories()
    print()
    
    # Step 2: Check requirements
    print("Step 2: Checking dependencies...")
    if not check_requirements():
        print("\n📦 Install dependencies with: pip install -r requirements.txt")
        sys.exit(1)
    print()
    
    # Step 3: Initialize database
    print("Step 3: Initializing database...")
    if not initialize_database():
        sys.exit(1)
    print()
    
    # Step 4: Create test user
    print("Step 4: Setting up test user...")
    create_test_user()
    print()
    
    print("=" * 50)
    print("✨ Setup complete!")
    print("=" * 50)
    print()
    print("🚀 To start the application, run:")
    print("   python app.py")
    print()
    print("📱 Access the app at: http://localhost:5000")
    print()
    print("📖 For more information, see README.md")
    print()

if __name__ == '__main__':
    main()
