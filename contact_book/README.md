# Django Contact Book

A modern, user-friendly contact management system built with Django and Bootstrap.

## Features

- **User Authentication**: Secure login system for personalized contact management
- **CRUD Operations**: Create, Read, Update, and Delete contacts
- **Search Functionality**: Search contacts by name, email, or phone number
- **Responsive Design**: Clean, modern UI built with Bootstrap 5
- **Contact Details**: Store names, emails, phone numbers, addresses, and notes
- **Pagination**: Efficient handling of large contact lists

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create a Superuser

```bash
python manage.py createsuperuser
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

- Open your browser and go to `http://127.0.0.1:8000/`
- Login with your superuser credentials
- Start adding contacts!

## Usage

### Adding Contacts
1. Click "Add Contact" in the navigation
2. Fill in the contact details
3. Click "Create Contact"

### Searching Contacts
1. Use the search bar on the main page
2. Search by name, email, or phone number
3. Results are filtered in real-time

### Managing Contacts
- **View**: Click "View" to see full contact details
- **Edit**: Click "Edit" to modify contact information
- **Delete**: Click "Delete" to remove a contact (with confirmation)

## Project Structure

```
contact_book/
├── contact_book/          # Main project settings
├── contacts/              # Contacts app
│   ├── models.py         # Contact model
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms
│   ├── urls.py           # URL routing
│   └── templates/        # HTML templates
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Model Fields

The Contact model includes:
- `first_name`: Contact's first name
- `last_name`: Contact's last name
- `email`: Email address (validated)
- `phone_number`: Phone number (validated format)
- `address`: Optional address field
- `notes`: Optional notes field
- `user`: Foreign key to User (for personalization)
- `created_at`: Timestamp when contact was created
- `updated_at`: Timestamp when contact was last updated

## Technologies Used

- **Django 5.2.6**: Web framework
- **Bootstrap 5**: Frontend CSS framework
- **Font Awesome**: Icons
- **SQLite**: Default database (easily configurable for production)

## Customization

### Adding New Fields
1. Modify the `Contact` model in `contacts/models.py`
2. Update the `ContactForm` in `contacts/forms.py`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Update templates as needed

### Styling
- Modify `contacts/templates/contacts/base.html` for global styles
- Individual templates can be customized for specific pages

## Production Deployment

For production deployment:
1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure proper security settings
5. Use environment variables for sensitive data

## License

This project is open source and available under the MIT License.
