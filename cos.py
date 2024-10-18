import math

def cosAlpha(vec_len):
    cosA = (16**2 + 16**2 - vec_len**2)/( 2 * 16**2)
    cosA = max(min(cosA, 1), -1)
    cosA_rad = math.acos(cosA)
    cosA_deg = math.degrees(cosA_rad)
    return cosA_deg