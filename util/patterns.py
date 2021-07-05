import re


class Patterns:
    @staticmethod
    def match(pattern: str, string: str, tag: str = "Patterns.match"):
        matcher = re.match(pattern, string)
        if matcher is None or matcher.span()[1] < len(string) - 1:
            raise PatternError(f"{tag}: {string} does not match {pattern}")


class PatternError(Exception):
    pass
