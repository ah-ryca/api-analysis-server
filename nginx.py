from __future__ import print_function
import os
import sys

sys.path.append( os.path.join(os.path.dirname(__file__), 'app'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
import django
django.setup()
from core.models import RequestInfo

def main():
    import gzip
    import os
    import re
    from datetime import datetime
    import pytz

    tz = pytz.timezone('UTC')

    INPUT_DIR = "/var/log/nginx/"

    lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)

    for f in os.listdir(INPUT_DIR):
        if f.endswith(".gz"):
            logfile = gzip.open(os.path.join(INPUT_DIR, f))
        else:
            logfile = open(os.path.join(INPUT_DIR, f))

        for l in logfile.readlines():
            try:
                data = re.search(lineformat, l.decode('utf-8'))
            except AttributeError:
                data = re.search(lineformat, l)
            if data:
                datadict = data.groupdict()
                ip = datadict["ipaddress"]
                datetimeobj = datetime.strptime(datadict["dateandtime"], "%d/%b/%Y:%H:%M:%S %z") # Converting string to datetime obj
                url = datadict["url"]
                bytessent = datadict["bytessent"]
                referrer = datadict["refferer"]
                useragent = datadict["useragent"]
                status = datadict["statuscode"]
                method = data.group(6)

                RequestInfo.objects.create(
                                            remote_addr = ip,  
                                            request_time =  tz.normalize(datetimeobj),
                                            request_path =url,
                                            status = status,
                                            status_type = method,
                                            bytes_sent = bytessent,
                                            http_referer = referrer,
                                            http_user_agent = useragent  
                                             )
        logfile.close()


if __name__ == '__main__':
    main()



