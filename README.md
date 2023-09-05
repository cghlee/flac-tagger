# FLAC Tagger

A personal project to streamline the arduous process of tagging copious
amounts of classical music tracks (and especially opera) in a uniform fashion.

## Dependencies

FLAC Tagger requires the `Mutagen` module, with relevant documentation linked
below:

- [Mutagen](https://pypi.org/project/mutagen/)

## How to Use

On first run of `tagger.py`, either specify the path to a permanent source
folder that will contain untagged files to be tagged, or use the specified
defaults. Repeat this for the path of the destination folder which will
contain the auto-created folder housing successfully tagged files.

Move FLAC files to be tagged into the specified source path folder, and
rerun FLAC Tagger.

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

Tagged files will be automatically moved into a created folder in the
pre-specified destination folder directory.