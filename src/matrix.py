list1 = ['findElements {using="css selector", value="#search-results .item.result.app"}]',
'findElements {using="css selector", value=".loading"}]',
'findElement {using="css selector", value=".navbar"}]',
'findElement {using="css selector", value=".tab-link[href*=new]"}]',
'findElement {using="css selector", value=".app-name:nth-child(1)"}]',
'findElement {using="id", value="search-q"}]',
'findElement {using="id", value="search-results"}]',
'findElement {using="css selector", value=".product-details.listing.expanded.c img[class=\"icon\"]"}]',
'findElement {using="css selector", value=".info > h3"}]',
'findElement {using="css selector", value=".author"}]',
'findElement {using="css selector", value=".button.product.install"}]',
'findElement {using="css selector", value=".support-email > a"}]',
'findElement {using="css selector", value=".description"}]',
'findElement {using="css selector", value=".slider"}]',
'findElement {using="css selector", value="#footer a[href*=\"privacy\"]"}]',
'findElement {using="css selector", value=".abuse > a"}]'
]

list2 = ['findElements {using="css selector", value="#search-results .item.result.app-list-app"}]',
'findElements {using="css selector", value=".loading"}]',
'findElement {using="css selector", value=".navbar"}]',
'findElement {using="css selector", value=".tab-link[href*=popular]"}]',
'findElement {using="css selector", value=".info > h3"}]',
'findElement {using="id", value="search-q"}]',
'findElement {using="css selector", value=".product.mkt-tile .heading .icon"}]',
'findElement {using="css selector", value=".author"}]',
'findElement {using="css selector", value=".button.product.install"}]',
'findElement {using="css selector", value=".support-email > a"}]',
'findElement {using="css selector", value=".description"}]',
'findElement {using="css selector", value=".slider"}]',
'findElement {using="css selector", value="#footer a[href*=\"privacy\"]"}]',
'findElement {using="css selector", value=".button.abuse"}]']

for val in list1:
    if val not in list2:
        print "no"
