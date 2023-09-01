import os, mutagen, shutil
from mutagen.flac import Picture

# Initial variables
music_folder = os.path.abspath('.' + '/music')
music_files = os.listdir(music_folder)
music_files = [file for file in music_files if file.lower().endswith('.flac')]
mutagen_files = []

# Import TXT file containing track titles and store titles in a list
with open('titles.txt', 'r', encoding='utf-8') as file:
    titles = [line.strip() for line in file.readlines()]
    file.close()

# Terminate program if no track titles have been imported
if len(titles) == 0:
    print('No track titles have been entered into tracks.txt')
    quit()

# Initialise Mutagen music files and append to a list
for file_name in music_files:
    music_file = os.path.join(music_folder, file_name)
    mutagen_files.append(mutagen.File(music_file))

# Ensure length of track titles list is equal to that of mutagen files list
if len(titles) != len(mutagen_files):
    print('ERROR: There are %s track titles in titles.txt, for %s music files'
          % (len(titles), len(mutagen_files)))
    quit()

# Generate user-defined variables containing album information
composer = input('Name of the composer:\n')
artist = input('Name of the artist(s):\n')
album = input('Name of the album:\n')
year = input('Year of the recording:\n')
genre = input('Genre of the album:\n').title()
label = input('Name of recording label:\n')

# Order list of music files by ascending track number
mutagen_files.sort(key=lambda x: int(x['tracknumber'][0]))

# Locate album artwork within folder (optional)
art_input = input('Name of album artwork file, excluding file extension: '\
                  '(optional)\n').lower()
artwork_file = ''
if art_input:
    for file in os.listdir():
        if file.lower().startswith(art_input):
            artwork_file = file
            break

# Instantiate album artwork
artwork = Picture()
artwork.type = 3
if artwork_file:
    if artwork_file.endswith('jpg') or artwork_file.endswith('jpeg'):   
        artwork.mime = u'image/jpeg'
    elif artwork_file.endswith('png'):
        artwork.mime = u'image/png'
    with open(artwork_file, 'rb') as art:
        artwork.data = art.read()
        art.close()

# Delete and replace all metadata of music files
track_number = 1
for file in mutagen_files:
    file.clear()
    file.clear_pictures()
    file['title'] = titles.pop(0)
    file['composer'] = [composer]
    file['album artist'] = [composer]
    file['artist'] = [artist]
    file['album'] = [album]
    file['date'] = [year]
    file['genre'] = [genre]
    file['tracknumber'] = [f'{track_number:02d}']
    if art_input:
        file.add_picture(artwork)
    track_number += 1
    file.save()

# Specify default directory to move tagged files to
default_dir = os.path.join(os.path.expanduser('~'), 'Music')

# Define name of folder to contain tagged files
folder_composer = composer.split()[-1]
folder_album = [part.strip() for part in album.split('/')]
folder_name = f'{folder_composer} - ' + ' - '.join(folder_album) + f' ({label})'

# Create new folder in default directory
new_dir = os.path.join(default_dir, folder_name)
os.mkdir(new_dir)
print('New folder name:\n%s' % folder_name)

# Move tagged files to new folder
for file in music_files:
    old_path = os.path.join(music_folder, file)
    shutil.move(old_path, new_dir)

print('Tagging operation complete')
print('%s tagged files moved to:\n%s' % (len(music_files), new_dir))