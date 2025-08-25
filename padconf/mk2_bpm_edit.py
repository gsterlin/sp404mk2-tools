import argparse

def update_pad_bpm(file_path: str, pad: int, bpm: int):
    if pad < 0 or pad > 160:
        raise ValueError("pad value must be 1 to 160")

    byte_position = 198 + ((pad-1) * 172)

    change_bytes(file_path, byte_position, bpm)


#def change_bytes(file_path: str, byte_position: int, new_value: bytes):
def change_bytes(file_path: str, byte_position: int, new_value: int):
    #if len(new_value) != 2:
        #raise ValueError("New value must be exactly two bytes long")

    with open(file_path, 'rb+') as file:
        file.seek(byte_position)

        # Read and discard the current two bytes to ensure we're at the right position
        #_ = file.read(2)

        # Write new value
        file.write(new_value.to_bytes(2, 'big'))

#def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("file", help="Path to the file")
    #parser.add_argument("position", type=int, help="Byte position to edit")
    #parser.add_argument("new_value", type=int, help="New value (in integer, 90.00BPM is 9000)")

    #args = parser.parse_args()

    #change_bytes(args.file, args.position, args.new_value)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("pad", type=int, help="Pad to edit")
    parser.add_argument("bpm", type=int, help="New Pad BPM (in integer, 90.00BPM is 9000)")

    args = parser.parse_args()

    update_pad_bpm(args.file, args.pad, args.bpm)

if __name__ == "__main__":
    main()

