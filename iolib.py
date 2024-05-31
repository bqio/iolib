from ctypes import (
    c_bool,
    c_byte,
    c_ubyte,
    c_short,
    c_ushort,
    c_int,
    c_uint,
    c_long,
    c_ulong,
)
from struct import pack
from contextlib import AbstractContextManager
from typing import Self

LITTLE_ENDIAN = 0
BIG_ENDIAN = 1
SEEK_BEGINNING = 0
SEEK_CURRENT = 1
SEEK_END = 2


class BinaryStreamWriter(AbstractContextManager):
    def __init__(self, output_path: str, endian: c_bool = LITTLE_ENDIAN) -> None:
        super().__init__()
        self.__output_path = output_path
        self.__fp = None
        self.__endian = "<" if endian == LITTLE_ENDIAN else ">"

    def write_byte(self, n: c_byte) -> int:
        """Write signed byte number into stream."""
        buf = pack("{}b".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_ubyte(self, n: c_ubyte) -> int:
        """Write unsigned byte number into stream."""
        buf = pack("{}B".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_short(self, n: c_short) -> int:
        """Write signed short number into stream."""
        buf = pack("{}h".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_ushort(self, n: c_ushort) -> int:
        """Write unsigned short number into stream."""
        buf = pack("{}H".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_int(self, n: c_int) -> int:
        """Write signed integer number into stream."""
        buf = pack("{}i".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_uint(self, n: c_uint) -> int:
        """Write unsigned integer number into stream."""
        buf = pack("{}I".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_long(self, n: c_long) -> int:
        """Write signed long number into stream."""
        buf = pack("{}l".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_ulong(self, n: c_ulong) -> int:
        """Write unsigned long number into stream."""
        buf = pack("{}L".format(self.__endian), n)
        return self.__fp.write(buf)

    def write_ascii_string(self, s: str) -> int:
        """Write ASCII string into stream."""
        return self.__fp.write(s.encode(encoding="ascii"))

    def write_ascii_nt_string(self, s: str) -> int:
        """Write ASCII nul terminated string into stream."""
        return self.__fp.write(s.encode(encoding="ascii") + bytes(1))

    def write_utf8_string(self, s: str) -> int:
        """Write UTF-8 string into stream."""
        return self.__fp.write(s.encode(encoding="utf-8"))

    def write_utf8_nt_string(self, s: str) -> int:
        """Write UTF-8 nul terminated string into stream."""
        return self.__fp.write(s.encode(encoding="utf-8") + bytes(1))

    def write(self, b: bytes) -> int:
        """Write bytes into stream."""
        return self.__fp.write(b)

    def open(self) -> Self:
        """Open binary file stream."""
        self.__fp = open(self.__output_path, "wb")
        return self

    def close(self) -> None:
        """Close binary file stream."""
        self.__fp.close()

    def seek(self, offset: int, whence: int = SEEK_BEGINNING) -> int:
        """Change the stream position."""
        return self.__fp.seek(offset, whence)

    def skip(self, count: int) -> int:
        """Skip bytes."""
        return self.__fp.seek(count, SEEK_CURRENT)

    def __enter__(self) -> Self:
        return self.open()

    def __exit__(self, *e) -> None:
        return self.close()
