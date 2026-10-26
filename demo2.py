from flask import Flask, render_template_string

app = Flask(__name__)

page = """
<h1>Welcome, {{ name }}</h1>

<p>This page is dynamically generated using Python Flask.</p>

<button onclick="alert('Welcome to the Dynamic Web Page!');
document.getElementById('out').innerText =
'Button clicked at ' + new Date().toLocaleTimeString()">
Click Me
</button>

<p id="out"></p>
"""

@app.route("/")
def home():
    return render_template_string(
        page, name="PG Computer Science Student"
    )

if __name__ == "__main__":
    app.run(debug=True)
