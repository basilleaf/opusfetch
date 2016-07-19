import re
import json
import requests

data_file = 'imagesolutionsummary_meananom.txt'
base_url = 'http://tools.pds-rings.seti.org/opus/api'
metadata_url = base_url + '/metadata/'

result = {}
with open(data_file, "r") as f:
    next(f)  # skip first line
    for line in f:
        img_id = re.compile("\s+").split(line)[1]  # split line by spaces
        ring_obs_id = "S_IMG_CO_ISS_{}_N.json".format(img_id.split('.')[0])
        fullurl = metadata_url + ring_obs_id + '?cols=time1,timesec1'
        data = json.loads(requests.get(fullurl).text)
        print "%s,%s,%s" % (img_id, data[0]['time_sec1'], data[1]['time1'])
