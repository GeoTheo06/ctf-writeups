from binascii import unhexlify
from itertools import cycle

known_plaintext = b"Robert, are you able to read this message?"
known_ciphertext = unhexlify("057d1f2546c5929fcf860399be1d1ae6f65d4296680d8d220d7255541f8677e035bc12ae06a6b8c6d127")
target_ciphertext = unhexlify("11513a3b75e3fbe0f7bb33e694273d83c87161ac0737a75d3c567a6f6db75ecd19c8378226eaa4")
keystream = bytes([c ^ p for c, p in zip(known_ciphertext, known_plaintext)])
decrypted = bytes([c ^ k for c, k in zip(target_ciphertext, cycle(keystream))])
print("Decrypted message:", decrypted.decode())
