import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

# sample data here
json = [{
    "id": 32281, 
    "title": "Kimi no Na wa.", 
    "main_picture": {"medium": "https://api-cdn.myanimelist.net/images/anime/5/87048.jpg", "large": "https://api-cdn.myanimelist.net/images/anime/5/87048l.jpg"}, 
    "start_date": "2016-08-26", 
    "mean": 8.95, 
    "media_type": "movie", 
    "status": "finished_airing", 
    "genres": [{"id": 22, "name": "Romance"}, {"id": 37, "name": "Supernatural"}, {"id": 23, "name": "School"}, {"id": 8, "name": "Drama"}], 
    "num_episodes": 1, 
    "start_season": {"year": 2016, "season": "summer"}, 
    "average_episode_duration": 6391, "rating": "pg_13", 
    "studios": [{"id": 291, "name": "CoMix Wave Films"}]
}]

# Query to execute
sql = "INSERT INTO studio (studio_id, studio_name, establishment_date) VALUES (%s, %s, %s)"

# Data to add, stored as a set, unique values only
studios = {} 

for entry in json:
    for studio in entry["studios"]:
        studios.add( (studio["id"], studio["name"]) ) # add as a tuple
        
studios = list(studios) # convert to list so that you can use executemany

# Perform sql operation
mycursor.executemany(sql, studios)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")
