# selfdrive/car/subaru/interface.py
from cereal import car
from openpilot.selfdrive.car.interfaces import CarInterfaceBase
from openpilot.selfdrive.car.subaru.values import CAR

EventName = car.CarEvent.EventName

class CarInterface(CarInterfaceBase):
  @staticmethod
  def get_params(candidate, fingerprints=None, car_fw=None, experimental_long=False, docs=False):
    ret = CarInterfaceBase.get_std_params(candidate, fingerprints, car_fw)

    # Basic identity
    ret.carName = "subaru"
    ret.safetyConfigs = CarInterfaceBase.get_safety_config("subaru_canfd")

    # We start in dashcam-only to prevent any engagement while we bring signals up
    ret.dashcamOnly = True

    # Subaru uses stock longitudinal; leave OP long off to be safe
    ret.openpilotLongitudinalControl = False
    ret.pcmCruise = False

    # Very rough initial specs; we’ll refine later
    # 2024 Outback: ~1650 kg curb + 75 kg, wheelbase ~2.67 m, SR ~13.5
    ret.mass = 1650. + 75.
    ret.wheelbase = 2.67
    ret.steerRatio = 13.5
    ret.centerToFront = ret.wheelbase * 0.41

    # Tuning placeholders (not used while dashcamOnly True, but harmless)
    ret.steerActuatorDelay = 0.1
    ret.steerLimitTimer = 1.0

    return ret

  def _update(self, c):
    # Parse CAN using the base helper (no custom CAN parser yet)
    ret = self.CS.update(self.cp, getattr(self, "cp_cam", None))

    # Always add a blocking event so the system remains view-only
    events = self.create_common_events(ret)
    events.add(EventName.carUnrecognized)  # explicit no-entry until we wire signals

    ret.events = events.to_msg()
    return ret

  def apply(self, c):
    # No controls yet; return empty control msg
    return car.CarControl.new_message()
