-- Вставка исполнителей
INSERT INTO artists (name)
VALUES
('NeoNate'),
('Parkway Drive'),
('ТонкаяКраснаяНить'),
('Insomnium'),
('Omnium Gatherum'),
('Xe-None'),
('Within Temptation'),
('Unheilig'),
('Lake Of Tears'),
('Lacrimosa'),
('Letzte Instanz'),
('Schelmish'),
('In Extremo'),
('Ышо-Ышо'),
('Zatknись'),
('Тараканы'),
('90-60-90'),
('Слот'),
('Haloscript'),
('Lunatica');

-- Вставка жанров
INSERT INTO genres (name)
VALUES
('Metalcore'),
('Death Metal'),
('Melodic Metal'),
('Symphonic Metal'),
('Industrial Metal'),
('Gothic Metal'),
('Doom Metal'),
('Medieval Metal'),
('Punk Rock'),
('Nu Metal'),
('Dance Metal');

-- Вставка альбомов
INSERT INTO albums (name, release_year)
VALUES
('Dancefloration', 2011),
('Mother Earth', 2001),
('В Маске', 2011),
('Ire', 2015),
('Across The Dark', 2009),
('The Redshift', 2008),
('Headstones', 1995),
('Sünder Ohne Zügel', 2001),
('Ins Licht', 2006),
('Wir Werden Sehen', 2007);

-- Вставка треков
INSERT INTO tracks (name, duration, album_id)
VALUES
('Vice Grip', 0424, 4),
('Against The Stream', 0612, 5),
('A Shadowkey', 0430, 6),
('I Seek You', 0353, 1),
('Mother Earth', 0531, 2),
('Headstones', 0516, 7),
('Save My Life', 0237, 11);

-- Вставка сборников
INSERT INTO compilations (name, release_year)
VALUES
('Best Of Metal', 2007),
('Best Of Best', 2017),
('Mixed', 2023),
('Need For Speed', 2020),
('Impossible Mix', 2019);

-- Связка исполнителей и альбомов
INSERT INTO artists_albums (artist_id, album_id)
VALUES
(1, 3),
(2, 4),
(4, 5),
(5, 6),
(6, 1),
(7, 2),
(9, 7),
(11, 9),
(12, 10),
(13, 8);

-- Связка исполнителей и жанров
INSERT INTO artists_genres (artist_id, genre_id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(4, 3),
(5, 2),
(6, 11),
(7, 4),
(8, 6),
(9, 6),
(10, 6),
(11, 8),
(12, 8),
(13, 8),
(14, 9),
(15, 9),
(16, 9),
(17, 9),
(18, 10),
(19, 10),
(20, 4);

-- Связка треков и сборников
INSERT INTO tracks_compilations (track_id, compilation_id)
VALUES
(1, 1),
(3, 1),
(5, 1),
(2, 2),
(4, 2),
(6, 2),
(1, 3),
(2, 3),
(3, 3),
(4, 4),
(5, 4),
(6, 4),
(2, 4),
(1, 5),
(2, 5),
(3, 5),
(4, 5),
(5, 5),
(6, 5);