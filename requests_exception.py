import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout = 0.5)
    print(response.status_code)
except ReadTimeout:
    print('Time out')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
