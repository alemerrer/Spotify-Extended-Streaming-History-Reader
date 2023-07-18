import sys
import json
import mysql.connector
import os
from datetime import datetime


sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="spotify"
)

mycursor = mydb.cursor()
null = None
true = 1
false = 0

def import_track(filename):
    f = open(filename,encoding="utf8")
    data = json.load(f)

    for i in data:
        if i['master_metadata_track_name'] != null and i['master_metadata_album_artist_name'] != null:
            date = i['ts']
            formattedDate = datetime.fromisoformat(date[:-1] + '+00:00')

            print(i['master_metadata_track_name'] + ' - ' + i['master_metadata_album_artist_name'])
            sql = 'INSERT INTO audio (ts,username,platform,ms_played,conn_country,ip_addr_decrypted,user_agent_decrypted,master_metadata_track_name,master_metadata_album_artist_name,master_metadata_album_album_name,spotify_track_uri,episode_name,episode_show_name,spotify_episode_uri,reason_start,reason_end,shuffle,skipped,offline,offline_timestamp,incognito_mode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (formattedDate,i['username'],i['platform'],i['ms_played'],i['conn_country'],i['ip_addr_decrypted'],i['user_agent_decrypted'],i['master_metadata_track_name'],i['master_metadata_album_artist_name'],i['master_metadata_album_album_name'],i['spotify_track_uri'],i['episode_name'],i['episode_show_name'],i['spotify_episode_uri'],i['reason_start'],i['reason_end'],i['shuffle'],i['skipped'],i['offline'],i['offline_timestamp'],i['incognito_mode'])
            mycursor.execute(sql, val)
            mydb.commit()

    f.close()

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".json"):
        print('-------------------')
        print('Importing ' + filename)
        import_track(filename)


#select count(*), a.master_metadata_album_artist_name, a.master_metadata_track_name  from spotify.audio a group by a.master_metadata_album_artist_name, a.master_metadata_track_name
#select count(*), a.master_metadata_album_artist_name  from spotify.audio a group by a.master_metadata_album_artist_name
#select count(*), a.master_metadata_album_artist_name , a.master_metadata_album_album_name     from spotify.audio a group by master_metadata_album_album_name  

