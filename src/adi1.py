import re

url='get {url="http://134.96.235.47:6052/some-other-page/somethingelse"}'
url2='get {url="http://134.96.235.47:8003/jenkins1.629/computer/new"}'

reg_mozilla_url_path=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+(.*?)\}', url, re.DOTALL | re.MULTILINE)
reg_jenkins_moodle_url_path=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+\\/[a-zA-Z0-9.]+(.*?)\}', url2, re.DOTALL | re.MULTILINE)

print reg_mozilla_url_path
print reg_jenkins_moodle_url_path
