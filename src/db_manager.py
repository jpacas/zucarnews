# db_manager.py

import sqlite3

def setup_database(db_path):
    """Crea la base de datos si no existe."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noticias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            source TEXT NOT NULL,
            published_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_news_to_db(db_path, noticias):
    """Guarda noticias en la base de datos."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for noticia in noticias:
        try:
            cursor.execute("""
                INSERT INTO noticias (title, url, source, published_at)
                VALUES (?, ?, ?, ?)
            """, (noticia["title"], noticia["url"], noticia["source"], noticia.get("published_at")))
        except sqlite3.IntegrityError:
            # Ignorar entradas duplicadas
            pass
    
    conn.commit()
    conn.close()
