
data_hex = "0503060506030705070206050409050606090703050306050603070507020600db8c5c6facdf68b15b14b29823bc8114"


data_bytes = bytes.fromhex(data_hex)


device_id = int.from_bytes(data_bytes[:2], byteorder='big')


parameters = [int.from_bytes(data_bytes[i:i+2], byteorder='big') for i in range(2, 30, 2)]


signature = data_bytes[-16:]


print(f"Device ID or Message Type: {device_id}")
print("Device Status / Configuration Parameters:")

for i, param in enumerate(parameters):
    print(f"  Parameter {i+1}: {param}")

print(f"Signature/Checksum: {signature.hex()}")