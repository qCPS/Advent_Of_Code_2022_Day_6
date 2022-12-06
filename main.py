signal_file = open("signal.txt", "r")

signal = signal_file.readline()


# Part 1


def find_packet_marker(string):

    # Create a local variable "chars" to store the number of characters before a message marker is found
    chars = 0

    # Create an empty list called "package_marker" to store the characters of a package marker
    package_marker = []

    # Find the marker
    for char in string:
        if char not in package_marker:
            package_marker.append(char)
            chars += 1

        else:
            while char in package_marker:
                package_marker.pop(0)

            package_marker.append(char)

            chars += 1

        if len(package_marker) == 4:
            return chars


# Part 2


def find_message_marker(string):

    # Create a local variable "chars" to store the number of characters before a message marker is found
    chars = 0

    # Create an empty list to store the characters of a message marker
    message_marker = []

    # Find the marker
    for char in string:
        if char not in message_marker:
            message_marker.append(char)
            chars += 1

        else:
            while char in message_marker:
                message_marker.pop(0)

            message_marker.append(char)

            chars += 1

        if len(message_marker) == 14:
            return chars


print(find_packet_marker(signal))

print(find_message_marker(signal))
