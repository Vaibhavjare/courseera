from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Logic to handle form data (e.g., store in DB, send email)
        if name and email and message:
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for('home'))  # Redirect to avoid form resubmission
        else:
            flash("All fields are required. Please try again.", "error")

    home_info = {
        "name": "Vaibhav Jare",
        "profession": "Data Scientist",
        "description": (
            "I’m Vaibhav Jare, a data scientist skilled in machine learning, data analysis, "
            "and Python programming. I develop innovative solutions, focusing on impactful "
            "projects like medicinal plant identification and augmented reality. My goal is to use "
            "data to drive decisions and create user-friendly applications."
        ),
        "image_path": "static/images/vaibhav.png"
    }

    about_info = {
        "name": "Vaibhav R Jare",
        "title": "Data Scientist",
        "description": "Hi, I’m Vaibhav Jare, a data scientist and computer engineering student with a passion for leveraging data to solve real-world problems. I specialize in machine learning, Python programming, and developing innovative applications like medicinal plant identification and augmented reality. My goal is to use my technical skills to create impactful, user-centric solutions that drive meaningful change.",
        "personal_info": {
            "Birthday": "20 Aug 2003",
            "Age": "21",
            "Website": "www.domain.com",
            "Email": "vaibhavjare07@gmail.com",
            "Degree": "B.Tech In Computer Science",
            "Phone": "+91 8805870316",
            "City": "Dhule"
        },
        "skills": [
            {"name": "Python", "level": 90},
            {"name": "C++", "level": 90},
            {"name": "C", "level": 90},
            {"name": "SQL", "level": 85},
            {"name": "MongoDB", "level": 70},
            {"name": "AI", "level": 50}
        ],
        "education": [
            {
                "period": "2021-2025",
                "degree": "B.Tech In Computer Science",
                "details": "Pursuing a B.Tech in Computer Engineering from SVKM’s IOT, Dhule, under DBATU. Gained expertise in Python, C++, C, and hands-on experience in web development, data science, and machine learning."
            }
        ],
        "experience": [
            {
                "period": "2022-2023",
                "role": "Intern",
                "details": "Worked at AIWIZ Tech Solution Pvt. Ltd. and Infotech Incorporate, gaining practical exposure to data science and web development."
            }
        ]
    }

    services_data = [
        {"icon": "fa fa-laptop-code", "title": "Data Analysis", "description": "Insights through visualizations and reports"},
        {"icon": "fa fa-code", "title": "Machine Learning", "description": "Custom models for predictions and analytics"},
        {"icon": "fa fa-mobile-alt", "title": "Web Development", "description": "User-friendly websites"},
        {"icon": "fa fa-palette", "title": "Database Administration", "description": "Efficient database design, management, and optimizations"},
        {"icon": "fa fa-search", "title": "Search Optimization", "description": "Optimize your application for better discoverability"},
        {"icon": "fa fa-bullhorn", "title": "Marketing Analytics", "description": "Analyze campaigns and customer insights"},
    ]

    
    portfolio_projects = [
        {"image": "static/images/portfolio/project-1.png", "title": "Project 1", "description": "Description of Project 1"},
        {"image": "static/images/portfolio/project-2.png", "title": "Project 2", "description": "Description of Project 2"},
        {"image": "static/images/portfolio/project-3.png", "title": "Project 3", "description": "Description of Project 3"},
        {"image": "static/images/portfolio/project-4.png", "title": "Project 4", "description": "Description of Project 4"},
        {"image": "static/images/portfolio/project-5.png", "title": "Project 5", "description": "Description of Project 5"},
        {"image": "static/images/portfolio/project-6.png", "title": "Project 6", "description": "Description of Project 6"},
    ]
    return render_template('index.html', about_info=about_info, home_info=home_info, services=services_data,projects=portfolio_projects)

if __name__ == '__main__':
    app.run(debug=True)
