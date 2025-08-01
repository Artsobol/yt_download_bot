from enum import Enum


class Itag(Enum):
    P_1080 = 137
    P_720 = 136
    P_480 = 135
    P_360 = 134
    P_240 = 133
    P_144 = 160

    def __str__(self):
        return f"{self.name[2:]}p"
