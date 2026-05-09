from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask App!'

# Wrapper function for HTML response
def html_response(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>About Me</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f0f0f0;
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 18px;
                    color: #555;
                }}
                img {{
                    width: 200px;
                    height: 200px;
                    border-radius: 50%;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            {content}
        </body>
        </html>
        """
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/about')
@html_response
def about():
    return """
        <h1>Hello! I am Rpalakoldu</h1>
        <p>I am a Python developer learning Flask and web development.</p>
        <p>I love building web applications and exploring new technologies.</p>
        <img src="https://avatars.githubusercontent.com/rpalakoldu-lab" 
             alt="My Profile Picture">
    """

if __name__ == '__main__':
    app.run(debug=True)