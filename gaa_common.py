
import gaa_constants 

def check_dl_type(dl_type):
    if not(dl_type in gaa_constants.gaa_dl_services):
        raise ValueError("invalid dl_type")
