import datetime
import re
from playwright.sync_api import Playwright, sync_playwright, Page, expect
import pytest 
from dataclasses import dataclass
from pages import AddEmployeePage, EditBasicInfoPage, EditAddressPage

## Creer une classe user ?

BASE_URL = "https://y.hr.dmerej.info"
RESET_PATH = "/reset_db"

# @dataclass
# class Employee:
#     name: str
#     email: str
#     address_line_1: str
#     address_line_2: str
#     city: str
#     zip_code: str
#     date: str
#     title: str
#     manager: bool = False

employee1 = {"name":"Employee 1", 
            "email":"email1@test.com", 
            "address_line_1":"123 Fake Street", 
            "address_line_2":"Appt 42", 
            "city":"Paris", 
            "zip_code":"75001", 
            "date":"2023-01-01",
            "title":"General Manager"}

employee2 = {"name":"Employee 2", 
            "email":"email2@test.com", 
            "address_line_1":"456 Rue Blanche", 
            "address_line_2":"Escalier A", 
            "city":"Lille", 
            "zip_code":"59000", 
            "date":"2022-01-01",
            "title":"CEO"}


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # Go to the starting url before each test.
    page.goto(BASE_URL)
    yield
    clean_database(page)

def clean_database(page: Page):
    page.goto(BASE_URL + RESET_PATH)
    page.get_by_role("button", name="Proceed").click()

def add_employee(page: Page, employee):
    add_employee_page = AddEmployeePage(page, BASE_URL)
    add_employee_page.navigate()
    add_employee_page.fillForm(employee)

def test_1_add_employee(page: Page):
    add_employee(page, employee1)
    # Check if redirection
    expect(page).to_have_title(re.compile("Employees"))
    expect(page.get_by_role("cell", name=employee1["name"])).to_be_visible()


def test_2_update_basic_info(page: Page):
    add_employee(page, employee1)

    id = page.get_by_role("link", name="Edit").get_attribute("href").split('/')[-1]

    basic_info_page = EditBasicInfoPage(page, BASE_URL, id)
    basic_info_page.navigate()
    basic_info_page.fillForm(employee2)
    basic_info_page.navigate()

    expect(basic_info_page.name_input).to_have_value(employee2['name'])
    expect(basic_info_page.email_input).to_have_value(employee2['email'])

def test_3_update_address(page: Page):
    add_employee(page, employee1)

    id = page.get_by_role("link", name="Edit").get_attribute("href").split('/')[-1]

    edit_address_page = EditAddressPage(page, BASE_URL, id)
    edit_address_page.navigate()
    edit_address_page.fillForm(employee2)
    edit_address_page.navigate()


    expect(edit_address_page.address_line_1_input).to_have_value(employee2['address_line_1'])
    expect(edit_address_page.address_line_2_input).to_have_value(employee2['address_line_2'])
    expect(edit_address_page.city_input).to_have_value(employee2['city'])
    expect(edit_address_page.zip_code_input).to_have_value(employee2['zip_code'])









    
