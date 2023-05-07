# '''
# The remote IP address
# The time of the request
# The request method (GET, POST, etc.)
# The requested URL
# The HTTP version
# The HTTP status code
# The size of the response sent to the client
# The referrer URL
# The user agent string
# '''


import re
import shlex
import pandas as pd

LOG_FILE = "access.log"


class parse:
    IP = 0
    TIME = 3
    TIME_ZONE = 4
    REQUESTED_URL = 5
    STATUS_CODE = 6
    USER_AGENT = 9

    def parse_line(self, line):
        try:
            line = re.sub(r"[\[\]]", "", line)
            data = shlex.split(line)
            result = {
                "ip": data[self.IP],
                "time": data[self.TIME],
                "status_code": data[self.STATUS_CODE],
                "requested_url": data[self.REQUESTED_URL],
                "user_agent": data[self.USER_AGENT],
            }
            return result
        except Exception as e:
            raise e


if __name__ == '__main__':
    parser = parse()
    with open(LOG_FILE, "r") as f:
        log_entries = [parser.parse_line(line) for line in f]
        print(type(log_entries))
    logs_df = pd.DataFrame(log_entries)


print(logs_df.head())
