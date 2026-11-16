import sqlite3
from pathlib import Path
import os

def db_path_function():
    #         Path("/home/dantepc/DealWatch") / "userdb.db"
    db_path = Path(__file__).resolve().parent / "userdb.db"
    return db_path

def connect(db_path: str) -> sqlite3.Con:
    if db_path.exists() == True:
        # Database exzists so connect to it
        con = sqlite3.connect(db_path)
        pass
    else:
        # Database doesnt exist, so create empty tables in a new database to use in program
        con = create_tables(db_path)
        
    con.execute("PRAGMA journal_mode = WAL")
    con.execute("PRAGMA foreign_keys = ON")
    return con

def create_tables(db_path: str) -> sqlite3.none:
    con = sqlite3.connect(db_path)
    cursor = con.connection()
    #Create Tables
    cursor.execute("""
CREATE TABLE marketplaces (
  id    INTEGER PRIMARY KEY,
  name  TEXT NOT NULL UNIQUE              -- 'facebook', 'ebay', 'buyee'
);

CREATE TABLE listings (
  id                INTEGER PRIMARY KEY,
  marketplace_id    INTEGER NOT NULL REFERENCES marketplaces(id),
  external_id       TEXT NOT NULL,        -- the site's own id
  search_id         INTEGER REFERENCES searches(id),
  url               TEXT NOT NULL,
  title             TEXT NOT NULL,
  description       TEXT,
  format            TEXT NOT NULL DEFAULT 'buy_now'
                    CHECK (format IN ('auction', 'buy_now')),
  ends_at           TEXT,                 -- auctions only
  status            TEXT NOT NULL DEFAULT 'new'
                    CHECK (status IN ('new', 'to_review', 'wishlisted', 'skipped', 'removed')),
  verdict           TEXT CHECK (verdict IN ('match', 'maybe', 'skip', 'excluded')),
  image_hash        TEXT REFERENCES images(hash),
  extra             TEXT,                 -- JSON
  first_seen        TEXT NOT NULL,
  last_seen         TEXT NOT NULL,
  status_changed_at TEXT,
  UNIQUE (marketplace_id, external_id)
);

CREATE TABLE price_history (
  id          INTEGER PRIMARY KEY,
  listing_id  INTEGER NOT NULL REFERENCES listings(id) ON DELETE CASCADE,
  price_cents INTEGER NOT NULL,
  bid_count   INTEGER,                    -- NULL for buy-now
  seen_at     TEXT NOT NULL
);

CREATE TABLE images (
  hash  TEXT PRIMARY KEY,
  path  TEXT NOT NULL,
  bytes INTEGER NOT NULL
);
""")


def main():
    con = connect(db_path_function())
    

main()
