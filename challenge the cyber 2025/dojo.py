import base64

def b64_to_int(b64_str):
    # Add padding if necessary.
    padded = b64_str + '=' * ((4 - len(b64_str) % 4) % 4)
    # URL-safe Base64 decode the padded string.
    byte_data = base64.urlsafe_b64decode(padded)
    # Convert from bytes to an integer.
    return int.from_bytes(byte_data, "big")

# Provided encoded values:
e_encoded = "AQAB"
n_encoded = (
    "4KW63Ggyz82E7MXqO3o97U3RP4_qG-RCRasdP0oG6xUqxGSTv0A1EtHtoThjzwK3E2jJMJYp1Kx_"
    "W71Uo_KIMxOB6nEzgcePQw7YCAGgxhA8zujXwt-wLAirpezFcspb-SoFdUuO4WLfJHsArPaOkZQPl"
    "Mf4ws3U8Mz34OmdC1VyQLCGjzCaO1gJwSNRpnSf9VEHqmLs4ZK_smJq6v0Wn0KtlGGyczytYEU9v_"
    "sCEsTwzRiFPWZUXq4DHjToT8N3IB-3-rdqfxOzKBUO5ZGzlMUqPse2jYENWnWUH5A5V11bUz1tToB"
    "VdLPv-vpEmQ2SP3BgBhToePPnWfkIVMyCXw"
)

# Decode the values:
e_int = b64_to_int(e_encoded)
n_int = b64_to_int(n_encoded)

print("Decoded e (exponent):", e_int)
print("Decoded n (modulus):", n_int)
