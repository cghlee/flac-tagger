# FLAC Tagger

A personal project to streamline the arduous process of tagging copious
amounts of classical music tracks (and especially opera) in a uniform fashion.

## Dependencies

FLAC Tagger requires the `Mutagen` module, with relevant documentation linked
below:

- [Mutagen module](https://pypi.org/project/mutagen/)

## How to Use

Move FLAC files to be tagged into the `music` folder.

In the TXT file named `titles.txt`, list track titles in order of ascending
track number, with one track title per line.

*NOTE: Ensure that tracks to be tagged are in the correct order according to
existing track number metadata, or the tagging order will be incorrect.*

If you want to embed album artwork into your FLAC files, move the artwork
file (in JPG or PNG format) into the same directory as `README.md`,
`titles.txt`, and `tagger.py`, and specify the file name of the album artwork
file when prompted.

Once the above steps are complete, run `tagger.py` and input your desired
metadata tags. Currently supported tags are for the composer (also used for
the "album artist" tag), artist(s), album name, year of recording, and genre.

Tagged files will be automatically moved into a folder created in your
`<home_path>/Music` directory.