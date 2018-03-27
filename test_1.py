

def test_login(app, id_submit="edit-submit", class_wrapper="wrapper-for-giftcard-837",
               id_submit_product="submit-product837", wine="wine-for-giftcard-8490", click_prod="submit-product8490",
               remark="edit-s-remark", text="sendsometextsends", product_="submit-product10770"):


    #driver.maximize_window()

    #login
    app.User_login('anna@nxte.nl', 'testtest', 'name', 'pass', 'edit-submit')
    #first card
    app.first_card("3", '100', '.menu-mlid-3848 > a:nth-child(1)', "qty-card-field-249",
                    "price-card-field-249", "submit-card249")
    #second card card
    app.second_card('50', "2", "qty-card-field-690", "price-card-field-690", "submit-card690")

    # #next
    # driver.find_element_by_id(id_submit).click()
    #
    # #choosing to first card:
    #
    # driver.find_element_by_class_name(class_wrapper).click()
    # driver.find_element_by_id(id_submit_product).click()
    #
    # # vine
    # driver.find_element_by_class_name(wine).click()
    # driver.find_element_by_id(click_prod).click()
    #
    # WebDriverWait(driver, 5)
    # driver.find_element_by_id(remark).send_keys(text)
    # driver.find_element_by_id(product_).click()
    #
    # #next
    # driver.find_element_by_id(id_submit).click()



