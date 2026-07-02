"""
Run simple DB initialization (create tables) for the configured DATABASE_URL.

Usage:
  python scripts/run_migrations.py

This will import `app.init_db` which calls SQLAlchemy's create_all.
"""
import logging
import sys

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Running DB initialization (create tables)")
    try:
        import app.init_db  # noqa: F401 - side-effect: creates tables
        logging.info("Database initialization complete.")
    except Exception as e:
        logging.exception("Failed to initialize DB: %s", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
