def detect_marker_position(datastream: str) -> int:
    marker = []

    for i, char in enumerate(datastream):
        if char in marker:
            marker = []

        marker.append(char)

        if len(marker) == 4:
            return i + 1


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.read()

    file.close()

    return file_content


if __name__ == "__main__":
    input_string = read_sample_file("tuning_trouble_input.txt")

    marker_position = detect_marker_position(input_string)

    print(marker_position)
