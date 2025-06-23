from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def setear_volumen(porcentaje):
    """Setea el volumen del sistema entre 0 y 100%"""
    # Normalizar a valor entre 0.0 y 1.0
    valor = max(0.0, min(porcentaje / 100, 1.0))

    devices = AudioUtilities.GetSpeakers()
    interfaz = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volumen = cast(interfaz, POINTER(IAudioEndpointVolume))
    
    volumen.SetMasterVolumeLevelScalar(valor, None)