CREATE TABLE IF NOT EXISTS publications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_campaign VARCHAR(255),
    id_publication VARCHAR(255) NOT NULL,
    image_prompt TEXT,
    caption TEXT,
    image LONGTEXT
);