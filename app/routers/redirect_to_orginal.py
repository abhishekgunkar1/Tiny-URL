from flask import request, redirect
from app import app
from ..redis_db_conn import redis_client

# Route to redirect to a particular shortened url if found
@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    original_url = redis_client.get(short_url)

    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found", 404