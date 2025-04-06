import mysql.connector

class PublicationSaver:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="mysql",
            port=3306,
            user="myuser",
            password="mypassword",
            database="mydatabase"
        )
        self.cursor = self.conn.cursor()

    def save_publication(self, publication: dict):
        sql = """
        INSERT INTO publications (id_campaign, id_publication, image_prompt, caption, image)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            publication.get("id_campaign"),
            publication.get("id_publication"),
            publication.get("image_prompt"),
            publication.get("caption"),
            publication.get("image")
        )

        self.cursor.execute(sql, values)
        self.conn.commit()
    
    def get_publications(self):
        sql = "SELECT id_campaign, id_publication, image_prompt, caption, image FROM publications"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        publications = []
        for row in rows:
            publication = {
                "id_campaign": row[0],
                "id_publication": row[1],
                "image_prompt": row[2],
                "caption": row[3],
                "image": row[4]
            }
            publications.append(publication)

        return publications

    def close(self):
        self.cursor.close()
        self.conn.close()