# 测试可调用方法__call__()


class SalaryAccount:

    def __call__(self, salary):
        print("算工资啦")

        yearSalary = salary * 12
        daySalary = salary // 22.5
        hourSalary = daySalary // 8

        return dict(yearSalary=yearSalary, daySalary = daySalary, hourSalary = hourSalary)

s = SalaryAccount
print(s.__call__(s,3000))