DROP TABLE IF EXISTS swusers;

CREATE TABLE swusers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    p4ssword TEXT NOT NULL
);


DROP TABLE IF EXISTS planet_votes;

CREATE TABLE planet_votes (
    id SERIAL PRIMARY KEY,
    planet_id INT,
    user_id INT REFERENCES swusers (id),
    submission_time TIMESTAMP
);
