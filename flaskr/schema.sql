DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS remedy;
DROP TABLE IF EXISTS remedy_potency;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  displayname TEXT NOT NULL DEFAULT ''
);

CREATE TABLE remedy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  potency_id integer NOT NULL,
  materia_medica_link TEXT NOT NULL DEFAULT '',
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE remedy_potency (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  potency TEXT NOT NULL UNIQUE
);

INSERT INTO remedy_potency (potency) VALUES ('3C');
INSERT INTO remedy_potency (potency) VALUES ('6C');
INSERT INTO remedy_potency (potency) VALUES ('12C');
INSERT INTO remedy_potency (potency) VALUES ('30C');
INSERT INTO remedy_potency (potency) VALUES ('200C');
INSERT INTO remedy_potency (potency) VALUES ('1M');
INSERT INTO remedy_potency (potency) VALUES ('10M');
INSERT INTO remedy_potency (potency) VALUES ('50M');

