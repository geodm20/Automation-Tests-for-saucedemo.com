from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import random
import time

s = Service(r'C:\Users\yourroute') # Your route goes here
driver = webdriver.Chrome(service=s)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
valid_username = "standard_user"
invalid_password = "wrong_password"
valid_password = "secret_sauce"

# This step is necessary in many of the test cases
def login():
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    username_input.clear()
    password_input.clear()
    username_input.send_keys(valid_username)
    time.sleep(0.5)
    password_input.send_keys(valid_password)
    time.sleep(0.5)
    driver.find_element(By.ID, "login-button").click()

# TC-01: Logging In with invalid credentials
def invalid_login():
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    username_input.clear()
    password_input.clear()
    username_input.send_keys(valid_username)
    time.sleep(0.5)
    password_input.send_keys(invalid_password)
    time.sleep(0.5)
    driver.find_element(By.ID, "login-button").click()
    if "Epic sadface: Username and password do not match any user in this service" in driver.page_source:
        print("Login invalid: TC-01 successful")
        time.sleep(0.5)
        username_input.clear()
        password_input.clear()
    else:
        print("TC-01 failed")
    driver.refresh()

invalid_login()

# TC-02: Logging In with valid credentials
def valid_login():
    login()
    time.sleep(0.5)
    if "Epic sadface: Username and password do not match any user in this service" not in driver.page_source:
        print("Login valid: TC-02 successful")
    else:
        print("TC-02 failed")

valid_login()

# TC-03: Log out after logging in
def log_out():
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(0.5)
    if "https://www.saucedemo.com/" in driver.current_url:
        print("Logged out: TC-03 sucessful")
    else:
        print("TC-03 failed")

log_out()

# TC-04: Products visualization
def visualize_products():
    login()
    time.sleep(0.5)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products_list = []
    for index, product in enumerate(products, start = 1):
        title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        products_list.append({"id": index, "title": title, "price": price})
    if len(products_list) > 0:
        print("Product visualization: TC-04 successful")
        print(products_list)
    else:
        print("TC-04 failed")

visualize_products()

# TC-05: Adding a product to the Cart
def adding_removing_product():
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    if products:
        random_product = random.randint(0, len(products) - 1)
        products[random_product].click()
        time.sleep(0.5)
        product_add = driver.find_element(By.CLASS_NAME, "btn_inventory")
        product_add.click()
        time.sleep(0.5)
        cart_count = int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
        if cart_count == 1:
            print("Adding products: TC-05 successful")
            # TC-06: Removing a product from the Cart
            product_remove = driver.find_element(By.CLASS_NAME, "btn_inventory")
            product_remove.click()
            time.sleep(0.2)
            cart_count_zero = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_count_zero_elements = cart_count_zero.find_elements(By.XPATH, "./*")
            if len(cart_count_zero_elements) == 0:
                print("Removing products: TC-06 successful")
            else:
                print("TC-06 failed")
        else:
            print("TC-05 failed")
    else:
        print("TC-05 failed: no products available")

adding_removing_product()

# TC-07: Sorting products by name or price
def sorting_products():
    driver.find_element(By.CLASS_NAME, "left_component").click()
    time.sleep(0.5)
    # Get products by default
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products_list = []
    for index, product in enumerate(products, start = 1):
        title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        products_list.append({"id": index, "title": title, "price": price})
    filter_icon = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filter_icon.click()
    time.sleep(0.5)
    # Get products sorted
    filters = filter_icon.find_elements(By.XPATH, "./*")
    random_filter = random.randint(1, len(filters) - 1)
    filters[random_filter].click()
    time.sleep(0.5)
    products_sorted = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products_list_sorted = []
    for index, product in enumerate(products_sorted, start = 1):
        title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        products_list_sorted.append({"id": index, "title": title, "price": price})
    filter_icon = driver.find_element(By.CLASS_NAME, "product_sort_container")
    if products_list != products_list_sorted:
        print("Sorting products: TC-07 successful")
    else:
        print("TC-07 failed")

sorting_products()

# TC-08 Adding multiple items to the cart
def adding_multiple_items():
    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    if len(buttons) > 0:
        # To click a random number of buttons available
        random_number1 = random.randint(2, len(buttons))
        selected_indices = []
        first_number = random_number1
        while random_number1 >= 1:
            buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
            # Second random number must be unique to not click the same button
            while True:
                random_number2 = random.randint(0, len(buttons) - 1)
                if random_number2 not in selected_indices:
                    break
            selected_indices.append(random_number2)
            buttons[random_number2].click()
            random_number1 -= 1
            time.sleep(0.2)
        time.sleep(2)
        cart_amount = int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
        if cart_amount == first_number:
            print("Adding items: TC-08 successful")
        else:
            print("TC-08 failed")
        
adding_multiple_items()

# TC-09: Checking buying functionality
def buying_function():
    try:
        driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "checkout_button").click()
        time.sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("First Name")
        time.sleep(0.3)
        driver.find_element(By.ID, "last-name").send_keys("Last Name")
        time.sleep(0.3)
        driver.find_element(By.ID, "postal-code").send_keys("91000")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        print("Buying function: TC-09 successful")
    except:
        print("TC-09 failed")

buying_function()

driver.quit()