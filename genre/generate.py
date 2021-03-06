# Find all movies of a given genre and generate the page for it 
import os
genres = ['Action','Adventure','Animation', 'Biography', 'Comedy', 'Crime', 
    'Documentary', 'Drama', 'Family', 'Fantasy', 'Noir', 
    'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 
    'Sci-Fi', 'Sports', 'Superhero', 'Thriller', 'War', 'Western']

movies = '''
    <dt><b>Free Guy</b></dt>
    <dd><em>Action | Adventure | Comedy</em></dd>
    <dt><b>The Addams Family 2</b></dt>
    <dd><em>Animation | Adventure | Comedy</em></dd>
    <dt><b>Venom: Let There Be Carnage</b></dt>
    <dd><em>Action | Adventure | Sci-Fi</em></dd>
    <dt><b>Dune</b></dt>
    <dd><em>Action | Adventure | Drama</em></dd>
    <dt><b>Resident Evil: Welcome to Raccoon City</b></dt>
    <dd><em>Action | Horror | Mystery</em></dd>
    <dt><b>Halloween Kills</b></dt>
    <dd><em>Crime | Horror | Thriller</em></dd>
    <dt><b>The French Dispatch</b></dt>
    <dd><em>Comedy | Drama | Romance</em></dd>
    <dt><b>Titanic</b></dt>
    <dd><em>Drama | Romance</em></dd>
    <dt><b>No Time to Die</b></dt>
    <dd><em>Action | Adventure | Thriller</em></dd>
    <dt><b>Black Widow</b></dt>
    <dd><em>Action | Adventure | Sci-Fi</em></dd>
    <dt><b>The Guilty</b></dt>
    <dd><em>Crime | Drama | Thriller</em></dd>
    <dt><b>Spectre</b></dt>
    <dd><em>Action | Adventure | Thriller</em></dd>
    <dt><b>The Many Saints of Newark</b></dt>
    <dd><em>Crime | Drama</em></dd>
    <dt><b>The Last Duel</b></dt>
    <dd><em>Action | Drama | History</em></dd>
    <dt><b>Malignant</b></dt>
    <dd><em>Crime | Horror | Mystery</em></dd>
    <dt><b>Wolf</b></dt>
    <dd><em>Drama | Mystery | Thriller</em></dd>
    <dt><b>Cruella</b></dt>
    <dd><em>Adventure | Comedy | Crime</em></dd>
    <dt><b>The Card Counter</b></dt>
    <dd><em>Action | Crime | Drama</em></dd>
    <dt><b>The Addams Family</b></dt>
    <dd><em>Animation | Adventure | Comedy</em></dd>
    <dt><b>My Little Pony: A New Generation</b></dt>
    <dd><em>Animation | Adventure | Comedy</em></dd>
    <dt><b>Shang-Chi and the Legend of the Ten Rings</b></dt>
    <dd><em>Action | Adventure | Fantasy</em></dd>
    <dt><b>Casino Royale</b></dt>
    <dd><em>Action | Adventure | Thriller</em></dd>
    <dt><b>Hocus Pocus</b></dt>
    <dd><em>Comedy | Family | Fantasy</em></dd>
    <dt><b>Eternals</b></dt>
    <dd><em>Action | Adventure | Drama</em></dd>
    <dt><b>Cinderella</b></dt>
    <dd><em>Adventure | Comedy | Family</em></dd>
    <dt><b>The DUFF</b></dt>
    <dd><em>Comedy | Romance</em></dd>
    <dt><b>Suicide Squad</b></dt>
    <dd><em>Action | Adventure | Comedy</em></dd>
    <dt><b>Cruise</b></dt>
    <dd><em>Action | Adventure | Comedy</em></dd>
    <dt><b>Venom</b></dt>
    <dd><em>Action | Adventure | Sci-Fi</em></dd>
    <dt><b>Spider-Man: No Way Home</b></dt>
    <dd><em>Action | Adventure | Sci-Fi</em></dd>'''
end = '''</dl>
</body>
</html>'''
m = movies.split('\n')

for genre in genres:
    s = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8"/>
    <title> {genre} Movies - MReview</title>
</head>
<body>
<h1>{genre} Movies</h1>
<nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="movies.html">All Movies</a></li>
        <li><a href="genres.html">Genres</a></li>
        <li><a href="forum.html">Forum</a></li>
        <li>Search</li>
    </ul>
</nav>
<dl>
'''
    out = []
    for i in  range(len(m)):
        # print(i)
        if i+1 >= len(m):
            if genre in m[i]:
                out.append(m[i])
            break
        elif genre in m[i] or genre in m[i+1]:
                out.append(m[i])
    for i in out:
        s += i + '\n'
    s += end
    os.system(f"echo '{s}' > ./genre/{genre.lower().replace('-', '').replace(' ', '')}.html")