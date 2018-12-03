import random


def get_random_hex_string(len):
    return ''.join([random.choice('0123456789abcdef') for _ in range(len)])


def get_random_unicode_string(len):
    result = u""
    for i in xrange(len):
        a = u"\\u%04x" % random.randrange(0x10000)
        result = result + a.decode('unicode-escape')
    return result


def get_random_filename():
    filename = get_random_unicode_string(random.randint(1, 30))
    extensions = ['.exe', '.avi', '.docx', '.xls', '.dmg', '.mp3', '.sh', '.txt', '.info']
    return filename + random.choice(extensions)
