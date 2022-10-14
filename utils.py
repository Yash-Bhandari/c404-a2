import re

def parse_url(url):
    is_https = True if url.startswith("https") else False
    regex = r'https?:\/\/([^:^\/]+):?([0-9]+)?(\/.*)?'
    match = re.match(regex, url)
    host, port, path = match.groups()
    if port is None:
        port = 443 if is_https else 80
    else:
        port = int(port)
    if path is None:
        path = '/'
    return host, port, path