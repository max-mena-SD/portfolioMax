from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.jpg",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "flask"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Micro-blog app with Python and MongoDB",
        "thumb": "img/micro-blog.jpg",
        "hero": "img/micro-blog-hero.jpg",
        "categories": ["python", "flask"],
        "slug": "personal-finance",
    },
    {
        "name": "Ejemplos interesantes",
        "thumb": "img/ejemplos-interesantes.jpg",
        "hero": "img/ejemplos-interesantes-hero.jpg",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

slug_to_project= {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.jinja2", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
