# Learn Python 3 the Hard Way
Python exercises from the Learn Python 3 the Hard Way book

## Code Editor
You can use any code editor of your choice.

I use [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=adw-brand&gclid=Cj0KCQjw5fDWBRDaARIsAA5uWTjreEhL275HxoFeD4Gf7ADY7O0l6tTZtEwOGZUH7d2pv5nqemlRJx8aAkKiEALw_wcB)

## Tools Needed
[Python 3](https://www.python.org/downloads/)

[Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=adw-brand&gclid=Cj0KCQjw5fDWBRDaARIsAA5uWTjreEhL275HxoFeD4Gf7ADY7O0l6tTZtEwOGZUH7d2pv5nqemlRJx8aAkKiEALw_wcB)

**VS Code add-on:** Python for VSCode

## Running the Exercise
After cloning the repository, change your current directory to the file you want to run. Below is an example. The same process can be repeat for the other exercises.

`cd python-hardway`

`python ex10.py`

## Running the Exercises (or Website) in the Folders
I was using window 10.

* Install `virtualenv` via `pip` in the command line
  * `pip install virtualenv`

* Create a `.venvs` directory
  * `mkdir .venvs`
  * `virtualenv --system-site-packages .venvs/lpthw`

* Activate the virtual environment
  * `.\.venvs\lpthw\Scripts\activate`

* Install `nose`
  * `(lpthw) > pip install nose`
  
Then run the application as normal. Below is an example.

`cd python-hardway\id_card`

`python app.py`

In the browser, after the localhost add "/idcard"
