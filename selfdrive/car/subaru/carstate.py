# selfdrive/car/subaru/carstate.py
from cereal import car
from openpilot.selfdrive.car.interfaces import CarStateBase

class CarState(CarStateBase):
  def update(self, cp, cp_cam=None):
    # Minimal CarState: fill the bare essentials so the interface can run.
    ret = car.CarState.new_message()

    # Leave these conservative/neutral until we parse real signals
    ret.vEgo = 0.0
    ret.vEgoRaw = 0.0
    ret.standstill = True
    ret.steeringAngleDeg = 0.0
    ret.steeringRateDeg = 0.0

    # Cruise & gear placeholders
    ret.cruiseState.available = False
    ret.cruiseState.enabled = False
    ret.cruiseState.speed = 0.0

    ret.gearShifter = car.CarState.GearShifter.unknown

    # Turn signal placeholders
    ret.leftBlinker = False
    ret.rightBlinker = False

    # Door/seatbelt placeholders
    ret.doorOpen = False
    ret.seatbeltUnlatched = False

    return ret
