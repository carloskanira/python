
class Staff:
    def __init__(self, staff_id, full_name, base_salary, performance_rating, punctuality_score):
        self.staff_id = staff_id
        self.full_name = full_name
        self.base_salary = base_salary
        self.performance_rating = performance_rating
        self.punctuality_score = punctuality_score

    def computePerformanceBonus(self):
        if 90 <= self.performance_rating <= 100:
            return 0.15 * self.base_salary
        elif 80 <= self.performance_rating < 90:
            return 0.08 * self.base_salary
        elif 70 <= self.performance_rating < 80:
            return 0.04 * self.base_salary
        else:
            return 0

    def computePunctualityBonus(self):
        if self.punctuality_score >= 96:
            return 4000
        elif 90 <= self.punctuality_score < 96:
            return 1500
        else:
            return 0

    def computeTotalBonus(self):
        return self.computePerformanceBonus() + self.computePunctualityBonus()
class Supervisor(Staff):
    def computeTeamBonus(self):
        return 0.12 * self.base_salary

    def computeTotalBonus(self):
        return super().computeTotalBonus() + self.computeTeamBonus()
def generateSummaryReport(staff_list):
    report = "Staff ID | Full Name | Base Salary | Performance Bonus | Punctuality Bonus | Total Bonus\n"
    report += "-" * 80 + "\n"
    for staff in staff_list:
        performance_bonus = staff.computePerformanceBonus()
        punctuality_bonus = staff.computePunctualityBonus()
        total_bonus = staff.computeTotalBonus()
        report += f"{staff.staff_id} | {staff.full_name} | {staff.base_salary} | {performance_bonus} | {punctuality_bonus} | {total_bonus}\n"
    return report
def saveReportToFile(report):
    with open("staffIncentiveReport.txt", "w") as file:
        file.write(report)
def main():
    staff_list = []
    while True:
        try:
            staff_id = input("Enter staff ID: ")
            full_name = input("Enter full name: ")
            base_salary = float(input("Enter base salary: "))
            performance_rating = float(input("Enter performance rating (0-100): "))
            punctuality_score = float(input("Enter punctuality score (0-100): "))
            staff_member = Staff(staff_id, full_name, base_salary, performance_rating, punctuality_score)
            staff_list.append(staff_member)
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
            continue
        more = input("Do you want to add another staff member? (yes/no): ")
        if more.lower() != "yes":
            break
    report = generateSummaryReport(staff_list)
    print(report)
    saveReportToFile(report)
if __name__ == "__main__":
    main()
