from flask import render_template, request, redirect, flash
from repositories.source_repository import get_sources, create_source
from config import app

@app.route("/")
def index():
    search_name = request.args.get("q", "").strip()
    sources = get_sources()
    if search_name:
        query = search_name.casefold()
        sources = [source for source in sources if query in source.content.casefold()]
    return render_template("index.html", sources=sources, search_name=search_name)

@app.route("/sources")
def source_view():
    sources = get_sources()
    return render_template("source_view.html", sources=sources)

@app.route("/new_source")
def new():
    return render_template("new_source.html")

@app.route("/add_source", methods=["POST"])
def add_source():
    reference_type = request.form.get("reference_type", "book")
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    year = request.form.get("year", "").strip()
    publisher = request.form.get("publisher", "").strip()
    isbn = request.form.get("isbn", "").strip()

    custom_names = request.form.getlist("custom_field_names[]")
    custom_values = request.form.getlist("custom_field_values[]")

    if not title or not author:
        flash("Title and author are required")
        return redirect("/new_source")

    # Temporary representation
    content = (
        f"Type: {reference_type}\n"
        f"Title: {title}\n"
        f"Author: {author}\n"
        f"Year: {year}\n"
        f"Publisher: {publisher}\n"
        f"ISBN: {isbn}\n"
    )

    for name, value in zip(custom_names, custom_values):
        if name.strip():
            content += f"{name.strip()}: {value.strip()}\n"

    create_source(content)
    return redirect("/")