import re
# INPUTS

url='get {url="http://134.96.235.47:6052/some-other-page/somethingelse"}'
url2='get {url="http://134.96.235.47:8003/jenkins1.629/computer/new"}'

reg_mozilla_url_path=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+(.*?)\}', url, re.DOTALL | re.MULTILINE)
reg_jenkins_moodle_url_path=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+\\/[a-zA-Z0-9.]+(.*?)\}', url2, re.DOTALL | re.MULTILINE)

print reg_mozilla_url_path
print reg_jenkins_moodle_url_path

data1 = """
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=10000.0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, maximizeWindow {windowHandle="current"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, get {url="http://134.96.235.47:6001"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, executeScript {args=[], script="return jQuery.isReady == true"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".navbar"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, maximizeWindow {windowHandle="current"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, get {url="http://134.96.235.47:6001"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, executeScript {args=[], script="return jQuery.isReady == true"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".navbar"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=1}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".tab-link[href*=new]"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementLocation {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=2}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementSize {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=2}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, executeScript {args=[], script="window.scrollTo(0, 108)"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".tab-link[href*=new]"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, clickElement {id="2"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".app-name:nth-child(1)"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementText {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=3}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="id", value="search-q"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, sendKeysToElement {id="4", value=["P","a","c","k","a","g","e","d"," ","A","p","p"," ","d","s","a","f","g","s","d","f","g","s","h","d","f","g","j"," ","f","g","f","g","f","g"]}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, submitElement {id="4"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=0.0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="id", value="search-results"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=10000.0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElements {using="css selector", value="#search-results .item.result.app"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElements {using="css selector", value="#search-results .item.result.app"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findChildElement {using="css selector", id="6", value=".info > h3"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementText {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=31}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElements {using="css selector", value="#search-results .item.result.app"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findChildElement {using="css selector", id="6", value=".info > h3"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementText {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=31}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findChildElement {using="css selector", id="6", value=".info > h3"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, clickElement {id="31"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=0.0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElements {using="css selector", value=".loading"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=10000.0}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getTitle {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".product-details.listing.expanded.c img[class=\"icon\"]"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=32}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".info > h3"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, getElementText {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=33}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".author"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=34}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".button.product.install"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=35}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".support-email > a"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=36}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".description"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=37}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".slider"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=38}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value="#footer a[href*=\"privacy\"]"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=39}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, findElement {using="css selector", value=".abuse > a"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, isElementDisplayed {sessionId=a076598e-3ba0-4ac3-914a-08ce8b209e99, id=40}]"""

data2 = """
[e76fe865-c7d6-45f2-aba9-5132b94915ae, implicitlyWait {ms=50000.0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getWindowSize {windowHandle=current, sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, setWindowSize {width=1280, windowHandle="current", height=1024}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, get {url="http://134.96.235.47:6004"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, executeScript {args=[], script="return jQuery.isReady == true"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".navbar"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getWindowSize {windowHandle=current, sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, get {url="http://134.96.235.47:6004"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, executeScript {args=[], script="return jQuery.isReady == true"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".navbar"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=1}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".tab-link[href*=popular]"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, clickElement {id="2"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".info > h3"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getElementText {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=3}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="id", value="search-q"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, sendKeysToElement {id="4", value=["D","e","l","i","c","i","o","u","s"," ","P","i","e","r","o","g","i"]}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, submitElement {id="4"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElements {using="css selector", value="#search-results .item.result.app-list-app"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElements {using="css selector", value="#search-results .item.result.app-list-app"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findChildElement {using="css selector", id="5", value=".info > h3"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getElementText {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=23}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElements {using="css selector", value="#search-results .item.result.app-list-app"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findChildElement {using="css selector", id="5", value=".info > h3"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getElementText {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=23}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findChildElement {using="css selector", id="5", value=".info > h3"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, clickElement {id="23"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, implicitlyWait {ms=0.0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElements {using="css selector", value=".loading"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, implicitlyWait {ms=10000.0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".product.mkt-tile .heading .icon"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=24}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".info > h3"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getElementText {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=25}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".author"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=26}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".button.product.install"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=27}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".support-email > a"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=28}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".description"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=29}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".slider"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=30}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value="#footer a[href*=\"privacy\"]"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=31}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".button.abuse"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=99990.0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=32}]"""




def get_element_dict(data):

    dictionary = {
       'findElement': [],
       'findElements': [],
       'findChildElement': [],
       'findChildElements': [],
       'get': [],
       'implicitlyWait': []
    }

    items = data.split(']\n')
    for item in items:
        element = item.split(', ', 1)[1].split(' {', 1)
        element_name = element[0]
        element_content = element[1]
        if element_name in dictionary:
            my_list = dictionary[element_name]
            my_list.append(element_content)
    return dictionary


first_processed_data = get_element_dict(data1)
second_processed_data = get_element_dict(data2)

for key, list in first_processed_data.items():
    if len(list) >= len(second_processed_data[key]):
        for value in list:
            if not value in second_processed_data[key]:
                print key, value

        for value in second_processed_data[key]:
            if not value in list:
                print "2nd file", key, value
