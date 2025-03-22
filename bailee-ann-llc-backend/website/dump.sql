CREATE TABLE users (
	id SERIAL,
	email VARCHAR(150) NOT NULL, 
	password VARCHAR(150) NOT NULL,
	first_name VARCHAR(150) NOT NULL,	
	PRIMARY KEY (id),
	UNIQUE (email)   
);

INSERT INTO users VALUES
(1, 'test@test.test', 'pbkdf2:sha256:1000000$WqbXd6LnBJuTiD45$94d10cd62078594224dcc30b101a7d34efc4046da699364c0999a0adbf581d5a', 'test'),
(2, 'test1@test2.test3', 'pbkdf2:sha256:1000000$WBQa5q1SWtY8xFhP$5f62fd295b7f6746f65ef6b27f58559fb7f952a29b5e5e0420aa7e55cf6cbd05', 'testtteee');

CREATE TABLE note (
	id SERIAL,
	data VARCHAR(10000),
	date TIMESTAMP DEFAULT NOW(),
	user_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
);

