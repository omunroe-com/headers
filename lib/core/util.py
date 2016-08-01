import csv
import json

class Util:

    def get_dictsites(self, filename='conf/topsites_global.csv'):
        dictsites = []
        with open(filename, 'rU') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                dictsites.append(row)
        return dictsites

    def load_config(self, filename='conf/params.json'):
        with open(filename) as settings_file:
            return json.load(settings_file)
