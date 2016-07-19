## Fetches Metadata about a set of images from the OPUS api

### Install

    git clone https://github.com/basilleaf/opusfetch.git
    cd opusfetch
    virtualenv --python=/usr/local/bin/python2.7 venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt

### Run

    python fetch.py > my_result_file.txt
