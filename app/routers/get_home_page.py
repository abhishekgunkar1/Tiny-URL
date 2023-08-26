from flask import render_template, request, redirect, url_for
from app import app
from ..shorten_url import generate_short_url
from ..redis_db_conn import redis_client
from ..constants import HOST_NAME

# Route that generates the shortened URL and that display 
# the HTML template
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the original URL
        original_url = request.form['url']
        # Generates the ID which is the shortened URL
        short_url = generate_short_url(original_url)

        # Store the mapping in Redis
        redis_client.set(short_url, original_url)
        
        # Display the template HTML with the generated url
        return render_template('index.html', short_url=short_url, host_url = HOST_NAME)

    return render_template('index.html')