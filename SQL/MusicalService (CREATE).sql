-- Создание БД
CREATE DATABASE Music_Service;

-- Создание таблицы Genre
CREATE TABLE genre (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы Artist
CREATE TABLE artist (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы Artists & Genres
CREATE TABLE artists_genres (
  artist_id INT,
  genre_id INT,
  FOREIGN KEY (artist_id) REFERENCES artists(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id)
);

-- Создание таблицы Album
CREATE TABLE album (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  release_year INT NOT NULL
);

-- Создание таблицы Artists & Albums
CREATE TABLE artists_albums (
  artist_id INT,
  album_id INT,
  FOREIGN KEY (artist_id) REFERENCES artists(id),
  FOREIGN KEY (album_id) REFERENCES albums(id)
);

-- Создание таблицы Track
CREATE TABLE track (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  duration INT NOT NULL,
  album_id INT NOT NULL,
  FOREIGN KEY (album_id) REFERENCES albums(id)
);

-- Создание таблицы Compilation
CREATE TABLE compilation (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  release_year INT NOT NULL
);

-- Создание таблицы Compilations & Tracks
CREATE TABLE tracks_compilations (
  track_id INT,
  compilation_id INT,
  FOREIGN KEY (track_id) REFERENCES tracks(id),
  FOREIGN KEY (compilation_id) REFERENCES compilations(id)
);