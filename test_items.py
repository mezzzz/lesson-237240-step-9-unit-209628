
def test_add_to_basket_form(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert is_element_present(browser) == True, "button didn't found"


def is_element_present(browser):
    try:
        browser.implicitly_wait(3)
        browser.find_element_by_css_selector('#add_to_basket_form button')
        return True
    except:
        return False


