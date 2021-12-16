FILENAME = './puzzle16/data/test8'

hex_dict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

inv_hex_dict = {v: k for k, v in hex_dict.items()}


with open(FILENAME) as file:
    for line in file:
        complete_message = line.strip()

bits = ''
for ch in complete_message:
    bits += hex_dict[ch]


def read_packet(i, total_versions):
    packet_version = int(inv_hex_dict['0' + bits[i:i+3]])
    total_versions += packet_version
    i += 3
    packet_type = int(inv_hex_dict['0' + bits[i:i+3]])
    i += 3
    if packet_type == 4:
        content = ''
        while True:
            content += bits[i + 1: i + 5]
            i += 5
            if bits[i - 5] == '0':
                break
        return [packet_version, packet_type, int(content, 2)], i, total_versions
    else:
        packet_length_type = int(bits[i:i+1])
        i += 1
        if packet_length_type == 0:
            packet_length = int(bits[i:i+15], 2)
            i += 15
            content = []
            inside = bits[i: i + packet_length]
            j = i
            while j < i + packet_length:
                internal, j, total_versions = read_packet(j, total_versions)
                content.append(internal)
            i += packet_length
            return [packet_version, packet_type, content], i, total_versions
        elif packet_length_type == 1:
            packet_length = int(bits[i:i+11], 2)
            i += 11
            content = []
            for _ in range(packet_length):
                inside, i, total_versions = read_packet(i, total_versions)
                content.append(inside)
            return [packet_version, packet_type, content], i, total_versions

packets, i, total_versions = read_packet(0, 0)

print(packets)
print(total_versions)
