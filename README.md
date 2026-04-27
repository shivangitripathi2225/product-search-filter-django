🛍️ Product Search & Filter API (Django + Vanilla JS)

📌 Overview

This project implements a full-stack product listing feature with search, filtering, sorting, and pagination.

🚀 Features
Backend (Django)
Search products by name (case-insensitive)

Filter by category

Sort by price (ascending/descending)

Pagination support

Input validation & error handling

JSON API response

Frontend (Vanilla JS)
Dynamic product listing

Search input

Category filter

Sorting options

Pagination controls

🏗️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, Vanilla JavaScript

Database: SQLite

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/shivangitripathi2225/product-search-filter-django.git
cd product-search-filter-django
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install django
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Create superuser (optional)
python manage.py createsuperuser
6. Run server
python manage.py runserver
7. Open in browser
http://127.0.0.1:8000/

🔌 API Endpoint
GET /products
Query Parameters:
search → search by product name

category → filter by category

sort → asc or desc

page → page number

Example:
/products?search=shirt&category=Clothing&sort=asc&page=1
Response:
{
  "products": [...],
  "total": 10,
  "page": 1,
  "page_size": 3,
  "total_pages": 4
}
⚠️ Error Handling
Invalid page → returns 400

Invalid sort → returns 400

Graceful handling of empty results

🤖 AI Usage Notes
Tools Used
ChatGPT (for architecture guidance, query building, and debugging)

Key Prompts
"How to implement filtering and pagination in Django"

"Best way to structure query params in REST API"

"Vanilla JS fetch API integration with backend"

Where AI Helped
Designing clean API structure

Implementing filtering, sorting, and pagination logic

Improving error handling

Structuring frontend API calls

Challenges / Corrections
Initial AI suggestions lacked proper validation for query params

Pagination logic was refined to ensure correct total count handling

Improved response structure for better API design