"""Disassemble and dump a python code object
"""

from types import CodeType
import binascii, struct, time, marshal, dis
import sys

FIELD_SIZE = 4  # 32 // 8


def dump(code_obj):
    frames = []

    def ddump(code_obj):
        for const in code_obj.co_consts:
            if isinstance(const, CodeType):
                ddump(const)
        frames.append((code_obj.co_filename, code_obj.co_firstlineno, code_obj))

    ddump(code_obj)
    frames.sort(key=lambda tpl: tpl[1])
    return frames


def main(fname):
    with open(fname, "rb") as infile:
        magic_number = binascii.hexlify(infile.read(FIELD_SIZE))
        bit_field = infile.read(FIELD_SIZE)
        moddate = infile.read(FIELD_SIZE)
        source_size = infile.read(FIELD_SIZE)

        modtime = time.asctime(time.localtime(struct.unpack("=L", moddate)[0]))
        source_size = struct.unpack("=L", source_size)

        print(f"File name: {fname}")
        print(f"Magic number: {magic_number}")
        print(f"Bit field{bit_field}")
        print(f"Modification time: {modtime}")
        print(f"Source size: {source_size}")
        print("\n")
        # An instance of https://docs.python.org/3/c-api/code.html#c.PyCodeObject
        code_obj = marshal.load(infile)
        frames = dump(code_obj)

        for tpl in frames:
            dis.disassemble(tpl[2])


if __name__ == "__main__":
    main(sys.argv[1])
