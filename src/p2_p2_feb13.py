import re
from collections import Counter

data1 = """
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, implicitlyWait {ms=10000}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, maximizeWindow {windowHandle="current"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, get {url="http://134.96.235.47:6001/f"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, get {url="http://134.96.235.47:6000/f"}]
[a2da1608-5e22-4a2c-b3ce-72b8b7e10141, get {url="http://134.96.235.47:6001/ff"}]
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
[e76fe865-c7d6-45f2-aba9-5132b94915ae, implicitlyWait {ms=10000}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getWindowSize {windowHandle=current, sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, setWindowSize {width=1280, windowHandle="current", height=1024}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, get {url="http://134.96.235.47:6004"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, executeScript {args=[], script="return jQuery.isReady == true"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, findElement {using="css selector", value=".navbar"}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=0}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getTitle {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, getWindowSize {windowHandle=current, sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2}]
[e76fe865-c7d6-45f2-aba9-5132b94915ae, get {url="http://134.96.235.47:6004/"}]
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
[e76fe865-c7d6-45f2-aba9-5132b94915ae, isElementDisplayed {sessionId=03c4b22e-12ea-47e8-aacf-967a631b8ff2, id=32}]"""


def get_element_dict(data):

    dictionary = {
       'findElement': [],
       'findElements': [],
       'findChildElement': [],
       'findChildElements': []
    }
    get = []
    implicitly_wait = []

    exception = {
      'clickElement': [],
      'sendKeysToElement': [],
      'executeScript': [],
      'getPageSource': [],
      'setTimeout': [],
      'getElementText': [],
      'getTitle': []
    }

    items = data.split(']\n')
    for item in items:
        element = item.split(', ', 1)[1].split(' {', 1)
        element_name = element[0]
        element_content = element[1]
        if element_name in dictionary:
            using = element_content.split('using="', 1)[1].split('",', 1)[0]
            value = element_content.split('value="', 1)[1].replace('"}', '')
            tuple = (using, value)
            my_list = dictionary[element_name]
            my_list.append(tuple)
        if element_name == "get": #Get only the path of [get {url="someurl/path"}]
            get_url=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+(.*?)\}',
                               item.split(', ', 1)[1], re.DOTALL | re.MULTILINE)
            get.append(get_url)
        if element_name in exception:
            exception[element_name].append(1)
        if element_name == "implicitlyWait":
            time = element_content.split('ms=', 1)[1].replace("}", "")
            if float(time) != 0.0:
                implicitly_wait.append(float(time))
    # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    return dictionary, get, exception, implicitly_wait

processed_data1, get1, exception1, implicitly_wait1 = get_element_dict(data1)
processed_data2, get2, exception2, implicitly_wait2 = get_element_dict(data2)


def set_(data):
    """Remove duplicate element entries"""
    unique = []
    [unique.append(item) for item in data if item not in unique]
    return unique

def print_and_process(data1, data2):
    reorder_list = []
    changed_list = []
    deleted_list = []
    added_list = []
    for element in data1:
        list1 = list(set_(data1[element]))
        list2 = list(set_(data2[element]))
        list1_number = [x[0] for x in list1]
        list2_number = [x[0] for x in list2]
        arange = range(len(list1))
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

        for i in arange:
            try:
                if list1[i] != list2[i]:
                    if list1[i] in list2:
                        tuple = (element, list1[i][0])
                        reorder_list.append(tuple)
                        print list1[i], i, "ordering has been changed to", list2.index(list1[i]), "in second one"

                    else:
                        tuple = (element, list1[i][0])
                        changed_list.append(tuple)
                        print list1[i], "2nd", list2[i]
            except IndexError:
                if list1[i] in list2:
                    tuple = (element, list1[i][0])
                    reorder_list.append(tuple)
                    print list1[i], i, "ordering has been changed to", list2.index(list1[i]), "in second one"
                else:
                    print list1[i], "not present in second data"

        list1_count = Counter(list1_number)
        list2_count = Counter(list2_number)
        for obj in list1_count:
            one = list1_count[obj]
            two = list2_count[obj]
            if one != two:
                if one > two:
                    tuple = (element, (one-two, obj))
                    deleted_list.append(tuple)
                if two > one:
                    tuple = (element, (two-one, obj))
                    added_list.append(tuple)

    return reorder_list, changed_list, deleted_list, added_list

def get_deleted_or_added(data):
    """Can be deleted, not used anymore"""
    dictionary = {}
    for obj in data:
        if not obj[1] in dictionary:
            dictionary[obj[1]] = [obj[0]]
        else:
            dictionary[obj[1]].append(obj[0])
    return dictionary

def print_accordance(type, data):
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }
    if type in ["deleted", "added"]:
        for key in data:
            dictionary[key[0]].update({key[1][1]: key[1][0]})
        return dictionary
        #dict = {}
        #for key in data:
        #    if key[0] not in dict:
        #        dict[key[0]] = {key[1][1]: key[1][0]}
        #    else:
        #        dict[key[0]].update({key[1][1]: key[1][0]})
        #if dict != {}:
        #    print type, dict
    if type in ["reorder", "changed"]:
        for key, value in data.items():
            dictionary[key[0]].update({key[1]: value})
        return dictionary


def compare_get(get_data1, get_data2):
    """Compare URL paths of two get{url} occurances"""
    changed = []
    for url in set_(get_data1):
        if not url in get_data2:
            changed.append(1)
    print "changed get", len(changed)

def compare_exception(exception1, exception2):

    for key in exception1:
        one = len(exception1[key])
        two = len(exception2[key])
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        print "Changed", key, one-two
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # To print added and deleted separately
        # if one != two:
        #     if one > two:
        #         print "deleted", key, one-two
        #     if two > one:
        #         print "added", key, two-one

def compare_implicitly_wait(implicitly_wait1, implicitly_wait2):
    one = len(implicitly_wait1)
    two = len(implicitly_wait2)
    print "Changed # implicitlyWait", one-two
    # To print added and deleted separately
    # if one > two:
    #     print "implicitlyWait", "deleted", one-two
    # else:
    #     print "implicitlyWait", "deleted", 0
    # if two > one:
    #     print "implicitlyWait", "created", two-one
    # else:
    #     print "implicitlyWait", "created", 0

reorder_list, changed_list, deleted_list, added_list = print_and_process(data1=processed_data1, data2=processed_data2)
total_reorder = Counter(reorder_list)
total_changed = Counter(changed_list)

#total_added = [x[1] for x in added_list]
#total_deleted = [x[1] for x in deleted_list]
# deleted_count = get_deleted_or_added(total_deleted)
# added_count = get_deleted_or_added(total_added)
reorder = print_accordance("reorder", total_reorder)
changed = print_accordance("changed", total_changed)
deleted = print_accordance("deleted", deleted_list)
added   = print_accordance("added", added_list)
compare_get(get1, get2)
compare_exception(exception1, exception2)
compare_implicitly_wait(implicitly_wait1, implicitly_wait2)

#for key, value in reorder.items():
 #   print "reorder", key, value
""" PRINT FINAL OUTPUTS """
print "\n"
print "======================================== REORDERED ================================================================="
for key in reorder:
    for value in reorder[key]:
        if changed[key][value]!="0": #checks if not equal to zero
            print "reordered" ,key ,"using" ,value, ":" ,reorder[key][value]

print "======================================= CHANGED =============================================================="

for key in changed:
    for value in changed[key]:
        if changed[key][value]!="0":
            print "changed" ,key ,"using" ,value, ":" ,changed[key][value]

print "======================================= ADDED =============================================================="
for key in added:
    for value in added[key]:
        if added[key][value]!="0":
            print "added" ,key ,"using" ,value, ":" ,added[key][value]

print "======================================= DELETED =============================================================="
for key in deleted:
    for value in deleted[key]:
        if deleted[key][value]!="0":
            print "deleted" ,key ,"using" ,value, ":" ,deleted[key][value]

# print "======================================= lenghts =============================================================="
"""
IGNORE-THIS-USE-LATER-IF-NEEDED
def process_data(data):
    dictionary = {}
    for obj, value in data.items():
        if obj[0] not in dictionary:
            dictionary[obj[0]] = {obj[1]: value}
        else:
            dictionary[obj[0]].update({obj[0]: value})
    return dictionary
"""