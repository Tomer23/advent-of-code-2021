import math

FILENAME = './puzzle16/data/input'

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


def read_packet(i):
    packet_version = int(inv_hex_dict['0' + bits[i:i+3]])
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
        return [packet_version, packet_type, int(content, 2)], i
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
                internal, j = read_packet(j)
                content.append(internal)
            i += packet_length
            return [packet_version, packet_type, content], i
        elif packet_length_type == 1:
            packet_length = int(bits[i:i+11], 2)
            i += 11
            content = []
            for _ in range(packet_length):
                inside, i = read_packet(i)
                content.append(inside)
            return [packet_version, packet_type, content], i

packets, i = read_packet(0)

def evaluate_packet(packet):
    if packet[1] == 4:
        return packet[2]
    elif packet[1] == 0:
        return sum([evaluate_packet(x) for x in packet[2]])
    elif packet[1] == 1:
        return math.prod([evaluate_packet(x) for x in packet[2]])
    elif packet[1] == 2:
        return min([evaluate_packet(x) for x in packet[2]])
    elif packet[1] == 3:
        return max([evaluate_packet(x) for x in packet[2]])
    elif packet[1] == 5:
        if evaluate_packet(packet[2][0]) > evaluate_packet(packet[2][1]):
            return 1
        return 0
    elif packet[1] == 6:
        if evaluate_packet(packet[2][0]) < evaluate_packet(packet[2][1]):
            return 1
        return 0
    elif packet[1] == 7:
        if evaluate_packet(packet[2][0]) == evaluate_packet(packet[2][1]):
            return 1
        return 0
        
print(evaluate_packet(packets))
