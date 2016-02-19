import csv

from collections import Counter
file_contents="""Session 57e4c7b9-c9bb-4656-9323-7d91bb6cd394 {
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, get {url="http://134.96.235.47:8000/moodle_first"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, implicitlyWait {ms=30000}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="partial link text", value="Login"}]
}
 id : 5df3beac-3e40-4e8f-9e92-653d2fa38cef
 nextStateId : Some(bd4c9046-0d0f-4d46-81c1-5163ff82b2fa)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, clickElement {id="0"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="username"}]
}
 id : bd4c9046-0d0f-4d46-81c1-5163ff82b2fa
 nextStateId : Some(beee662f-77bf-4c5d-ae4e-66fba37f7fa2)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="1", value=["admin"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="password"}]
}
 id : beee662f-77bf-4c5d-ae4e-66fba37f7fa2
 nextStateId : Some(e6eea326-cf9a-4166-9f08-8f9dc34aa175)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="2", value=["MOODLE_admin_121"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="loginbtn"}]
}
 id : e6eea326-cf9a-4166-9f08-8f9dc34aa175
 nextStateId : Some(c0f276fa-8605-47f8-99d4-6b13e66ec907)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, clickElement {id="3"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="css selector", value="#id_email"}]
}
 id : c0f276fa-8605-47f8-99d4-6b13e66ec907
 nextStateId : Some(a866950b-00af-4120-9df8-22092da9d2e2)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="4", value=["admin@admin.com"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="css selector", value="#id_city"}]
}
 id : a866950b-00af-4120-9df8-22092da9d2e2
 nextStateId : Some(1cc08842-b524-45d9-9d72-a3177dc5aa72)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="5", value=["Perth"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="id_country"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, getElementTagName {sessionId=9ddbe802-e28c-4dd2-80f0-7bf6718e540b, id=6}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, getElementAttribute {sessionId=9ddbe802-e28c-4dd2-80f0-7bf6718e540b, name=multiple, id=6}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findChildElements {id="6", using="xpath", value=".//option[normalize-space(.) = \"Uganda\"]"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, isElementSelected {sessionId=9ddbe802-e28c-4dd2-80f0-7bf6718e540b, id=7}]
}
 id : 1cc08842-b524-45d9-9d72-a3177dc5aa72
 nextStateId : Some(003df9f3-4386-4911-a6ad-80cf2ef0cd84)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, clickElement {id="7"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="css selector", value="input[value='Update profile']"}]
}
 id : 003df9f3-4386-4911-a6ad-80cf2ef0cd84
 nextStateId : Some(8c0594f7-0056-4c79-a232-c2e78d707ada)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, clickElement {id="8"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="id_s__fullname"}]
}
 id : 8c0594f7-0056-4c79-a232-c2e78d707ada
 nextStateId : Some(3074ac22-8bea-4ea8-b167-9393eb66371b)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="9", value=["moodleintmaster"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="id_s__shortname"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="id", value="id_s__shortname"}]
}
 id : 3074ac22-8bea-4ea8-b167-9393eb66371b
 nextStateId : Some(f600b3b6-cf8b-441e-b36d-b0985cc48ecb)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, sendKeysToElement {id="10", value=["intmaster"]}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElements {using="css selector", value="input[wdwd"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElements {using="css selector", value="infwput[wdwd"}],
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, findElement {using="css selector", value="input[value='Save changes']"}]
}
 id : f600b3b6-cf8b-441e-b36d-b0985cc48ecb
 nextStateId : Some(55aa2799-e71a-477e-9605-3de6f4e62c2f)}
,
 actions : {
[57e4c7b9-c9bb-4656-9323-7d91bb6cd394, clickElement {id="11"}]
}
 id : 55aa2799-e71a-477e-9605-3de6f4e62c2f
 nextStateId : None}"""

file_contents2=file_contents
def return_raw_actions(file_contents):
    actions_list = []
    actions = file_contents.split(' {', 1)[1].split('\n,')
    total_length = range(len(actions))
    for number in total_length:
        data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
        dictionary = {}
        length = len(data)
        total_action = range(length)
        for i in total_action:
            action = data[i].split(',', 1)[1]
            actions_list.append(action)
    return actions_list


def count_by_action_type(file_contents):
    data = return_raw_actions(file_contents)
    # print data

    findElementsDictionary = {
    'findChildElement':'using',
    'findChildElements':'using',
    'findElement':'using',
    'findElements':'using'}

    other_actions=['clickElement',
    'sendKeysToElement',
    'implicitlyWait',
    'get']

    findElement_list= []
    other_actions_list = []
    for item in data:
        items = item.split('{')
        action = items[0].replace(' ', '')
        if action in findElementsDictionary and action not in other_actions :
            splitter = findElementsDictionary[action] + '="'
            element = items[1].split(splitter)[1].split('",')[0]
            tuple = (action, element)
            findElement_list.append(tuple)
        elif action in other_actions:
            other_actions_list.append(action)

    return dict(Counter(findElement_list)), dict(Counter(other_actions_list))


def get_dictionary(file_contents):
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }

    exception = {'get' : '0',
      'implicitlyWait' : '0',
      'clickElement': '0',
      'sendKeysToElement': '0'}

    findElement_count_dict,otherActions_count_dict=count_by_action_type(file_contents)
    for key, value in findElement_count_dict.items():
        dictionary[key[0]].update({key[1]: value})
    for key, value in otherActions_count_dict.items():
        exception[key] = value
    dictionary = merge_dictionary(dictionary)
    return dictionary, exception

"""I will be back in 5 mins and knock you here. >> Ok
"""
def merge_dictionary(contents):
    dictionary = {
    'Element': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
    'ChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
    }

    for item, elements in dictionary.items():
        if item == "Element":
            for element in elements:
                try:
                    one = contents["findElement"][element]
                    two = contents["findElements"][element]
                    dictionary["Element"][element] = int(one) + int(two)
                except KeyError:
                    dictionary["Element"][element] = contents["findElement"][element]
        if item == "ChildElement":
            for element in elements:
                try:
                    one = contents["findChildElement"][element]
                    two = contents["findChildElements"][element]
                    dictionary["ChildElement"][element] = int(one) + int(two)
                except KeyError:
                    dictionary["ChildElement"][element] = contents["findChildElement"][element]

    return dictionary


def process_data_for_csv(elementdict, exception):
    fields = ['Childcssselector', 'Childxpath', 'Childtagname', 'xpath', 'partiallinktext',
              'classname', 'linktext', 'name', 'cssselector', 'tagname', 'id',
              'sendKeysToElement', 'implicitlyWait', 'get','clickElement']
    dictionary = {}
    for key, value in elementdict.items():
        # proces the data according to column name
        for element in value:
            if key != "ChildElement":
                title = element.replace(' ', '')
                dictionary[title] = value[element]
            if key == "ChildElement":
                title = element.replace(' ', '')
                dictionary["Child" + title] = value[element]

    # For exception one
    dictionary.update(exception)

    return fields, dictionary

def write_in_csv(file_contents):
    dictionary, exception = get_dictionary(file_contents)
    fields, dictionary = process_data_for_csv(dictionary, exception)
    try:
        with open('csv_output_new.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerow(dictionary)
        print "success"
    except IOError:
        print "ERROR"


write_in_csv(file_contents)