import csv
from csv import writer
from csv import reader
#set which user is needed
userID = 1

#create new csv with genre cols
genres = ['Action', 'Romance', 'School', 'Supernatural', 'Adventure', 'Drama', 'Magic', 'Military', 'Shounen', 'Comedy', 'Historical', 'Parody', 'Samurai', 'Sci-Fi', 'Thriller', 'Sports', 'Super Power', 'Space', 'Slice of Life', 'Mecha', 'Music', 'Mystery', 'Seinen', 'Fantasy', 'Martial Arts', 'Vampire', 'Shoujo', 'Horror', 'Police', 'Psychological', 'Demons', 'Josei', 'Shounen Ai', 'Ecchi', 'Dementia', 'Harem', 'Game', 'Cars', 'Kids', 'Shoujo Ai', 'Hentai', 'Yuri', 'Yaoi']
#userRatings : order will be alternating (anime ID , rating, anime ID, rating, ...)
userRatings = [] 
#userTotals : Totals for User enjoyment per category / totals correlate to the genre in the same position of the genres[] array
userTotals = [0] * 43

#get rated anime ids and ratings
with open('rating.csv', newline='', encoding="utf8") as ratings:
    for row in ratings:
        if row[0] == 'u':
            continue
        array = row.split(",") #split to seperate individual items for comparison
        if int(array[0]) == userID:
            userRatings.append(array[1])
            rate = array[2].split() #split because it had \r\n after the rating
            userRatings.append(rate[0])


with open('anime.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        array = row[2]
        showGenres = array.split(",")
        for spot in range(1,len(showGenres)): #taking space off begining of each genre
            string = showGenres[spot] 
            string = string[1:]
            showGenres[spot] = string
        for i in range(0, len(userRatings), 2): #calculating totals for specific user
            if int(userRatings[i+1]) == int(-1): # dont include stuff the user rated -1 (assuming it means no rating)
                continue
            else:
                if  row[0] == userRatings[i]:
                    for genre in showGenres:
                        count = 0
                        for x in genres:
                            if genre in genres[count]:
                                userTotals[count] = int(userTotals[count]) + (int(userRatings[i+1]) - 5)
                                break
                            count = count + 1
                            continue
                        
with open('anime.csv', newline='', encoding="utf8") as read_obj, \
        open('userRates.csv', 'w',newline='',encoding="utf8") as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list

    count = 0
    for row in csv_reader:
        
        total = 0
        # Append the default text in the row / list
        if count == 0:
            strUser = str(userID)
            row.append('User' + strUser + 'Interest') # add title for new col and only want it to happen once
            count = count + 1
            continue
        else:
            array = row[2]
            showGenres = array.split(",")
            for genre in showGenres:
                for i in range(0, len(genres)):
                    if genre in genres[i]:
                        total = total + int(userTotals[i])
            row.append(total)
        # Add the updated row / list to the output file
        csv_writer.writerow(row)    


    
        
