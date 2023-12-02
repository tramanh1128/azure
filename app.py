from flask import Flask, request, session
import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'
show_time = []
@app.route("/")
def hello():
    return "Index Page"
@app.route('/access_times')
def index():
    # Get the visitor's IP address
    ip_address = request.remote_addr

    # Generate a unique token for this page load
    page_token = str(uuid.uuid4())

    # Record the access time in the session
    current_time = datetime.datetime.now()
    access_times = session.get('access_times', [])
    access_times.append((page_token, ip_address, current_time))
    session['access_times'] = access_times

    # Display the access time to the visitor
    formatted_time = current_time.strftime('%a %b %d %Y %H:%M:%S')
    
    show_time.append(formatted_time)
    response = "<h2>Access Times:</h2>"
    for x in show_time:
        response += f"<p>{x}</p>"
    return response
    

if __name__ == '__main__':
    app.run(debug=True)
