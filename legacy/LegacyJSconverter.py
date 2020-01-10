import requests
import re

SOURCES = ['https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt']

UNSUPPORTED_PALEMOON = ['(nano-set', '||', ':has', '@@', ':xpath']

OUTPUT = 'xyzzyx.txt'
OUTPUT_PALEMOON = 'legacyJS.notlist'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_palemoon(line) -> bool:
    for token in UNSUPPORTED_PALEMOON:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_palemoon(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"\(aeld,", 
           r"(addEventListener-defuser.js,", 
           line
        )

        line = re.sub(
           r"\(nowebrtc\)", 
           r"(nowebrtc.js)", 
           line
        )

        line = re.sub(
           r"\(aopr,", 
           r"(abort-on-property-read.js,", 
           line
        )

        line = re.sub(
           r"\(aopw,", 
           r"(abort-on-property-write.js,", 
           line
        )

        line = re.sub(
           r"\(window.open-defuser\)", 
           r"(window.open-defuser.js)", 
           line
        )

        line = re.sub(
           r"\(std,", 
           r"(setTimeout-defuser.js,", 
           line
        )

        line = re.sub(
           r"\(nobab\)", 
           r"(bab-defuser.js)", 
           line
        )

        line = re.sub(
           r"\(acis,", 
           r"(abort-current-inline-script.js,", 
           line
        )

        line = re.sub(
           r"\(noeval\)", 
           r"(noeval.js)", 
           line
        )

        line = re.sub(
           r"\(set-constant,", 
           r"(set-constant.js,", 
           line
        )

        line = re.sub(
           r".*#[@]?#[a-z0-9.#[].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[/*.|:#-].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^! [a-zA-SU-Z0-9-].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^! To counter", 
           r"", 
           line
        )

        if is_supported_palemoon(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    palemoon_filter = prepare_palemoon(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_PALEMOON, "w") as text_file:
        text_file.write(palemoon_filter)

    print('The  versions have been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['NonAuto.notlist', 'legacyJS.notlist']

OUTPUT = 'xyzzyx2.txt'
OUTPUT_PALEMOON = 'legacy.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for file in SOURCES:
        r = requests.get(file)
        text += r.text
    return text

# function that prepares the filter list for AdGuard Home
def prepare_palemoon(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        if not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    palemoon_filter = prepare_palemoon(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_PALEMOON, "w") as text_file:
        text_file.write(palemoon_filter)

    print('The  versions have been generated.')