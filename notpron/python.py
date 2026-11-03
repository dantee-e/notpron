# 1:                                https://notpron.com/notpron/levelone.htm
# 2:                                https://notpron.com/notpron/not/level2.htm
# 3:                                https://notpron.com/notpron/false/movetotheothersite.php
# 4:  voodoo magic                  https://notpron.com/notpron/true/movetotheothersite.php
# 5:  simple songs                  https://notpron.com/notpron/google/shestheoneforme.php
# 6:  kill zone                     https://notpron.com/notpron/nothing/hesgotitall.php
# 7:  rediar                        https://notpron.com/notpron/sdrawkcab/tieman.htm
# 8:  inverted tenthlevel           https://notpron.com/notpron/sdrawkcab/rediar.htm
# 9:  turnmeon deadman              https://notpron.com/notpron/luv2music/paulisdead.htm
# 10: dark times                    https://notpron.com/notpron/wrong/roawr.htm
# 11: fucking pans                  https://notpron.com/notpron/reality/mystery.htm
# 12: remote control                https://notpron.com/notpron/blame/crossview.htm
# 13: devil hell                    https://notpron.com/notpron/ps/afterdeath.htm
# 14: deja vu                       https://notpron.com/notpron/neo/beenthere.htm
# 15: random access                 https://notpron.com/notpron/rusty/board.htm
# 16: doom murder


levels = [
    {
        "url1": None,
        "url2": "levelone",
        "password": None,
        "user": None,
    },
    {"url1": "not", "url2": "level2", "password": None, "user": None},
    {
        "url1": "false",
        "url2": "movetotheothersite",
        "password": None,
        "user": None,
    },
    {
        "url1": "true",
        "url2": "movetotheothersite",
        "password": "magic",
        "user": "voodoo",
    },
    {
        "url1": "google",
        "url2": "shestheoneforme",
        "password": "songs",
        "user": "simple",
    },
    {
        "url1": "nothing",
        "url2": "hesgotitall",
        "password": "zone",
        "user": "kill",
    },
    {
        "url1": "sdrawkcab",
        "url2": "tieman",
        "password": None,
        "user": None,
    },
    {
        "url1": "sdrawkcab",
        "url2": "rediar",
        "password": "tenthlevel",
        "user": "inverted",
    },
    {
        "url1": "luv2music",
        "url2": "paulisdead",
        "password": "deadman",
        "user": "turnmeon",
    },
    {
        "url1": "wrong",
        "url2": "roawr",
        "password": "times",
        "user": "dark",
    },
    {
        "url1": "reality",
        "url2": "mystery",
        "password": "pans",
        "user": "fucking",
    },
    {
        "url1": "blame",
        "url2": "crossview",
        "password": "control",
        "user": "remote",
    },
    {
        "url1": "ps",
        "url2": "afterdeath",
        "password": "hell",
        "user": "devil",
    },
    {
        "url1": "neo",
        "url2": "beenthere",
        "password": "vu",
        "user": "deja",
    },
    {
        "url1": "rusty",
        "url2": "board",
        "password": "access",
        "user": "random",
    },
    {
        "url1": "zoo",
        "url2": "mznvh",
        "password": "access",
        "user": "random",
    },
]


def level16():
    sequence = [
        False,
        False,
        False,
        (False, 4),
        (True, 5),
        (True, 3),
        False,
        (True, 2),
        (False, 5),
        False,
        (True, 1),
        (False, 1),
        (False, 1),
        (False, 2),
        (False, 1),
    ]

    class Solution:
        def solve(self, text):
            N = ord("z") + ord("a")
            return "".join([chr(N - ord(s)) for s in text])

    ob = Solution()

    result = ""

    for index, obj in enumerate(sequence):
        level = levels[index]

        if not obj:
            continue

        user = level["user"]

        if not obj[0]:
            result += user[obj[1] - 1]
        else:
            result += ob.solve(user)[obj[1] - 1]

    print(result)


import requests


def level18():
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i)
        request = requests.get(
            f"https://notpron.com/notpron/finale/screen19{i}.jpg",
            auth=("doom", "murder"),
        )
        print(request.status_code)
        if request.status_code == 200:
            print(f"success {i}")


level18()
