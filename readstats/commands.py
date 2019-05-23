import argparse
import sys
def parse_commands():
    """Create parser object which map the commands
    return: the parser variable which contains the ArgumentParser object"""
    parser = argparse.ArgumentParser(prog="readstats", usage="readstats [USERNAME] ...[<args>]")
    parser.add_argument("user", help="Look if a name given exists on Goodreads")
    parser.add_argument("-A", "--all", action="store_true", help="Display all the stats of the given user")
    parser.add_argument("-a", "--authors", action="store_true", help="Display the favorite authors and how many books by them")
    #action='store_true' to execute the flag witouh any argument, so it will return True
    parser.add_argument("-g", "--genres", action="store_true",help="Display favorite genres. According to what the user is actually read and not what he shelved as favorite")
    parser.add_argument("-T", "--more-time", action="store_true", help="Display books which took more time to finish considering book lenght and time")
    parser.add_argument("-t", "--less-time", action="store_true", help="Display books which took less time to finish considering book lenght and time")
    parser.add_argument("-br", "--liked-review", action="store_true", help="Display the most liked review the user has written and for which book")
    parser.add_argument("-sr", "--shortest-review", action="store_true", help="Display the shortest review the user has written and the name of the book")
    parser.add_argument("-lr", "--longest-review", action="store_true", help="Display the longest review the user has written and for which book")
    return parser