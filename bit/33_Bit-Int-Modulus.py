#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given a list of bytes a, each representing one byte of a larger integer (ie. {0x12, 0x34, 0x56, 0x78} represents the integer 0x12345678), and an integer b, find a % b.

mod({0x03, 0xED}, 10) = 5
'''


def mod(bits, num):
    res = 0
    for bit in bits:
        res = (res << 8) | (bit & 0xff)
        res %= num
    return res


if __name__ == '__main__':
    assert mod([0x03, 0xED], 10) == 5
