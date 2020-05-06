# Soundcloud Like Parser

A simple Python script that scrapes the public Soundcloud api to calculate the artists and genres you've liked the most. 
It uses the public api methods, therefore you'll need a `client_id` and a `user_id`. Both can be retrieved with any browser's developer tools by capturing the API calls with the filter `track_likes?`. Written with Python 3.7 using only the requests library.

The number of retrieved likes will likely be less than the number reflected in your Soundcloud profile, because many tracks get deleted or made private. 

![dev tools](https://raw.githubusercontent.com/NoSecurityBlog/Soundcloud-Like-Parser/master/img/likes.png)
![dev tools](https://raw.githubusercontent.com/NoSecurityBlog/Soundcloud-Like-Parser/master/img/artists.png)
![dev tools](https://raw.githubusercontent.com/NoSecurityBlog/Soundcloud-Like-Parser/master/img/genres.png)

# Where to get client_id and user_id
![dev tools](https://raw.githubusercontent.com/NoSecurityBlog/Soundcloud-Like-Parser/master/img/devtools.png)

![closeup](https://raw.githubusercontent.com/NoSecurityBlog/Soundcloud-Like-Parser/master/img/closeup.png)
