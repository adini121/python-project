# import re
# regex_str = 'findElement {using="css selector", value="#app-thunderbird"}]'
# findElement_xpath=re.findall('findElement\s\{using\=\"(.*?)\"', regex_str, re.DOTALL | re.MULTILINE)
# print findElement_xpath
safwan = """ actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, get {url="http://134.96.235.47:8000/moodle_third"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, implicitlyWait {ms=30000}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="partial link text", value="Login"}]
}
 id : 7386f7f4-23f8-419a-9ed6-dce6d6bc3f6a
 nextStateId : Some(c9961479-60a3-4be8-bd0b-7b5f60a1f390)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, clickElement {id="0"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="username"}]
}
 id : c9961479-60a3-4be8-bd0b-7b5f60a1f390
 nextStateId : Some(4de4837b-0316-4b28-b584-6cc6bd046313)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="1", value=["admin"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="password"}]
}
 id : 4de4837b-0316-4b28-b584-6cc6bd046313
 nextStateId : Some(dd0f876a-772e-45ce-a873-9d39233d3e37)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="2", value=["MOODLE_admin_121"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="loginbtn"}]
}
 id : dd0f876a-772e-45ce-a873-9d39233d3e37
 nextStateId : Some(d15ff7aa-f0bc-4d1d-bf4d-9ac67f3478fc)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, clickElement {id="3"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="css selector", value="#id_email"}]
}
 id : d15ff7aa-f0bc-4d1d-bf4d-9ac67f3478fc
 nextStateId : Some(e1c5926a-8406-4211-b39f-3d80bfee09d2)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="4", value=["admin@admin.com"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="css selector", value="#id_city"}]
}
 id : e1c5926a-8406-4211-b39f-3d80bfee09d2
 nextStateId : Some(81cb5266-ae69-436b-8a34-21c1b21a2414)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="5", value=["Perth"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="id_country"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, getElementTagName {sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6, id=6}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, getElementAttribute {sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6, name=multiple, id=6}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findChildElements {id="6", using="xpath", value=".//option[normalize-space(.) = \"Uganda\"]"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, isElementSelected {sessionId=95793cef-c0cf-42d2-a836-ce4cc83e91d6, id=7}]
}
 id : 81cb5266-ae69-436b-8a34-21c1b21a2414
 nextStateId : Some(b847f359-8d04-4990-b19d-554ae14f8fae)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, clickElement {id="7"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="css selector", value="input[value='Update profile']"}]
}
 id : b847f359-8d04-4990-b19d-554ae14f8fae
 nextStateId : Some(607a510d-184c-45f6-ad3a-3cc3d490d13b)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, clickElement {id="8"}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="id_s__fullname"}]
}
 id : 607a510d-184c-45f6-ad3a-3cc3d490d13b
 nextStateId : Some(f9135f62-d2ec-4db5-b5f5-64cd34eb16be)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="9", value=["moodleintmaster"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="id", value="id_s__shortname"}]
}
 id : f9135f62-d2ec-4db5-b5f5-64cd34eb16be
 nextStateId : Some(428c356b-e131-4576-8cc9-fe7eb71acec0)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, sendKeysToElement {id="10", value=["intmaster"]}],
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, findElement {using="css selector", value="input[value='Save changes']"}]
}
 id : 428c356b-e131-4576-8cc9-fe7eb71acec0
 nextStateId : Some(37f103a6-96ba-4eba-b7aa-958eadc800d9)}
,
 actions : {
[f9437e1c-8b15-40b9-91a6-1d8e5d6da249, clickElement {id="11"}]
}
 id : 37f103a6-96ba-4eba-b7aa-958eadc800d9
 nextStateId : None}
"""
my_list = []
actions = safwan.split(' {', 1)[1].split('\n,')
total_length = range(len(actions))
for number in total_length:
    data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
    dictionary = {}
    length = len(data)
    total_action = range(length)
    for i in total_action:
        action = data[i].split(',', 1)[1].replace(' ', '')
        my_list.append(action)

print my_list