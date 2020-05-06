import requests

# Api variables
client_id = 'YOUR CLIENT ID HERE'
user_id = "YOUR USER ID HERE"
query_amount = 200 # Soundcloud doesn't seem to display more than 200 likes per query
query_offset = 0

# Custom variables
likes_counter = 0
artist_list = []
genre_list = []

# Doing the API query
print('[+] Querying the API:')
while query_offset or query_offset == 0:
    url = 'https://api-v2.soundcloud.com/users/' + user_id + '/track_likes?client_id=' + client_id + '&limit=' + str(query_amount) + '&offset=' + str(query_offset)
    json_output = requests.get(url).json()

    # Looping over the liked tracks
    for i in json_output['collection']:
        artist_list.append(i['track']['user']['username'])
        genre_list.append(i['track']['genre'])
        likes_counter += 1

    print('Likes Retrieved: ' + str(likes_counter))

    # Getting the offset for the next API query
    if json_output['next_href'] != None:
        query_offset = json_output['next_href'].replace('&limit', 'offset=').split('offset=')[1]
    else:
        print('\n[+] All Likes Retrieved [+]\n')
        query_offset = None

def get_frequency(mode):
    print('[+] Calculating Frequency [+]')
    frequency_list = {}

    # Counting the frequency into a dictionary
    if mode == 'artist':
        top_frequency = {i: artist_list.count(i) for i in artist_list}
    elif mode == 'genre':
        top_frequency = {i: genre_list.count(i) for i in genre_list}

    # Concatenating names of artists/genres with the same frequency
    for new_key,value in top_frequency.items():
        if value not in frequency_list.values():
            frequency_list[new_key] = value
        else:
            old_key = list(frequency_list.keys())[list(frequency_list.values()).index(value)] # Finds the key corresponding to the duplicate value
            frequency_list[str(old_key) + ', ' + str(new_key)] = frequency_list.pop(old_key) # Concatenates the old key with the new and assigns them the old key's value

    # Sorting the frequency dictionary in descending order
    frequency_list = {key: value for key, value in sorted(frequency_list.items(), key=lambda item: item[1], reverse=True)}

    # Printing the artists/genres with frequency
    print('\n')
    for i in frequency_list:
        print(str(frequency_list[i]) + ': ' + i)

# Getting user selection
user_selection = True
print('1) Calculate artist frequency\n2) Calculate genre frequency\n3) Exit')
while user_selection:
    print('\n')
    try:
        user_selection = int(input('Enter selection: '))
    except:
        print('Error: Enter a number')
        continue

    if user_selection == 1:
        get_frequency('artist')
    elif user_selection == 2:
        get_frequency('genre')
    elif user_selection == 3:
        user_selection = False
