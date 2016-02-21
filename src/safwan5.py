from collections import Counter

data = ['setWindowSize{windowHandle="current",width=1024,height=768}', 'setTimeout{type="pageload",ms=30000}', 'implicitlyWait{ms=1000}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/configureSecurity/"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="cssselector",value="[path=\'/useSecurity\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=0}', 'isElementSelected{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=0}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"0"}]}]\n', 'clickElement{id="0"}', 'findElements{using="xpath",value=".//input[@type=\'radio\'][./@id=\'Delegatetoservletcontainer\'or./@name=\'Delegatetoservletcontainer\'or./@value=\'Delegatetoservletcontainer\'or./@placeholder=\'Delegatetoservletcontainer\'or./@id=//label[contains(normalize-space(.),\'Delegatetoservletcontainer\')]/@for]|.//label[contains(normalize-space(.),\'Delegatetoservletcontainer\')]//input[@type=\'radio\']|.//label[contains(normalize-space(.),\'Delegatetoservletcontainer\')][@class=\'attach-previous\']/preceding-sibling::input[@type=\'radio\']"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"1"}]}]\n', 'clickElement{id="1"}', 'getElementAttribute{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,name=path,id=1}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'Save\'or./@name=\'Save\'orcontains(./@value,\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]|.//button[(((./@id=\'Save\'orcontains(./@value,\'Save\'))orcontains(normalize-space(.),\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=2}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"2"}]}]\n', 'clickElement{id="2"}', 'findElement{using="xpath",value="/html"}', 'getElementText{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=3}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/newJob"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="name",value="name"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=4}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"4"}]}', 'clearElement{id="4"}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"4"}]}]\n', 'sendKeysToElement{id="4",value=["oral_aquarium"]}', 'findElement{using="xpath",value=".//input[@type=\'radio\'][./@id=\'hudson.model.FreeStyleProject\'or./@name=\'hudson.model.FreeStyleProject\'or./@value=\'hudson.model.FreeStyleProject\'or./@placeholder=\'hudson.model.FreeStyleProject\'or./@id=//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')]/@for]|.//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')]//input[@type=\'radio\']|.//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')][@class=\'attach-previous\']/preceding-sibling::input[@type=\'radio\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=5}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"5"}]}]\n', 'clickElement{id="5"}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'OK\'or./@name=\'OK\'orcontains(./@value,\'OK\'))orcontains(./@title,\'OK\'))]|.//input[./@type=\'image\'][contains(./@alt,\'OK\')]|.//button[(((./@id=\'OK\'orcontains(./@value,\'OK\'))orcontains(normalize-space(.),\'OK\'))orcontains(./@title,\'OK\'))]|.//input[./@type=\'image\'][contains(./@alt,\'OK\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=6}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"6"}]}]\n', 'clickElement{id="6"}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="xpath",value="//input[@name=\'parameterized\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=7}', 'isElementSelected{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=7}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"7"}]}]\n', 'clickElement{id="7"}', 'findElement{using="xpath",value="//button[text()=\'AddParameter\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=8}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"8"}]}]\n', 'clickElement{id="8"}', 'findElement{using="xpath",value="//button[text()=\'AddParameter\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=8}]\n', 'executeScript{script="YAHOO.util.Dom.batch(document.querySelector(\'.yui-menu-body-scrolled\'),function(el){el.style.height=\'auto\';YAHOO.util.Dom.removeClass(el,\'yui-menu-body-scrolled\');});",args=[]}', 'findChildElement{id="8",using="xpath",value="ancestor::*[contains(@class,\'yui-menu-button\')]/.."}', 'findChildElement{id="9",using="xpath",value=".//A[@href][@id=\'StringParameter\'ornormalize-space(.)=\'StringParameter\'or@title=\'StringParameter\'or.//img[@alt=\'StringParameter\']]"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"10"}]}]\n', 'clickElement{id="10"}', 'findElement{using="xpath",value="//div[@name=\'parameter\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=11}', 'findElements{using="xpath",value="//div[@name=\'parameter\']"}', 'getElementAttribute{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,name=path,id=11}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="cssselector",value="[path=\'/properties/hudson-model-ParametersDefinitionProperty/parameterized/parameter/name\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=12}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"12"}]}', 'clearElement{id="12"}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"12"}]}]\n', 'sendKeysToElement{id="12",value=["ID"]}', 'findElement{using="cssselector",value="[path=\'/pseudoRemoteTrigger\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=13}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"13"}]}]\n', 'clickElement{id="13"}', 'findElement{using="name",value="authToken"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=14}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"14"}]}', 'clearElement{id="14"}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"14"}]}]\n', 'sendKeysToElement{id="14",value=["TOKEN"]}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="cssselector",value="[path=\'/hetero-list-add[builder]\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=15}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"15"}]}]\n', 'clickElement{id="15"}', 'findElement{using="cssselector",value="[path=\'/hetero-list-add[builder]\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=15}]\n', 'executeScript{script="YAHOO.util.Dom.batch(document.querySelector(\'.yui-menu-body-scrolled\'),function(el){el.style.height=\'auto\';YAHOO.util.Dom.removeClass(el,\'yui-menu-body-scrolled\');});",args=[]}', 'findChildElement{id="15",using="xpath",value="ancestor::*[contains(@class,\'yui-menu-button\')]/.."}', 'findChildElement{id="16",using="xpath",value=".//A[@href][@id=\'Executeshell\'ornormalize-space(.)=\'Executeshell\'or@title=\'Executeshell\'or.//img[@alt=\'Executeshell\']]"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"17"}]}]\n', 'clickElement{id="17"}', 'findElement{using="xpath",value="//div[@name=\'builder\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=18}', 'findElements{using="xpath",value="//div[@name=\'builder\']"}', 'getElementAttribute{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,name=path,id=18}', 'findElement{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=19}', 'findElements{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=19}', 'findElement{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=19}', 'findElements{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=19}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="xpath",value="//*[@path=\'/builder/command\']"}]\n', 'executeScript{script="cmElem=document.evaluate(arguments[0],document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue;codemirror=cmElem.CodeMirror;if(codemirror==null){console.log(\'CodeMirrorobjectnotfound!\');}codemirror.setValue(arguments[1]);codemirror.save();",args=["//*[@path=\'/builder/command\']/following-sibling::div","test\'id_to_pass\'=$ID"]}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'Save\'or./@name=\'Save\'orcontains(./@value,\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]|.//button[(((./@id=\'Save\'orcontains(./@value,\'Save\'))orcontains(normalize-space(.),\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=20}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"20"}]}]\n', 'clickElement{id="20"}', 'findElement{using="xpath",value="/html"}', 'getElementText{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=21}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/newJob"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="name",value="name"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=22}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"22"}]}', 'clearElement{id="22"}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"22"}]}]\n', 'sendKeysToElement{id="22",value=["separate_coach"]}', 'findElement{using="xpath",value=".//input[@type=\'radio\'][./@id=\'hudson.model.FreeStyleProject\'or./@name=\'hudson.model.FreeStyleProject\'or./@value=\'hudson.model.FreeStyleProject\'or./@placeholder=\'hudson.model.FreeStyleProject\'or./@id=//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')]/@for]|.//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')]//input[@type=\'radio\']|.//label[contains(normalize-space(.),\'hudson.model.FreeStyleProject\')][@class=\'attach-previous\']/preceding-sibling::input[@type=\'radio\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=23}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"23"}]}]\n', 'clickElement{id="23"}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'OK\'or./@name=\'OK\'orcontains(./@value,\'OK\'))orcontains(./@title,\'OK\'))]|.//input[./@type=\'image\'][contains(./@alt,\'OK\')]|.//button[(((./@id=\'OK\'orcontains(./@value,\'OK\'))orcontains(normalize-space(.),\'OK\'))orcontains(./@title,\'OK\'))]|.//input[./@type=\'image\'][contains(./@alt,\'OK\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=24}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"24"}]}]\n', 'clickElement{id="24"}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="cssselector",value="[path=\'/hetero-list-add[builder]\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=25}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"25"}]}]\n', 'clickElement{id="25"}', 'findElement{using="cssselector",value="[path=\'/hetero-list-add[builder]\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=25}]\n', 'executeScript{script="YAHOO.util.Dom.batch(document.querySelector(\'.yui-menu-body-scrolled\'),function(el){el.style.height=\'auto\';YAHOO.util.Dom.removeClass(el,\'yui-menu-body-scrolled\');});",args=[]}', 'findChildElement{id="25",using="xpath",value="ancestor::*[contains(@class,\'yui-menu-button\')]/.."}', 'findChildElement{id="26",using="xpath",value=".//A[@href][@id=\'Executeshell\'ornormalize-space(.)=\'Executeshell\'or@title=\'Executeshell\'or.//img[@alt=\'Executeshell\']]"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"27"}]}]\n', 'clickElement{id="27"}', 'findElement{using="xpath",value="//div[@name=\'builder\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=28}', 'findElements{using="xpath",value="//div[@name=\'builder\']"}', 'getElementAttribute{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,name=path,id=28}', 'findElement{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=29}', 'findElements{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=29}', 'findElement{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=29}', 'findElements{using="cssselector",value="[path=\'/builder/command\']"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=29}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCurrentUrl{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="xpath",value="//*[@path=\'/builder/command\']"}]\n', 'executeScript{script="cmElem=document.evaluate(arguments[0],document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue;codemirror=cmElem.CodeMirror;if(codemirror==null){console.log(\'CodeMirrorobjectnotfound!\');}codemirror.setValue(arguments[1]);codemirror.save();",args=["//*[@path=\'/builder/command\']/following-sibling::div","curlhttp://134.96.235.47:8001/jenkins1.625.3/job/oral_aquarium/buildWithParameters?token=TOKEN\\&ID=id_to_pass"]}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'Save\'or./@name=\'Save\'orcontains(./@value,\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]|.//button[(((./@id=\'Save\'orcontains(./@value,\'Save\'))orcontains(normalize-space(.),\'Save\'))orcontains(./@title,\'Save\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Save\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=30}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"30"}]}]\n', 'clickElement{id="30"}', 'findElement{using="xpath",value="/html"}', 'getElementText{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=31}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/job/separate_coach/build?delay=0sec"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getTitle{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'findElement{using="xpath",value=".//input[./@type=\'submit\'or./@type=\'reset\'or./@type=\'image\'or./@type=\'button\'][((./@id=\'Proceed\'or./@name=\'Proceed\'orcontains(./@value,\'Proceed\'))orcontains(./@title,\'Proceed\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Proceed\')]|.//button[(((./@id=\'Proceed\'orcontains(./@value,\'Proceed\'))orcontains(normalize-space(.),\'Proceed\'))orcontains(./@title,\'Proceed\'))]|.//input[./@type=\'image\'][contains(./@alt,\'Proceed\')]"}', 'isElementDisplayed{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce,id=32}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'executeScript{script="//Visuallynavigatetotheelementinordertointeractwithit.\n//Elementswithoutpathattributeareignored\n\nvare=arguments[0];\n\nif(e.getAttribute("path")){\n//Scrolltotheelement.Itwillappearatthetopedgeofthescreen.\ne.scrollIntoView();\n//Scrollabitbacksobreadcrumbsarenothidingtheelement.\nwindow.scrollBy(0,-40);\n}\n",args=[{"ELEMENT":"32"}]}]\n', 'clickElement{id="32"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/job/separate_coach/1/console"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n', 'get{url="http://134.96.235.47:8001/jenkins1.625.3/job/oral_aquarium/lastBuild/console"}', 'getPageSource{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}', 'getCookies{sessionId=7769a6d6-c06d-40b5-ad82-3b473a6f55ce}]\n']


dictionary = {
    'findElement':'using',
    'findChildElements': 'using',
    'findChildElement': 'using'
}

exception=['clickElement',
	'sendKeysToElement',
    'implicitlyWait',
    'executeScript',
    'getElementText',
    'get']

my_list = []
for item in data:
    items = item.split('{')
    action = items[0]
    if action in dictionary and action not in exception :
        splitter = dictionary[action] + '="'
        element = items[1].split(splitter)[1].split(',')[0]
        tuple = (action, element)
        my_list.append(tuple)

print Counter(my_list)