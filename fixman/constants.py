"""
Shell constants focus on exit codes, the purpose of which is to make shell exit codes more obvious. There are a few
different sources. We've chosen those codes referenced in the the Advanced Bash Scripting Guide (which in turn
references ``sysexist.h``) -- and added a few of our own.

See https://stackoverflow.com/a/1535733/241720

See http://www.tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF

"""
EXIT_OK = 0
EXIT_ERROR = 1
EXIT_INPUT = 2
EXIT_USAGE = 64
EXIT_ENVIRONMENT = 71
EXIT_IO = 74
EXIT_TEMP = 75
EXIT_PERMISSIONS = 77
EXIT_CONFIG = 78

EXIT_FAILURE = EXIT_ERROR
EXIT_SUCCESS = EXIT_OK
EXIT_UNKNOWN = 99

LOGGER_NAME = "fixman"
