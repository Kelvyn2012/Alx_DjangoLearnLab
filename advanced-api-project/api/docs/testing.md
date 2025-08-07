🧪 Testing Strategy for Book API
🔧 Purpose
The purpose of this test suite is to validate that the Book API endpoints are working correctly, return the right data, and enforce proper authentication and permissions.

✅ Testing Framework
Framework: Django’s built-in unittest

Test Command:

bash
Copy
Edit
python manage.py test api
Test File Location:
api/test_views.py

Environment:
Tests run on a temporary database that is created and destroyed automatically, ensuring your main database remains untouched.

📂 Individual Test Cases
1. Book List Test
What it does: Sends a GET request to /books/

Checks:

Status code is 200 OK

Response returns a list of books

Valid for authenticated and unauthenticated access (if IsAuthenticatedOrReadOnly is used)

### Authentication in Tests

These tests use **TokenAuthentication** rather than session-based login, so instead of `self.client.login()`, we:

- Create a user and token in `setUp()`
- Attach the token using `self.client.credentials(...)`
- Use `force_authenticate(user=None)` to simulate unauthenticated users

This ensures each test runs independently and securely against a test database.


2. Book Detail Test
What it does: Sends a GET request to /books/<id>/

Checks:

Status code is 200 OK

Book details match the one created

Returns 404 if ID doesn't exist

3. Book Creation Test
What it does: Sends a POST request to /books/create/ with book data

Checks:

Status code is 201 CREATED

Response data matches input

Fails if no authentication token is provided

4. Book Update Test
What it does: Sends a PUT or PATCH request to /books/update/<id>/

Checks:

Status code is 200 OK

Fields are updated correctly

Fails without authentication or invalid ID

5. Book Delete Test
What it does: Sends a DELETE request to /books/delete/<id>/

Checks:

Status code is 204 NO CONTENT

Book is removed from the database

Fails without authentication

6. Filtering Test
What it does: Appends query parameters like ?author=1 to the URL

Checks:

Only books by that author are returned

7. Search Test
What it does: Appends ?search=keyword to /books/

Checks:

Returns books matching the keyword in the title or author name

8. Ordering Test
What it does: Appends ?ordering=publication_year to /books/

Checks:

Response is sorted by the requested field

9. Permission Test
What it does: Tries to POST, PUT, or DELETE without a token

Checks:

Returns 401 UNAUTHORIZED

▶️ How to Run the Tests
Make sure your virtual environment is active

Navigate to your project folder

Run the command:

bash
Copy
Edit
python manage.py test api
📈 Interpreting the Results
✅ Dot (.) — A test passed

❌ F — A test failed (you’ll get details on which one and why)

🔥 E — An error occurred (e.g., missing field, bad setup)

Sample Output:
bash
Copy
Edit
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in 9.922s

OK
Destroying test database for alias 'default'...