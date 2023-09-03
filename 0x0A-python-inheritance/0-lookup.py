#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns list of objects in the atrributes"""
    return (dir(obj))
