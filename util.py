import datetime
import json

class Util():
    def build_url(self, base_url):
        urls = {}
        with open('filter.json') as file_json:    
            data = json.load(file_json)
            
        # daily
        recurrence = 'daily'
        urls[recurrence] = []
        for i, country in enumerate(data[0]['country_code']):
            for k, date in enumerate(data[0]['date']):
                tmp = date.split('/')
                date = datetime.date(int(tmp[-1]), int(tmp[-3]), int(tmp[-2]))
                urls[recurrence].append(base_url+'/'+country+'/'+recurrence+'/'+str(date)+'/')

        # weekly
        recurrence = 'weekly'
        urls[recurrence] = []
        for i, country in enumerate(data[1]['country_code']):
            for k, date in enumerate(data[1]['date']):
                tmp = date.split('/')
                date = datetime.date(int(tmp[-1]), int(tmp[-3]), int(tmp[-2]))
                date_i = date-datetime.timedelta(7)
                date_f = date+datetime.timedelta(1)
                urls[recurrence].append(base_url+'/'+country+'/'+recurrence+'/'+str(date_i)+'--'+str(date_f)+'/')

        return urls

    def json_write(self, f, d):
        with open(f, "w") as file:
            json.dump(d, file, indent=4)

        return 0


base_url = 'https://spotifycharts.com/regional'
util = Util()
util.json_write("start_urls.json", util.build_url(base_url))