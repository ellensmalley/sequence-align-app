# sequence-align-app

## Description
This is a simple web application that takes input in the form of a DNA string and returns information on whether that sequence encodes a protein within a small set of genomes [1]. The queries are run asynchronously and the UI is updated upon their completion.
When first visiting the applicaiton, a user will need to pick a name to associate these queries to. 

[1] NC_000852, NC_007346, NC_008724, NC_009899, NC_014637, NC_020104, NC_023423, NC_023640, NC_023719, NC_027867

## Requirements
* python 3.7 (highest version supported when deploying to Elastic Beanstalk)
* node 12.18
* npm 6.14
* Django 3.1 and djangorestframework 3.12
* biopython 1.78
* awsebcli 3.19 for deployment
* In case of issue, exact packages for your python virtual environment can be found in `./requirements.txt`
* Add `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` at bottom of `.bash_profile` to allow for multiprocessing when running locally on a recent version of macOS. 

## Project Structure
`./alignSequence` is the base directory of the Django project.

`./sequenceRequests` app stores the backend Django API service of the application, i.e. the views, serializers, and Request model.
This directory also contains the `alignmentService` class in `./sequenceRequests/alignmentService.py` which contains the logic of searching for the chosen sequence.

`./frontend` app contains a simple REACT application, all components are within the `src/components/` directory.

## Running Locally
Create and activate a python virtual environment with requirements above then from the top level project directory run `python manage.py runserver`

If node_modules missing or out of date, you may need to run `npm install` from `./frontend` directory.

If changes are made to the UI, need to cd into `./frontend` and execute `npm run dev` to regenerate `main.js` static file.

### Details on Simple Sequence Alignment Algo
First validates that sequence consists of just characters ATGC, then randomizes genome list and for each genome searches for both the sequence and the reverse compliment of the sequence.  
This can lead to a few result cases:
1. If a sequence is found in the genome entirely within a portion encoding region, the algorithm will return that protein.
2. If a sequence is found in the genome but a portion of the sequence is non-coding, the algo will append this location and genome to a list of possible return values
3. If a sequence is not found to reside entirely within a protein encoding region, one of these possibiltiies will be returned.  
4. If a sequence is not found, empty strings will be returned for the location details.

### Ideas for Future Enhancements
Ideally these protein sequences should not be stored in static files but rather in document storage like an S3 bucket or in Elastic Search. If a file is missing from these locations, it could be fetched using NCBI's Entrez databases.  

Could use Celery for multiprocessing instead of multithreading from within the view and/or externalize the searching service to a separate application running multiple instances that can be called from the view.

