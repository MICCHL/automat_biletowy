from enum import Enum


class TicketNames(Enum):
    STUDENT_SHORT = 'Bilet ulgowy 20 min \n 1,70 zł'
    SHORT = 'Bilet normalny 20 min \n 3,40 zł'
    STUDENT_NORMAL = 'Bilet ulgowy 50 min \n 2, 30zł'
    NORMAL = 'Bilet normalny 50 min \n 4,60zł'
    STUDENT_LONG = 'Bilet ulgowy 90 min \n 3zł'
    LONG = 'Bilet normalny 90 min \n 6zł'

    def __str__(self):
        return str(self.value)
