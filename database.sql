CREATE DATABASE MovieDB;

USE MovieDB;
CREATE TABLE Actors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT
);

CREATE TABLE Movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    year INT
);

INSERT INTO Actors (name, age) VALUES
('Tom Hanks', 66),
('Meryl Streep', 73),
('Leonardo DiCaprio', 48),
('Scarlett Johansson', 38),
('Denzel Washington', 68);

INSERT INTO Movies (title, year) VALUES
('The Shawshank Redemption', 1994),
('The Godfather', 1972),
('The Dark Knight', 2008),
('Pulp Fiction', 1994),
('Forrest Gump', 1994);

SELECT * FROM Actors;
SELECT * FROM Movies;
SELECT * FROM Movies WHERE year = 1994;
SELECT * FROM Actors WHERE age > 50;

-- Create a junction table
CREATE TABLE MovieActors (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (actor_id) REFERENCES Actors(id)
);