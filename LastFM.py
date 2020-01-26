'''
Provide a solution to the questions below. For each question, describe your solution and its limitations.
1- Create a list of user IDs, along with the number of distinct songs each user has played.
2- Create a list of the 100 most popular songs (artist and title) in the dataset, with the number of times each was played.
3- Say we define a user’s “session” of Last.fm usage to be comprised of one or more songs played by that user,
where each song is started within 20 minutes of the previous song’s start time. Create a list of the top 10 longest sessions,
with the following information about each session: userid, timestamp of first and last songs in the session, and the list of songs
played in the session (in order of play).
'''

#Import the data
import csv
import pandas as pd


Data_Location = 'C:/Users/Dinesh/Downloads/userid-timestamp-artid-artname-traid-traname.tsv'

Count = 1
Data_List = []
with open(Data_Location, encoding="utf8") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      Count = Count+1
      Data_List.append(row)
      if Count==100000:
          break

#Remove count for full dataset. Scales as expected.

ids = [item[0] for item in Data_List]

unique_id = []

def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print(x)
        unique_id.append(x)

unique(ids)

dict = {}

for id in unique_id:
    dict['%s' % id] = []
    for sublist in Data_List:
        if id in sublist:
            dict[id].append(sublist[5])


len(dict['user_000003'])
# Length is 19494


Final_List = {}
unique_songs = []

#for id in unique_id:
#    dict['%s' % id] = []


for userid in dict:
    Final_List['%s' % userid] = []
    a = []
    for each_song in dict[userid]:
        if each_song not in a:
            a.append(each_song)
            Final_List[userid].append(each_song)

#Final List
#The list of user ID's is contained here:
for userid in dict:
    print(userid)

#The user ID within quotation marks below can then be replaced with another users ID
# to return the list of songs that that specific user has played. i.e:

Answer1 = {}

for i in Final_List:
    Answer1[i] = i

for each_user in unique_id:
    Answer1.update( {each_user : len(Final_List[each_user])} )

Answer1

#Question 2
QuestionTwo = Data_List.copy()
songs = []
for row in QuestionTwo:
    songs.append(row[5])

#unique_id = []
#unique(songs)


from collections import Counter
cnt = Counter()
for song in songs:
    cnt[song] += 1

cnt.keys()

Top_Songs = cnt.most_common(100)

count = 1
for i in Top_Songs:
    count = count + 1

    if count == 5:
        break

type(cnt.most_common(100))

Top_100 = []
count = 1

for k,v in cnt.most_common():
    count = count + 1
    print(k)
    name_song = k
    Top_100.append(name_song)
    #Top_100.append(k)
    if count == 101:
        break


Songs_with_Artist = {}
count = 1

for i in Top_100:
    Songs_with_Artist['%s' % i] = []
        for each_entry in QuestionTwo:
            if i in each_entry:
                Songs_with_Artist[i].append(each_entry[3])

Times_Played = []
Question2Dict = {}

len(Songs_with_Artist)
Name_of_Artist = []

for each_song in Songs_with_Artist:
    Name_of_Artist.append(Songs_with_Artist[each_song][0])


len(Name_of_Artist)



for each_artist in Songs_with_Artist:
    Question2Dict.update( {Songs_with_Artist[each_artist][0] : each_artist} )

#Artist Name and Song
# each_artist in Songs_with_Artist:
#    Question2Dict[each_artist].append(len(Songs_with_Artist[each_artist]))

Artist = []
for each_artist in Name_of_Artist:
    Artist.append(each_artist)



Question_2_Answer = pd.DataFrame()

Question_2_Answer["Artist"] = Artist

len(Question_2_Answer)

Song_name = []
for each_artist in Artist:
    Song_name.append(Question2Dict[each_artist])

Question_2_Answer["Song Name"] = Song_name

Times_Song_Played = []
for each_song in Songs_with_Artist:
    Times_Song_Played.append(len(Songs_with_Artist[each_song]))

len(Times_Song_Played)
Question_2_Answer["Times Played"] = Times_Song_Played

#Question 3
QuestionThree = Data_List.copy()
ids = [item[0] for item in QuestionThree]

unique_id = []
unique(ids)

for id in unique_id:
    dict['%s' % id] = []
    for sublist in QuestionThree:
        if id in sublist:
            dict[id].append(sublist[1])

unique_id

from datetime import datetime

counter = 1

import datetime
from datetime import date

list1 = []
step_ahead = []
counter = 1


for each_user in unique_id:
    for time in dict[each_user]:
        dict[each_user] = pd.to_datetime(dict[each_user])

count = 1
for each_user in unique_id:
    count = count + 1
    for time in dict[each_user]:
        print(type(time))
        if count == 5:
            break

dict
copy_dict = dict
test_data = dict
from datetime import timedelta

a = dict["user_000001"][0] - dict["user_000001"][1]
Longest_Session = {}

count = 1

dict

'''
test_data = {"user_000004": [timedelta(days=0, hours=1, minutes=59, seconds=0, microseconds=0),
                             timedelta(days=0, hours=1, minutes=49, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=49, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=43, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=42, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=41, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=30, seconds=0, microseconds=0),
                             timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0),
                             timedelta(days=0, hours=0, minutes=39, seconds=0, microseconds=0)]}
'''


test_user = ["user_000004"]
#the difference is recorded in seconds

test_data["user_000004"][0] - test_data["user_000004"][2]

m = timedelta(days=-1, hours=23, minutes=30, seconds=0, microseconds=0)

for each_user in dict:
    Longest_Session[each_user] = timedelta(days=0, hours=0, minutes=0, seconds=0, microseconds=0)

#Longest_Session.update( {'user_000004' : timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0)} )

for each_user in dict:
    Session_Length = timedelta(days=0, hours=0, minutes=0, seconds=0, microseconds=0)
    Session_ID = 1
    for i,k in zip(test_data[each_user][0::1], test_data[each_user][1::1]):
        c = i - k
        print(c)
        if c.total_seconds() <= 0:
            print("Starting a new session")
            current_val = Longest_Session[each_user]
            if Session_Length > current_val:
                print("Updating Longest Session for %s to:" %each_user)
                print("%s" %Session_Length)
                Longest_Session.update( {each_user : Session_Length} )
        if c  <= timedelta(days=0, hours=0, minutes=0, seconds=1200, microseconds=0):
            Session_Length = Session_Length + c
            print("Adding to current session")
        else:
            current_val = Longest_Session[each_user]
            if Session_Length > current_val:
                print("Updating Longest Session for %s to:" %each_user)
                print("%s" %Session_Length)
                username = each_user
                Longest_Session.update( {each_user : Session_Length} )
