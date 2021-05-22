# flake8: noqa
try:
    # python 3.7 and earlier
    from importlib_metadata import version  # type: ignore
except ImportError:
    # python 3.8 and later
    from importlib.metadata import version  # type: ignore

from .airconditioner_miot import AirConditionerMiot
from .airconditioningcompanion import (
    AirConditioningCompanion,
    AirConditioningCompanionV3,
)
from .airconditioningcompanionMCN import AirConditioningCompanionMcn02
from .airdehumidifier import AirDehumidifier
from .airfresh import AirFresh, AirFreshVA4
from .airfresh_t2017 import AirFreshA1, AirFreshT2017
from .airhumidifier import AirHumidifier, AirHumidifierCA1, AirHumidifierCB1
from .airhumidifier_jsq import AirHumidifierJsq
from .airhumidifier_miot import AirHumidifierMiot
from .airhumidifier_mjjsq import AirHumidifierMjjsq
from .airpurifier import AirPurifier
from .airpurifier_airdog import AirDogX3, AirDogX5, AirDogX7SM
from .airpurifier_miot import AirPurifierMiot
from .airqualitymonitor import AirQualityMonitor
from .aqaracamera import AqaraCamera
from .ceil import Ceil
from .chuangmi_camera import ChuangmiCamera
from .chuangmi_ir import ChuangmiIr
from .chuangmi_plug import ChuangmiPlug, Plug, PlugV1, PlugV3
from .cooker import Cooker
from .curtain_youpin import CurtainMiot
from .device import Device
from .exceptions import DeviceError, DeviceException
from .fan import Fan, FanP5, FanSA1, FanV2, FanZA1, FanZA4
from .fan_leshow import FanLeshow
from .fan_miot import FanMiot, FanP9, FanP10, FanP11
from .gateway import Gateway
from .heater import Heater
from .heater_miot import HeaterMiot
from .huizuo import Huizuo
from .miot_device import MiotDevice
from .philips_bulb import PhilipsBulb, PhilipsWhiteBulb
from .philips_eyecare import PhilipsEyecare
from .philips_moonlight import PhilipsMoonlight
from .philips_rwread import PhilipsRwread
from .powerstrip import PowerStrip
from .protocol import Message, Utils
from .pwzn_relay import PwznRelay
from .toiletlid import Toiletlid
from .vacuum import Vacuum, VacuumException
from .vacuum_tui import VacuumTUI
from .vacuumcontainers import (
    CleaningDetails,
    CleaningSummary,
    ConsumableStatus,
    DNDStatus,
    Timer,
    VacuumStatus,
)
from .viomivacuum import ViomiVacuum
from .waterpurifier import WaterPurifier
from .waterpurifier_yunmi import WaterPurifierYunmi
from .wifirepeater import WifiRepeater
from .wifispeaker import WifiSpeaker
from .yeelight import Yeelight
from .yeelight_dual_switch import YeelightDualControlModule

from .discovery import Discovery

__version__ = version("python-miio")
