# NY Times Scrapper
 This robot will open the NYTimes website and search for a phrase in a custom date-range and custom sections, then download it into a csv (and the images)

# How to run:
 - You need to have `conda` installed
 - Run `conda env create -f conda.yaml` to create the conda env
 - Run `conda activate my_env` to activate the env
 - Setup the .env file (follow the env.sample)
 - To run local, you can set in your .env the var ENV="dev", so the variables will be loaded from the .env
 - Without ENV="dev, the code will try to retrieve the vars from robocorp work_items (if it fails, .env will be tried)
