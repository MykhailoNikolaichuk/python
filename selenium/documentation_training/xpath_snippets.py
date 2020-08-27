# //img[contains(@src, 'CB46')]
# //script[starts-with(@type, 'a-state')]

# //*[text()='Orders']

# /bookstore/book[position()<3] Selects the first two book elements that are children of the bookstore element

# /bookstore/book[last()]	Selects the last book element that is the child of the bookstore element
# /bookstore/book[last()-1] Selects the last but one book element that is the child of the bookstore element

# //book/title | //book/price	Selects all the title AND price elements of all book elements


'''
++link: Features
1. //a[text()='Features']
2. //a[contains(text(),'Features')] --recommended

++button:
//button[@type='button' and @class='btn']
//button[contains(text(),'Sign Up')]
//div[@class='dropdown']//button[@type='button' and @class='btn btn-secondary dropdown-toggle' and @id='dropdownMenuButton']
//button[@id='dropdownMenuButton']

++preceding-sibling:
//a[text()='test2 test2']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input

++parent & preceding-sibling:

//a[text()='test2 test2']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input[@name='contact_id']

'''