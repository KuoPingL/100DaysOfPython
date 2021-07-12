# 業務
class SalesRepresentative:
    def find_client(self):
        # 找客戶
        pass


# 產品經理
class ProductManager:
    def manage_product(self):
        # 控管產品
        pass


# 研究人員
class ResearchDeveloper:
    def do_some_research(self):
        # 研發
        pass

    def prepare_research_presentation(self):
        # 準備研究報告
        pass


# 清潔工
class Cleaner:
    def clean_the_office(self):
        # 打掃辦公室
        pass


# 會計
class Accountant:
    def do_accounting(self):
        # 財務報告
        pass


class BossB:
    def get_financial_report(self, accountant: Accountant):
        accountant.do_accounting()

    def listen_to_research_report(self, rd: ResearchDeveloper):
        rd.prepare_research_presentation()

    def find_funder(self):
        print("Searching for funders")

    # more actions





