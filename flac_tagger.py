import os, json, mutagen, shutil
from mutagen.flac import Picture

# Pull or generate folder paths for FLAC Tagger operation
default_dir = os.path.join(os.path.expanduser('~'), 'Music')

# Pull folder paths from a pre-existing 'paths.json' file
if os.path.exists('paths.json'):
    with open('paths.json', 'r') as file:
        paths = json.load(file)
        path_src = paths['source']
        path_dest = paths['destination']
        file.close()
# Allow user specificiation of folder paths to be stored in 'paths.json' file
else:
    # Allow user-defined source folder to house FLAC files to be tagged
    print('No JSON file detected containing folder path information')
    paths = {}
    path_src = input('Define path to permanent folder that will contain files '
                     'to be tagged:\n(if no folder path is provided, a default '
                     '"%s" directory will be used)\n' % default_dir)
    if path_src:
        os.makedirs(path_src, exist_ok=True)
    else:
        path_src = os.path.join(default_dir, 'Non-Tagged Files')
        os.makedirs(path_src, exist_ok=True)
    paths['source'] = path_src
    print('Source folder created at:\n%s' % path_src)

    # Allow user-defined destination folder for auto-created album folders
    path_dest = input('Define path to permanent folder which will house the '
                      'auto-generated folder containing tagged files:\n'
                      '(if no folder path provided, the default "%s" '
                      'directory will be used)\n' % default_dir)
    if path_dest:
        os.makedirs(path_dest, exist_ok=True)
    else:
        path_dest = default_dir
    paths['destination'] = path_dest
    print('Destination path specified as:\n%s' % path_dest)

    # Save source and destination folder paths to 'paths.json' file
    with open('paths.json', 'w') as file:
        json_paths = json.dumps(paths)
        file.write(json_paths)
        file.close()
    print('Created JSON with folder path information\nPlease place untagged '
          'FLAC files into the "%s" folder and rerun FLAC Tagger' % path_src)
    quit()

# Initialise list variables to contain music file information
music_files = os.listdir(path_src)
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
    music_file = os.path.join(path_src, file_name)
    mutagen_files.append(mutagen.File(music_file))

# Ensure length of track titles list is equal to that of mutagen files list
if len(titles) != len(mutagen_files):
    print('ERROR: There are %s track titles in titles.txt, for %s music files'
          % (len(titles), len(mutagen_files)))
    quit()

# Generate user-defined variables containing album information
composer = input('Name of the composer:\n')
artist = input('Name of the artist(s):\n')

# Check for invalid characters in the given album name (which is used for the folder name)
toggle_album_confirmed = False
while not toggle_album_confirmed:
    album = input('Name of the album:\n')
    
    chars_invalid = ['<', '>', ':', '"', '\\', '/' '|', '?', '*']
    for char in chars_invalid:
        if char in album:
            print(f'\nInvalid character "{char}" in album name, please try again\n')
            break
    else:
        toggle_album_confirmed = True

year = input('Year of the recording:\n')
genre = input('Genre of the album:\n').title()
label = input('Name of recording label:\n')

# Order list of music files by ascending track number
mutagen_files.sort(key=lambda x: int(x['tracknumber'][0]))

# Locate album artwork within folder (optional)
art_input = input('Name of album artwork file, excluding file extension: '
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
    if artwork_file.endswith(('jpg', 'jpeg')): 
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

# Define name of folder to contain tagged files
folder_composer = composer.split()[-1]
folder_album = [part.strip() for part in album.split('/')]
folder_name = f'{folder_composer} - ' + ' - '.join(folder_album) + f' ({label})'

# Create new folder in default directory
new_dir = os.path.join(path_dest, folder_name)
os.mkdir(new_dir)
print('\nNew folder name:\n%s' % folder_name)

# Move tagged files to new folder
for file in music_files:
    old_path = os.path.join(path_src, file)
    shutil.move(old_path, new_dir)

print('\nTagging operation complete')
print('\n%s tagged files moved to:\n%s' % (len(music_files), new_dir))
