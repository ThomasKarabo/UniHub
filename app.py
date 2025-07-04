from flask import Flask, render_template, jsonify

app = Flask(__name__)

resource = {
  "id": "res_001",
  "title": "Introduction to Algorithms",
  "type": "textbook",
  "description": "Comprehensive guide to algorithms...",
  "category": "Computer Science",
  "format": "PDF",
  "thumbnail": "/thumbnails/books/algo.jpg",
  "url": "/downloads/books/algo.pdf",
  "uploadDate": "2024-03-15"
}

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/home/resources/api')
def resource_api():
    data = resource
    return jsonify(resource)

@app.route('/home/resources')
def resource_page():
    return render_template('resource_page.html')

@app.route('/home/resources/your_notes')
def resources():
    return render_template('resources.html')

@app.route('/home/opportunities')
def opportunities():
    return render_template('opportunities.html')

@app.route('/home/community')
def community():
    return '<p>Community page is under construction.</p>'

@app.route('/home/mentorship')
def mentorship():
    return '<p>Mentorship page is under construction.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
