from flask import Flask
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, template_folder="frontend")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h2>About the Program</h2><p>A 2-day full-stack bootcamp covering HTML, CSS, Python, SQL, and deployment.</p>"

'''
@app.route("/register", methods=["POST"])
#def register():
    return "<h2>📨 Registration Received</h2><p>Form data will be processed/p>"
'''
@app.route("/register", methods=["POST"])
def register():
    
    full_name = request.form.get("full_name", "").strip()
    email = request.form.get("email", "").strip().lower()
    course = request.form.get("course", "")
    enroll_date = request.form.get("enroll_date", "")
    phone = request.form.get("phone", "").strip()
    remarks = request.form.get("remarks", "").strip()

    errors = []
    if not full_name or len(full_name) < 2:
        errors.append("Full name must be at least 2 characters.")
    if not email or "@" not in email:
        errors.append("Valid email address is required.")
    if not course:
        errors.append("Please select a course.")
    
    if errors:
        return f"<h2>Validation Failed</h2><ul>{''.join(f'<li>{e}</li>' for e in errors)}</ul><a href='/'>Go Back</a>", 400

    # 3. Process & Log (Placeholder for DB insertion)
    submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"NEW REGISTRATION: {full_name} | {email} | {course} | {enroll_date} | {phone}")
    
    # 4. Return Success Response
    return f"""
        <h2>Registration Successful!</h2>
        <p>Thank you, <strong>{full_name}</strong>!</p>
        <p><strong>Email:</strong> {email}<br>
        <strong>Course:</strong> {course}<br>
        <strong>Enrollment:</strong> {enroll_date or 'Not specified'}<br>
        <strong>Submitted:</strong> {submission_time}</p>
        <hr>
        <p><em>Remarks:</em> {remarks if remarks else 'None provided'}</p>
        <a href="/"><button>Register Another Student</button></a>
    """, 200
if __name__ == "__main__":
    app.run(debug=True, port=8000)