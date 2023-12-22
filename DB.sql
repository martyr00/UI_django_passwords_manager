.open project.db

BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "account" (
	"id_account"	INTEGER NOT NULL UNIQUE,
	"login"	TEXT,
	"password"	TEXT,
	"email"	TEXT,
	"website"	TEXT,
	"id_category"	INTEGER,
	PRIMARY KEY("id_account" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "category" (
	"id_category"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id_category" AUTOINCREMENT)
);
COMMIT;