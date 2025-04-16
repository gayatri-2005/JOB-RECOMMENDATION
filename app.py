from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # You can put any random string here

# Allowed resume file formats
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Check file type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        file = request.files.get("resume")
        if not file or file.filename == "":
            flash("Please upload a file.")
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Optional: file.save(os.path.join("uploads", filename))

            # Simulated roles extracted from resume
            job_roles = [
                "Data Science Intern", "Machine Learning Intern", "AI Engineer",
                "Backend Developer", "Frontend Developer", "Full Stack Developer",
                "Cloud Engineer", "Cybersecurity Intern", "Software Engineer",
                "Business Analyst", "DevOps Intern", "Data Analyst",
                "QA Engineer", "UI/UX Designer", "Android Developer"
            ]
            return render_template("results.html", job_roles=job_roles)
        else:
            flash("Unsupported file type. Please upload PDF or DOCX.")
            return redirect(request.url)

    return render_template("index.html")

@app.route("/submit-jobs", methods=["POST"])
def submit_jobs():
    selected_roles = request.form.getlist("selected_roles")
    job_type = request.form.get("job_type")
    work_mode = request.form.get("work_mode")
    location = request.form.get("location")

    if not selected_roles:
        flash("Please select at least one job role.")
        return redirect(url_for("upload_resume"))

    # Simulated job listings (can be replaced by real API)
    listings = []
    for role in selected_roles:
        listings.append({
            "title": f"{role} ({job_type})",
            "company": "Example Corp",
            "location": location if location else work_mode,
            "salary": "₹4,00,000 - ₹10,00,000 (Approx)",
            "description": f"We are hiring a {role.lower()} to join our dynamic team.",
            "qualifications": "Bachelor’s degree in a relevant field, strong communication skills.",
            "link": "https://example.com/apply"
        })

    return render_template("job_results.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)
