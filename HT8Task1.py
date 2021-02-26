class Data:
    def __init__(self, line):
        self.date = line.split('-')

    @staticmethod
    def validation(line):
        forvalid = line.split("-")
        if 0 < int(forvalid[0]) < 32 and 0 < int(forvalid[1]) < 12:
            if int(forvalid[1]) == 2:
                if int(forvalid[2]) % 4 == 0 and int(forvalid[2]) % 100 != 0:
                    if int(forvalid[0]) < 30:
                        return True
                    else:
                        return False
                else:
                    if int(forvalid[0]) < 29:
                        return True
                    else:
                        return False
            return True
        else:
            return False

    @classmethod
    def get_full_date(cls, line):
        cls.date = line.split('-')
        if Data.validation(line) is True:
            return f'DD:{cls.date[0]} MM:{cls.date[1]} YYYY:{cls.date[2]}'


a = Data('29-02-95')
print(a.get_full_date('28-02-2021'))
