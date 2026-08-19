from datetime import datetime


def format_report(func):
    def wrapper(self):
        print("=" * 50)
        print("DYNAMIC REPORT")
        print("=" * 50)
        func(self)
        print("=" * 50)
    return wrapper

class Report:
    report_count = 0

    def __init__(self, title, data):
        self.title = title
        self.data = data
        Report.report_count += 1
    @classmethod
    def total_reports(cls):
        return cls.report_count
    @format_report
    def generate(self):
        print(f"Title: {self.title}")
        print(f"Date: {datetime.now().strftime('%d-%m-%Y')}")
        print("-" * 50)
        for key, value in self.data.items():
            print(f"{key:<20}: {value}")
    def __str__(self):
        return f"Report: {self.title}"
    def __len__(self):
        return len(self.data)
data = {
    "Name": "xyz",
    "Department": "CSE",
    "Marks": 85,
    "Grade": "A"
}
report = Report("Student Performance Report", data)
print(report)
print("Number of fields:", len(report))
report.generate()
print("Total Reports Created:", Report.total_reports())