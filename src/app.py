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
def source_addition():
    content = request.form["abstract"]

    try:
        create_source(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_source")