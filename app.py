from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_music')
def run_music():
    try:
        subprocess.Popen(["streamlit", "run", "music.py"], shell=True)
        return "Streamlit app started successfully!"
    except Exception as e:
        return f"Error starting Streamlit: {e}"

if __name__ == '__main__':
    app.run(debug=True)
