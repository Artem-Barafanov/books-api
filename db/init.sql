CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL
);

INSERT INTO books (title, author) VALUES
('War and Peace', 'Leo Tolstoy'),
('Crime and Punishment', 'Fyodor Dostoevsky'),
('The Master and Margarita', 'Mikhail Bulgakov');
