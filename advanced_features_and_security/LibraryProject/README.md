# LibraryProject

This is a basic Django project setup guide for getting started with Django.

---

## 🔧 Prerequisites

- Python installed on your system (3.8 or later recommended)
- pip (Python package installer)

---

## 🚀 Steps to Set Up

### 1. Install Django

Open your terminal and run:

```bash
pip install django

## Permissions & Groups Setup

### Custom Permissions
Defined in the `Article` model (`models.py`) as:
- can_view
- can_create
- can_edit
- can_delete

### User Groups
Created via `setup_groups.py`:
- **Viewers**: Only can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: All permissions

### Views
Protected using `@permission_required` decorators:
- `book_list`: requires can_view
- `book_create`: requires can_create
- `book_edit`: requires can_edit
- `book_delete`: requires can_delete

### Testing
Create test users and assign them to different groups.
Login as each and attempt actions to confirm enforcement.

> You can also manage users, permissions, and groups from the Django Admin dashboard.
