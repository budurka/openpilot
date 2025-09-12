from cereal import car
from openpilot.selfdrive.car import AngleRateLimit, dbc_dict
from openpilot.selfdrive.car.docs_definitions import CarDocs, CarHarness, CarSpecs, Column, Row, DataFormat
from openpilot.selfdrive.car.fw_query_definitions import FwQueryConfig, Request, StdQueries, p16

Ecu = car.CarParams.Ecu
CAR = car.CarParams.CarModel

class SubaruFlags:
  IS_DBW = "isDbw"

FINGERPRINTS = {
  CAR.OUTBACK: [{
    # 2024 Subaru Outback (D-harness)
    0x002: 8, 0x040: 8, 0x041: 8, 0x044: 8,
    0x048: 8, 0x049: 8, 0x04A: 8, 0x110: 8,
    0x111: 8, 0x112: 8, 0x118: 8, 0x119: 8,
    0x11A: 8, 0x11E: 8, 0x11F: 8, 0x121: 8,
    0x122: 8, 0x124: 8, 0x138: 8, 0x139: 8,
    0x13A: 8, 0x13B: 8, 0x13C: 8, 0x145: 8,
    0x146: 8,
  }],
}

DBC = {
  CAR.OUTBACK: dbc_dict('subaru_global_2020', None),
}

FW_VERSIONS = {
  CAR.OUTBACK: {
    (Ecu.engine, 0x7e0, None): [
      b"2024 Outback Engine FW",
    ],
  },
}

CAR_INFO = {
  CAR.OUTBACK: CarDocs("Subaru Outback 2024", "All trims (D-harness)"),
}

HARNESS_CONFIG = {
  CAR.OUTBACK: CarHarness.subaru_d,
}
