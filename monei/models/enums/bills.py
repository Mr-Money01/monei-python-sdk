from enum import Enum


class BillCategory(str, Enum):
    AIRTIME = "AIRTIME"
    MOBILEDATA = "MOBILEDATA"
    CABLEBILLS = "CABLEBILLS"
    UTILITYBILLS = "UTILITYBILLS"