## Music for programmers

This is a simple tool to download info and mp3 files from the awesome site [Music for programming](https://musicforprogramming.net/)
and play those using the default music player app. This opens iTunes on Mac and Groove Music on Windows 10, however, 
based on your file type association with mp3 files, the tool will open the corresponding app. On other platforms it will
 just download and ask users to play it themselves.

The files are downloaded in user's home directory - whatever `~` expands to. The actual path is
`~/music4programmers/`. 

### Install

* Clone the repo into your local filesystem. 
* Make sure you have `Python 3.n (n >= 5)` and `pip` installed.
* `cd` to the directory where you have cloned it and run `pip install -r requirements.txt`. 
* Run `pip install .` or `pip install -e .` (for development mode).
* A new command `m4p` should be available for you now if `pip install` was successful.
