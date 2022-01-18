
class ISBN:
    def controlNumber(self, number):
        newNumber = number.replace("-", "")
        sum = 0
        for i in range(len(newNumber)):
            if i % 2 == 0:
                sum += int(newNumber[i])
            else:
                sum += (int(newNumber[i]))*3
        remainder = sum % 10
        if remainder == 0:
            return 0
        return 10 - remainder

