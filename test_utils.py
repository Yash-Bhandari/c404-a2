from utils import parse_url

def test_parse_url_with_ip_and_port():
	assert parse_url('http://0.0.1:8080') == ('0.0.1', 8080, '/')

def test_parse_url_with_domain():
	assert parse_url('https://github.com/whodidit/n0w') == ('github.com', 443, '/whodidit/n0w')


def test_parse_url_with_domain_and_port():
	assert parse_url('https://github.com:4000/whodidit/n0w') == ('github.com', 4000, '/whodidit/n0w')