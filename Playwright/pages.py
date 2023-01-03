class AddEmployeePage:
    def __init__(self, page, baseUrl):
        self.page = page
        self.baseUrl = baseUrl

    def navigate(self):
        self.page.goto(self.baseUrl + "/add_employee")

    def fillForm(self, employee):
        self.page.get_by_label("Name").fill(employee["name"])
        self.page.get_by_label("Email").fill(employee["email"])
        self.page.locator("#id_address_line1").fill(employee["address_line_1"])
        self.page.locator("#id_address_line2").fill(employee["address_line_2"])
        self.page.get_by_label("City").fill(employee["city"])
        self.page.get_by_label("Zip code").fill(employee["zip_code"])
        self.page.get_by_label("Hiring date").fill(employee["date"])
        self.page.get_by_label("Job title").fill(employee["title"])
        self.page.get_by_role("button", name="Add").click()


class EditEmployeePage:
    def __init__(self, page, baseUrl, employee_id):
        self.page = page
        self.baseUrl = baseUrl
        self.employee_id = employee_id

    def navigate(self):
        self.page.goto(f"{self.baseUrl}/employee/{self.employee_id}")


class EditBasicInfoPage:
    def __init__(self, page, baseUrl, employee_id):
        self.page = page
        self.baseUrl = baseUrl
        self.employee_id = employee_id

        self.name_input = page.get_by_label("Name")
        self.email_input =  page.get_by_label("Email")

    def navigate(self):
        self.page.goto(f"{self.baseUrl}/employee/{self.employee_id}/basic_info")

    def fillForm(self, employee):
        self.name_input.fill(employee["name"])
        self.email_input.fill(employee["email"])
        self.page.get_by_role("button", name="Update").click()

class EditAddressPage:
    def __init__(self, page, baseUrl, employee_id):
        self.page = page
        self.baseUrl = baseUrl
        self.employee_id = employee_id

        self.address_line_1_input = self.page.locator("#id_address_line1")
        self.address_line_2_input = self.page.locator("#id_address_line2")
        self.city_input = self.page.get_by_label("City")
        self.zip_code_input = self.page.get_by_label("Zip code")

    def navigate(self):
        self.page.goto(f"{self.baseUrl}/employee/{self.employee_id}/address")

    def fillForm(self, employee):
        self.address_line_1_input.fill(employee["address_line_1"])
        self.address_line_2_input.fill(employee["address_line_2"])
        self.city_input.fill(employee["city"])
        self.zip_code_input.fill(employee["zip_code"])
        self.page.get_by_role("button", name="Update").click()
