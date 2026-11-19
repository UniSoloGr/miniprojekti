from config import db
from sqlalchemy import text

from entities.source import Source

def get_sources():
    result = db.session.execute(text("SELECT id, content FROM Sources"))
    sources = result.fetchall()
    return [Source(source[0], source[1]) for source in sources]

def create_source(content):
    sql = text("INSERT INTO Sources (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()