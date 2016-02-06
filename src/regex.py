# import re
# regex_str = 'findElement {using="css selector", value="#app-thunderbird"}]'
# findElement_xpath=re.findall('findElement\s\{using\=\"(.*?)\"', regex_str, re.DOTALL | re.MULTILINE)
# print findElement_xpath
safwan = """
Session c03ad187-87d7-4163-8cb7-4592b526d2a6 {
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, setWindowSize {windowHandle="current", width=1024, height=768}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, setTimeout {type="page load", ms=30000}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, implicitlyWait {ms=1000}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : dc099486-43aa-459c-aa2d-53f98e78c5ca
 nextStateId : Some(57ebaa06-a279-416b-b8ca-cd5e6bdf3f48)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/configureSecurity/"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/useSecurity']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=0}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementSelected {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=0}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 57ebaa06-a279-416b-b8ca-cd5e6bdf3f48
 nextStateId : Some(7dc96609-c0ac-4469-92fe-47d3b3cfad8d)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"0"}]}]
}
 id : 7dc96609-c0ac-4469-92fe-47d3b3cfad8d
 nextStateId : Some(d95cc1b0-65d6-4afd-90b9-071ac13fdbd2)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="0"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="xpath", value="  .//input[@type='radio'][./@id = 'Delegate to servlet container' or ./@name = 'Delegate to servlet container' or ./@value = 'Delegate to servlet container' or ./@placeholder = 'Delegate to servlet container' or ./@id = //label[contains(normalize-space(.), 'Delegate to servlet container')]/@for]| .//label[contains(normalize-space(.), 'Delegate to servlet container')]//input[@type='radio']| .//label[contains(normalize-space(.), 'Delegate to servlet container')][@class='attach-previous']/preceding-sibling::input[@type='radio']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : d95cc1b0-65d6-4afd-90b9-071ac13fdbd2
 nextStateId : Some(2ba678b3-d3ea-4c11-97b7-715358944027)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"1"}]}]
}
 id : 2ba678b3-d3ea-4c11-97b7-715358944027
 nextStateId : Some(d771af9b-3f64-4d4e-9f6f-ef16ef814c37)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="1"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementAttribute {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, name=path, id=1}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'Save' or ./@name = 'Save' or contains(./@value, 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')] | .//button[(((./@id = 'Save' or contains(./@value, 'Save')) or contains(normalize-space(.), 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=2}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : d771af9b-3f64-4d4e-9f6f-ef16ef814c37
 nextStateId : Some(e7c1b5ad-e621-463c-85a6-155780b2f8e5)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"2"}]}]
}
 id : e7c1b5ad-e621-463c-85a6-155780b2f8e5
 nextStateId : Some(12139b48-be62-4531-8d16-d4b45805155c)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="2"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="/html"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementText {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=3}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 12139b48-be62-4531-8d16-d4b45805155c
 nextStateId : Some(c4ad1729-9008-4980-802b-027a43ef5351)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/newJob"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="name", value="name"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=4}]
}
 id : c4ad1729-9008-4980-802b-027a43ef5351
 nextStateId : Some(e0281d77-d550-4004-9680-72be6f1d438a)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"4"}]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clearElement {id="4"}]
}
 id : e0281d77-d550-4004-9680-72be6f1d438a
 nextStateId : Some(cbee6f83-181a-4cce-ad74-a89cc1c5beee)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"4"}]}]
}
 id : cbee6f83-181a-4cce-ad74-a89cc1c5beee
 nextStateId : Some(615a5065-fc94-4157-a7bc-17d62c11073c)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, sendKeysToElement {id="4", value=["oral_aquarium"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="  .//input[@type='radio'][./@id = 'hudson.model.FreeStyleProject' or ./@name = 'hudson.model.FreeStyleProject' or ./@value = 'hudson.model.FreeStyleProject' or ./@placeholder = 'hudson.model.FreeStyleProject' or ./@id = //label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')]/@for]| .//label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')]//input[@type='radio']| .//label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')][@class='attach-previous']/preceding-sibling::input[@type='radio']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=5}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 615a5065-fc94-4157-a7bc-17d62c11073c
 nextStateId : Some(4d0b6d2e-588d-4146-8b7c-31cde667314a)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"5"}]}]
}
 id : 4d0b6d2e-588d-4146-8b7c-31cde667314a
 nextStateId : Some(8764f947-7388-41a3-ad45-a7b307d3dd43)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="5"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'OK' or ./@name = 'OK' or contains(./@value, 'OK')) or contains(./@title, 'OK'))] | .//input[./@type = 'image'][contains(./@alt, 'OK')] | .//button[(((./@id = 'OK' or contains(./@value, 'OK')) or contains(normalize-space(.), 'OK')) or contains(./@title, 'OK'))] | .//input[./@type = 'image'][contains(./@alt, 'OK')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=6}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 8764f947-7388-41a3-ad45-a7b307d3dd43
 nextStateId : Some(ec4c954b-3305-47b7-87f3-adfbe8e59384)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"6"}]}]
}
 id : ec4c954b-3305-47b7-87f3-adfbe8e59384
 nextStateId : Some(dd70dd80-d467-4ef6-a90a-3651867d8656)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="6"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//input[@name='parameterized']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=7}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementSelected {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=7}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : dd70dd80-d467-4ef6-a90a-3651867d8656
 nextStateId : Some(7b96b55b-0e3c-49f4-bd4a-c95b9d3bf330)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"7"}]}]
}
 id : 7b96b55b-0e3c-49f4-bd4a-c95b9d3bf330
 nextStateId : Some(0ac5e055-9e8f-41bd-a047-a7db914ea8a4)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="7"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//button[text()='Add Parameter']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=8}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 0ac5e055-9e8f-41bd-a047-a7db914ea8a4
 nextStateId : Some(d8670f90-f7eb-4c11-a48a-339e821da0b0)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"8"}]}]
}
 id : d8670f90-f7eb-4c11-a48a-339e821da0b0
 nextStateId : Some(09882df3-33eb-4600-ba83-56538165a629)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="8"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//button[text()='Add Parameter']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=8}]
}
 id : 09882df3-33eb-4600-ba83-56538165a629
 nextStateId : Some(c6ab4cb1-3f1b-4067-8201-d0735c7f2959)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="YAHOO.util.Dom.batch(    document.querySelector('.yui-menu-body-scrolled'),    function (el) {        el.style.height = 'auto';        YAHOO.util.Dom.removeClass(el, 'yui-menu-body-scrolled');    });", args=[]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="8", using="xpath", value="ancestor::*[contains(@class,'yui-menu-button')]/.."}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="9", using="xpath", value=".//A[@href][@id='String Parameter' or normalize-space(.)='String Parameter' or @title='String Parameter' or .//img[@alt='String Parameter']]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : c6ab4cb1-3f1b-4067-8201-d0735c7f2959
 nextStateId : Some(6cdf9dd9-3aaf-45e4-acac-745bc48cd2f1)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"10"}]}]
}
 id : 6cdf9dd9-3aaf-45e4-acac-745bc48cd2f1
 nextStateId : Some(520240e0-4448-49bd-b9a2-7f767c3f7981)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="10"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//div[@name='parameter']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=11}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="xpath", value="//div[@name='parameter']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementAttribute {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, name=path, id=11}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/properties/hudson-model-ParametersDefinitionProperty/parameterized/parameter/name']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=12}]
}
 id : 520240e0-4448-49bd-b9a2-7f767c3f7981
 nextStateId : Some(69466afb-f5d8-4463-9747-1ed2b1eb5b90)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"12"}]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clearElement {id="12"}]
}
 id : 69466afb-f5d8-4463-9747-1ed2b1eb5b90
 nextStateId : Some(603146bb-2beb-475a-8fa0-4d3aafb19f98)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"12"}]}]
}
 id : 603146bb-2beb-475a-8fa0-4d3aafb19f98
 nextStateId : Some(6741233c-2f57-40b8-98ad-31e3476b7489)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, sendKeysToElement {id="12", value=["ID"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/pseudoRemoteTrigger']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=13}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 6741233c-2f57-40b8-98ad-31e3476b7489
 nextStateId : Some(927f7e72-d745-471a-8dab-5ed26bd65d90)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"13"}]}]
}
 id : 927f7e72-d745-471a-8dab-5ed26bd65d90
 nextStateId : Some(b3902ee3-5a87-4354-a166-e3c16b6346a9)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="13"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="name", value="authToken"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=14}]
}
 id : b3902ee3-5a87-4354-a166-e3c16b6346a9
 nextStateId : Some(5172bbcb-fa2e-4b14-8eb0-913f792fbb77)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"14"}]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clearElement {id="14"}]
}
 id : 5172bbcb-fa2e-4b14-8eb0-913f792fbb77
 nextStateId : Some(3091f325-f471-4e2d-9246-cc907e739961)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"14"}]}]
}
 id : 3091f325-f471-4e2d-9246-cc907e739961
 nextStateId : Some(6f964f67-9011-447c-9136-214e07fcc9bd)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, sendKeysToElement {id="14", value=["TOKEN"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/hetero-list-add[builder]']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=15}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 6f964f67-9011-447c-9136-214e07fcc9bd
 nextStateId : Some(7a153590-0a78-4985-b875-d6f9b92a309e)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"15"}]}]
}
 id : 7a153590-0a78-4985-b875-d6f9b92a309e
 nextStateId : Some(be558b31-a14c-4b2a-a853-74388157928e)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="15"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/hetero-list-add[builder]']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=15}]
}
 id : be558b31-a14c-4b2a-a853-74388157928e
 nextStateId : Some(5eb72f68-0d5c-477f-a814-264057cd042c)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="YAHOO.util.Dom.batch(    document.querySelector('.yui-menu-body-scrolled'),    function (el) {        el.style.height = 'auto';        YAHOO.util.Dom.removeClass(el, 'yui-menu-body-scrolled');    });", args=[]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="15", using="xpath", value="ancestor::*[contains(@class,'yui-menu-button')]/.."}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="16", using="xpath", value=".//A[@href][@id='Execute shell' or normalize-space(.)='Execute shell' or @title='Execute shell' or .//img[@alt='Execute shell']]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 5eb72f68-0d5c-477f-a814-264057cd042c
 nextStateId : Some(771cd478-fc14-4b31-b7a2-1f35d7bb1daa)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"17"}]}]
}
 id : 771cd478-fc14-4b31-b7a2-1f35d7bb1daa
 nextStateId : Some(712d731e-fac1-40a6-91ea-e134b57bb31d)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="17"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//div[@name='builder']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=18}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="xpath", value="//div[@name='builder']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementAttribute {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, name=path, id=18}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=19}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=19}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=19}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=19}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//*[@path='/builder/command']"}]
}
 id : 712d731e-fac1-40a6-91ea-e134b57bb31d
 nextStateId : Some(6992bda3-79bf-448b-8f58-d86019beac53)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="cmElem = document.evaluate(        arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;codemirror = cmElem.CodeMirror;if (codemirror == null) {    console.log('CodeMirror object not found!');}codemirror.setValue(arguments[1]);codemirror.save();", args=["//*[@path='/builder/command']/following-sibling::div","test 'id_to_pass' = $ID"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'Save' or ./@name = 'Save' or contains(./@value, 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')] | .//button[(((./@id = 'Save' or contains(./@value, 'Save')) or contains(normalize-space(.), 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=20}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 6992bda3-79bf-448b-8f58-d86019beac53
 nextStateId : Some(6ac222df-7ac2-4e0b-bfd9-fef190d1b678)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"20"}]}]
}
 id : 6ac222df-7ac2-4e0b-bfd9-fef190d1b678
 nextStateId : Some(8f388945-425c-4661-bf54-b590d55df3eb)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="20"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="/html"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementText {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=21}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 8f388945-425c-4661-bf54-b590d55df3eb
 nextStateId : Some(f23592a7-da40-4873-8114-80925465835e)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/newJob"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="name", value="name"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=22}]
}
 id : f23592a7-da40-4873-8114-80925465835e
 nextStateId : Some(e9cafaf3-6cba-459b-82d4-4a13af29e231)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"22"}]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clearElement {id="22"}]
}
 id : e9cafaf3-6cba-459b-82d4-4a13af29e231
 nextStateId : Some(b3f41e72-7f46-4b5f-ab21-f65b564f371d)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"22"}]}]
}
 id : b3f41e72-7f46-4b5f-ab21-f65b564f371d
 nextStateId : Some(1ffa501f-65f5-4c62-a0cc-d9dc69bfceff)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, sendKeysToElement {id="22", value=["separate_coach"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="  .//input[@type='radio'][./@id = 'hudson.model.FreeStyleProject' or ./@name = 'hudson.model.FreeStyleProject' or ./@value = 'hudson.model.FreeStyleProject' or ./@placeholder = 'hudson.model.FreeStyleProject' or ./@id = //label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')]/@for]| .//label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')]//input[@type='radio']| .//label[contains(normalize-space(.), 'hudson.model.FreeStyleProject')][@class='attach-previous']/preceding-sibling::input[@type='radio']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=23}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 1ffa501f-65f5-4c62-a0cc-d9dc69bfceff
 nextStateId : Some(3eeec35b-a45e-40c3-a232-f07f7a10d41f)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"23"}]}]
}
 id : 3eeec35b-a45e-40c3-a232-f07f7a10d41f
 nextStateId : Some(180e42d6-4744-4cf9-9228-719cdd14ce46)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="23"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'OK' or ./@name = 'OK' or contains(./@value, 'OK')) or contains(./@title, 'OK'))] | .//input[./@type = 'image'][contains(./@alt, 'OK')] | .//button[(((./@id = 'OK' or contains(./@value, 'OK')) or contains(normalize-space(.), 'OK')) or contains(./@title, 'OK'))] | .//input[./@type = 'image'][contains(./@alt, 'OK')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=24}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 180e42d6-4744-4cf9-9228-719cdd14ce46
 nextStateId : Some(7a88abec-289b-4912-b62d-1c0e2746b53c)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"24"}]}]
}
 id : 7a88abec-289b-4912-b62d-1c0e2746b53c
 nextStateId : Some(33ddc187-abac-4928-af27-3b11776d017f)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="24"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/hetero-list-add[builder]']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=25}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 33ddc187-abac-4928-af27-3b11776d017f
 nextStateId : Some(127990a5-46a0-4d57-b594-6d5e36c21344)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"25"}]}]
}
 id : 127990a5-46a0-4d57-b594-6d5e36c21344
 nextStateId : Some(a625d3ed-5708-4886-b0c1-bff05bad87d8)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="25"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/hetero-list-add[builder]']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=25}]
}
 id : a625d3ed-5708-4886-b0c1-bff05bad87d8
 nextStateId : Some(62069fac-b8f0-40bf-960b-30675b687286)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="YAHOO.util.Dom.batch(    document.querySelector('.yui-menu-body-scrolled'),    function (el) {        el.style.height = 'auto';        YAHOO.util.Dom.removeClass(el, 'yui-menu-body-scrolled');    });", args=[]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="25", using="xpath", value="ancestor::*[contains(@class,'yui-menu-button')]/.."}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findChildElement {id="26", using="xpath", value=".//A[@href][@id='Execute shell' or normalize-space(.)='Execute shell' or @title='Execute shell' or .//img[@alt='Execute shell']]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 62069fac-b8f0-40bf-960b-30675b687286
 nextStateId : Some(14b70115-21ce-44f5-ade4-52e019ae64c0)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"27"}]}]
}
 id : 14b70115-21ce-44f5-ade4-52e019ae64c0
 nextStateId : Some(1deadeff-6941-45dd-866a-f0d0651c2237)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="27"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//div[@name='builder']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=28}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="xpath", value="//div[@name='builder']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementAttribute {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, name=path, id=28}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=29}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=29}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=29}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElements {using="css selector", value="[path='/builder/command']"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=29}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCurrentUrl {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="//*[@path='/builder/command']"}]
}
 id : 1deadeff-6941-45dd-866a-f0d0651c2237
 nextStateId : Some(d1bc4a78-b793-40cd-8d1c-9dd56779b451)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="cmElem = document.evaluate(        arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;codemirror = cmElem.CodeMirror;if (codemirror == null) {    console.log('CodeMirror object not found!');}codemirror.setValue(arguments[1]);codemirror.save();", args=["//*[@path='/builder/command']/following-sibling::div","curl http://134.96.235.47:8001/jenkins1.625.3/job/oral_aquarium/buildWithParameters?token=TOKEN\\&ID=id_to_pass"]}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'Save' or ./@name = 'Save' or contains(./@value, 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')] | .//button[(((./@id = 'Save' or contains(./@value, 'Save')) or contains(normalize-space(.), 'Save')) or contains(./@title, 'Save'))] | .//input[./@type = 'image'][contains(./@alt, 'Save')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=30}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : d1bc4a78-b793-40cd-8d1c-9dd56779b451
 nextStateId : Some(8c177199-9067-419a-864f-c3d3eaaa43be)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"30"}]}]
}
 id : 8c177199-9067-419a-864f-c3d3eaaa43be
 nextStateId : Some(452469a9-860a-47e3-9fdd-0dd186ac567e)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="30"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value="/html"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getElementText {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=31}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 452469a9-860a-47e3-9fdd-0dd186ac567e
 nextStateId : Some(d2f09054-4255-4d6b-b1f4-232f61cf3178)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/job/separate_coach/build?delay=0sec"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getTitle {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, findElement {using="xpath", value=".//input[./@type = 'submit' or ./@type = 'reset' or ./@type = 'image' or ./@type = 'button'][((./@id = 'Proceed' or ./@name = 'Proceed' or contains(./@value, 'Proceed')) or contains(./@title, 'Proceed'))] | .//input[./@type = 'image'][contains(./@alt, 'Proceed')] | .//button[(((./@id = 'Proceed' or contains(./@value, 'Proceed')) or contains(normalize-space(.), 'Proceed')) or contains(./@title, 'Proceed'))] | .//input[./@type = 'image'][contains(./@alt, 'Proceed')]"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, isElementDisplayed {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce, id=32}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : d2f09054-4255-4d6b-b1f4-232f61cf3178
 nextStateId : Some(940e1216-1bf3-4705-b88e-3de91f2f1d73)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, executeScript {script="// Visually navigate to the element in order to interact with it.\n// Elements without path attribute are ignored\n\nvar e = arguments[0];\n\nif (e.getAttribute(\"path\")) {\n    // Scroll to the element. It will appear at the top edge of the screen.\n    e.scrollIntoView();\n    // Scroll a bit back so breadcrumbs are not hiding the element.\n    window.scrollBy(0, -40);\n}\n", args=[{"ELEMENT":"32"}]}]
}
 id : 940e1216-1bf3-4705-b88e-3de91f2f1d73
 nextStateId : Some(0e5df105-f323-4d00-828c-b270a8ae2575)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, clickElement {id="32"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 0e5df105-f323-4d00-828c-b270a8ae2575
 nextStateId : Some(5ee85350-b445-487b-bc1f-114f4558c0e1)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 5ee85350-b445-487b-bc1f-114f4558c0e1
 nextStateId : Some(ccfa43a1-50fb-457c-a6d0-9ccdf8cd94aa)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : ccfa43a1-50fb-457c-a6d0-9ccdf8cd94aa
 nextStateId : Some(ba0f9113-7a16-4a2d-97c0-6541e040be99)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/job/separate_coach/1/console"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : ba0f9113-7a16-4a2d-97c0-6541e040be99
 nextStateId : Some(a2abb1c0-87fb-4465-8cc4-4dcca298196b)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : a2abb1c0-87fb-4465-8cc4-4dcca298196b
 nextStateId : Some(0fa912b4-d8b6-4912-9ec8-3093472d73dc)}
,
 actions : {
[c03ad187-87d7-4163-8cb7-4592b526d2a6, get {url="http://134.96.235.47:8001/jenkins1.625.3/job/oral_aquarium/lastBuild/console"}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getPageSource {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}],
[c03ad187-87d7-4163-8cb7-4592b526d2a6, getCookies {sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]
}
 id : 0fa912b4-d8b6-4912-9ec8-3093472d73dc
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