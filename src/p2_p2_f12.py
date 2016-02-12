from collections import Counter

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




data1 = {'findElements': [('css selector', '#search-results .item.result.app'), ('css selector', '#search-results .item.result.app'), ('css selector', '#search-results .item.result.app'), ('css selector', '.loading')], 'findChildElements': [], 'findElement': [('css selector', '.navbar'), ('css selector', '.navbar'), ('css selector', '.tab-link[href*=new]'), ('css selector', '.tab-link[href*=new]'), ('css selector', '.app-name:nth-child(1)'), ('id', 'search-q'), ('id', 'search-results'), ('css selector', '.product-details.listing.expanded.c img[class="icon"]'), ('css selector', '.info > h3'), ('css selector', '.author'), ('css selector', '.button.product.install'), ('css selector', '.support-email > a'), ('css selector', '.description'), ('css selector', '.slider'), ('css selector', '#footer a[href*="privacy"]'), ('css selector', '.abuse > a')], 'findChildElement': [('css selector', '.info > h3'), ('css selector', '.info > h3'), ('css selector', '.info > h5')]}

data2 = {'findElements': [('css selector', '#search-results .item.result.app-list-app'), ('css selector', '#search-results .item.result.app-list-app'), ('css selector', '#search-results .item.result.app-list-app'), ('css selector', '.loading')], 'findChildElements': [], 'findElement': [('css selector', '.navbar'), ('css selector', '.navbar'), ('css selector', '.tab-link[href*=popular]'), ('css selector', '.info > h3'), ('id', 'search-q'), ('css selector', '.product.mkt-tile .heading .icon'), ('css selector', '.info > h3'), ('css selector', '.author'), ('css selector', '.button.product.install'), ('css selector', '.support-email > a'), ('css selector', '.description'), ('css selector', '.slider'), ('css selector', '#footer a[href*="privacy"]'), ('css selector', '.button.abuse')], 'findChildElement': [('css selector', '.info > h3'), ('css selector', '.info > h3'), ('css selector', '.info > h10')]}


def set_(data):
    unique = []
    [unique.append(item) for item in data if item not in unique]
    return unique

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

def get_deleted_or_added(data):
    dictionary = {}
    for obj in data:
        if not obj[1] in dictionary:
            dictionary[obj[1]] = [obj[0]]
        else:
            dictionary[obj[1]].append(obj[0])
    return dictionary

dictionary = {
 'findChildElement': ["css selector", "xpath", "tag name"],
 'findChildElements': ["css selector", "xpath", "tag name"],
 'findElement': ["css selector", "xpath", "tag name", "name", "class name", "id", "link text", "partial link text"],
 'findElements': ["css selector", "xpath", "tag name"]
 }

def print_accordance(type, data):
    if type in ["deleted", "added"]:
        for key, value in dict(data).items():
            print key, type, "element", value[0], value[1]
    if type in ["reorder", "changed"]:
        dict = {}


total_reorder = Counter(reorder_list)
total_changed = Counter(changed_list)
print total_changed
# total_added = [x[1] for x in added_list]
# total_deleted = [x[1] for x in deleted_list]
# deleted_count = get_deleted_or_added(total_deleted)
# added_count = get_deleted_or_added(total_added)
print_accordance("reorder", total_reorder)
print_accordance("changed", total_changed)
print_accordance("deleted", deleted_list)
print_accordance("added", added_list)