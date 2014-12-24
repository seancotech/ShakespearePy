ShakespearePy
=============

A project developed on a Raspberry Pi Model B+. Searches an XML file of Shakespeare plays for a provided or random quote and displays the play, speaker, and full speech containing that quote.

Features cross-platform text-to-speech support via the pyttsx library as well as caching for speedup, tracked by file hash of the speech file.

## Syntax

````
python ShakespearePi [-q|--quiet] [-s|--speak] [-n|--no-cache] [quote]
````

`-q`, `--quiet`: Omit all output except the output speech data.
`-s`, `--speak`: Speak output using the pyttsx library after lookup.
`-n`, `--no-cache`: Don't cache to a file or look for one at all before lookup.
`quote`: Input quote to look up. If none is provided, a quote will be chosen at random from `Quotes.py`.
