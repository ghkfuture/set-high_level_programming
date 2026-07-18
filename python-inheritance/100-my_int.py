#!/usr/bin/python3
"""Defines a inverted logic MyInt data tracking module."""


class MyInt(int):
    """Rebels against standard equality integer operators explicitly."""

    def __eq__(self, value):
        """Inverts traditional match responses."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts traditional mismatch responses."""
        return super().__eq__(value)
