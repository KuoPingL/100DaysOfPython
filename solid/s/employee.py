class Employee:
    def __init__(self):
        self.base_salary = 10000
        self.base_hours = 8
        self.overtime = 0
        self.name = "John"
        self.employee_id = "000000"

    def calculate_pay(self):
        # 由會計部指定，向 CFO 報告
        return self.regular_hours() * 100

    def report_hours(self):
        # 由人事部指定，向 COO 報告
        return self.regular_hours()

    def save(self):
        # 由資料管理員指定，向 CTO 報告
        print(f"saving {self.base_salary} to database")

    def regular_hours(self):
        return self.base_hours + self.overtime







