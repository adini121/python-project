data = ['get{url="http://134.96.235.47:8000/moodle_third"}', 'implicitlyWait{ms=30000}', 'findElement{using="partiallinktext",value="Login"}]\n', 'clickElement{id="0"}', 'findElement{using="id",value="username"}]\n', 'sendKeysToElement{id="1",value=["admin"]}', 'findElement{using="id",value="password"}]\n', 'sendKeysToElement{id="2",value=["MOODLE_admin_121"]}', 'findElement{using="id",value="loginbtn"}]\n', 'clickElement{id="3"}', 'findElement{using="cssselector",value="#id_email"}]\n', 'sendKeysToElement{id="4",value=["admin@admin.com"]}', 'findElement{using="cssselector",value="#id_city"}]\n', 'sendKeysToElement{id="5",value=["Perth"]}', 'findElement{using="id",value="id_country"}', 'getElementTagName{sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6,id=6}', 'getElementAttribute{sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6,name=multiple,id=6}', 'findChildElements{id="6",using="xpath",value=".//option[normalize-space(.)="Uganda"]"}', 'isElementSelected{sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6,id=7}]\n', 'clickElement{id="7"}', 'findElement{using="cssselector",value="input[value=\'Updateprofile\']"}]\n', 'clickElement{id="8"}', 'findElement{using="id",value="id_s__fullname"}]\n', 'sendKeysToElement{id="9",value=["moodleintmaster"]}', 'findElement{using="id",value="id_s__shortname"}]\n', 'sendKeysToElement{id="10",value=["intmaster"]}', 'findElement{using="cssselector",value="input[value=\'Savechanges\']"}]\n', 'clickElement{id="11"}]\n']


dictionary = {
    'findChildElement':'using',
    'findChildElement':'using',
    'findChildElement':'id',
    'findChildElements':'id',
    'findElement':'using',}

exception=['get'
    'clickElement'
	'sendKeysToElement'
    'implicitlyWait'
    'executeScript'
    'getElementText']

my_list = []
for item in data:
    items = item.split('{')
    action = items[0]
    if action in dictionary and action not in exception :
        splitter = dictionary[action] + '="'
        element = items[1].split(splitter)[1].split(',')[0]
        tuple = (action, element)
        my_list.append(tuple)
print my_list