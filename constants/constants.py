from dataclasses import dataclass, field
from typing import List

from os.path import join


SHEETNAVN = "MaanedsStatistik"
NAVNEKOL = "Navn"  # Den kolonne der indeholder medarb. 'Navn . (ini)'
INIKOL = "Ini"  # Kolonne der oprettes til at indeholde medarbejder-ini
AARKOL = "År"
AARSTAL = 2023
JANKOL = "jan"  # Kolonnenavn for 'Januar'-måned - små bogstaver


# rootpath rod-dir hvor FR med arket "maanedsStatistik" findes
# sourcepath mappe hvor pdf-timesedlerne findes
@dataclass
class Faelles:
    rootpath: str = r"F:\EUOkonomi\LIFE-Okonomi"
    frpath: str = r"1. FinancialReport"
    sourcepath: str = (
        r"F:\EUOkonomi\LIFE-Okonomi\mTidsstatistik\mTidsStatistik2023\MaanedsStatistik"
    )
    timeseddelpath: str = r"2. RegnskabsBilag\Bilag2023\Timesedler"
    navneliste: List[str] = field(default_factory=list)


@dataclass
class Kontrol(Faelles):
    projpath: str = r"Opfolgning\2023"
    filnavn: str = r"20240115_TidsUdtraek_Endelig2023.xlsx"
    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Kontrol.projpath, Kontrol.filnavn
        )
    )


@dataclass
class Bet(Faelles):
    projpath: str = r"LIFE-BetterBirdLife"
    filnavn: str = r"Naturstyrelsen og Kystdirektoratet2023Q4.xlsm"

    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Bet.projpath, Faelles.frpath, Bet.filnavn
        )
    )

    destinationpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Bet.projpath, Faelles.timeseddelpath
        )
    )


@dataclass
class Coast(Faelles):
    projpath: str = r"LIFE-CoastalLife"
    filnavn: str = r"NST-LIFECoastalLifeFinancialReporting2023Q4.xlsx"
    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Coast.projpath, Faelles.frpath, Coast.filnavn
        )
    )

    destinationpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Coast.projpath, Faelles.timeseddelpath
        )
    )


@dataclass
class Hoj(Faelles):
    projpath: str = r"LIFE-Hojmose"
    filnavn: str = r"NST_HojMoseFinancialReport2023Q3.xlsx"
    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Hoj.projpath, Faelles.frpath, Hoj.filnavn
        )
    )

    destinationpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Hoj.projpath, Faelles.timeseddelpath
        )
    )


@dataclass
class Wadsea(Faelles):
    projpath: str = r"LIFE-WattenSeaBird"
    filnavn: str = r"NST-LIFEWadSeaFinancialReporting2023Q4.xlsx"
    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Wadsea.projpath, Faelles.frpath, Wadsea.filnavn
        )
    )

    destinationpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Wadsea.projpath, Faelles.timeseddelpath
        )
    )


@dataclass
class Orchids(Faelles):
    projpath: str = r"LIFE-Orchid"
    filnavn: str = r"NST-LIFEOrchidFinancialReporting2023Q4.xlsx"
    filpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Orchids.projpath, Faelles.frpath, Orchids.filnavn
        )
    )

    destinationpath: str = field(
        default_factory=lambda: join(
            Faelles.rootpath, Orchids.projpath, Faelles.timeseddelpath
        )
    )
