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
@app.route('/num_start')
def num_start():
    return render_template('plot.html')

@app.route('/numbers', methods=['POST'])
def numbers():
    toothpaste = request.form['ToothPaste']
    facecream = request.form['FaceCream']
    facewash = request.form['FaseWash']
    bathingsoap = request.form['BathingSoap']
    shampoo = request.form['Shampoo']
    moisturizer = request.form['Moisturizer']

    data = [float(toothpaste), float(facecream), float(facewash), float(bathingsoap), float(shampoo), float(moisturizer)]
    labels = ['ToothPaste', 'FaceCream', 'FaseWash', 'BathingSoap', 'Shampoo', 'Moisturizer']

    plt.clf()
    ax = plt.subplots()
    pie = ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    
    plt.title('Distribution of Products')  # Added title
    
    # Add legend
    ax.legend(pie[0], labels, loc="upper left", bbox_to_anchor=(0.8, 0.5))
    
    fname = './static/piechart.jpg'
    plt.savefig(fname, bbox_inches='tight')
    
    return fname
    

if __name__ == '__main__':
    app.run(debug=True)
