# Fetches Metadata about a set of images from the OPUS api

## run it:

    python fetch.py > my_result_file.txt


## Install


### with conda 
    
	conda create -n opusfetch --file requirements.txt   
	source activate opusfetch
    
### with pip
  
    git clone https://github.com/basilleaf/opusfetch.git
    cd opusfetch
    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt
