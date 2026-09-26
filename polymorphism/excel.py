class ExcelReport:
    def generate(self):
        print("Generating Excel report.")


class PDFReport:
    def generate(self):
        print("Generating PDF report.")


def generate_report(report):
    report.generate()


generate_report(ExcelReport())
generate_report(PDFReport())