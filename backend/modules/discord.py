import requests

def discord_email(email):

    cookies = {
        '__cfruid': '75dd35fcb721545ff0a6798a2833c04ec257fd5a-1679183851',
        '__dcfduid': 'a585f1c2c5e811edb2f6a25738b7802e',
        '__sdcfduid': 'a585f1c2c5e811edb2f6a25738b7802e9ba98e53c2319d50476386ec96c3a06087eb06f1ccf8dec3627a51ff901681ca',
    }

    headers = {
        'authority': 'discord.com',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/register',
        'sec-ch-ua-platform': '"macOS"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        # 'Cookie': '__cfruid=75dd35fcb721545ff0a6798a2833c04ec257fd5a-1679183851; __dcfduid=a585f1c2c5e811edb2f6a25738b7802e; __sdcfduid=a585f1c2c5e811edb2f6a25738b7802e9ba98e53c2319d50476386ec96c3a06087eb06f1ccf8dec3627a51ff901681ca',
    }

    json_data = {
        'fingerprint': '1086786637167599686.7j66Qwbpt2J6Y-YZdDQPVn0Zp3g',
        'email': email,
        'username': 'asdfasdfasdf',
        'password': 'OSINTisAwesome2023!',
        'invite': None,
        'consent': True,
        'date_of_birth': '1983-07-01',
        'gift_code_sku_id': None,
        'captcha_key': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQa0y_zAHbxiFaEF4IjldPsteAFDkWnOS4KSRqu0YdNPzqEWYDdbfLWfhDtm5Mqcc9UUbS5wiCeCg__iHsu2DnzsIKfXh6guxGX6rIVfKzDK59yFH9RH2ogsLQ5RRLtgPfP0Uzc_IOGFP660d_MxUsVzEgiDeP7E6LmdA-8EnmYS5v3WkTfddOjkefkKQTUOkuJggTKiiQpZjjXVh2kgZppIP_MnerUTdWMS-uBsgNJt0H2p_-Q0aSDH3UT5WEMhXElbIWrileJOBxavfbgWPDPcM-mEuzFDwqptfrF_MMcotT3Tkz1rVcvK9Lo1eeIX9gyk9v3rTsSik6Fcox8NeET_w60GT33lF-TpEMNAUrDIF52uRPGxL1fmhsLhxlas49vsZ18laBOdxqczq44j6PNRuLzAMuSrswdkOUfV5lbpej9F4VMkL7JQVKvHGpJCT1c3Dlvtiq5gRRXnF52VACdqNO91cdkZcUdxx2AVJsSE_jaG48Nxy2xiyYFocpEuAvQPNRDA7bLKm90a-Lf1wCmYRhQeKn0xa--QH7AoEnaE9P5D3y4zvOEW2LWVlEEiNsjIQHHAVMZgv-ggLsxmzbwAAdsiTgCyLSYAKRqFsHW8eTKOkS_74xBg6w9Z7ztDhCpFtaIhhfM7bMH7JvHizbWIZ59Q7ixup7ASYorhe_cuLDUzMpzXivAiW-fB92-34tko2FZKwNPy-VrUcojjae3lR_YIEEJ9dryOoSSabCnn_NlqA7Zq0mXNQ1TVzAzpM79d9Nqnqoyf31RKa2Ih_Hu4qT3jmlP9EENnjZfgaVkBpozvn-k9lxE5OKC97Nc_DrbjnDnIKj0GKsxevUvJD5ClD37KMWHVgrB_Nt9gI4lwSWBIi7T04PDeZPXGxv04q2wf14kvGo2LwEo7fF5J6QTZpuOd-U5NFiIQ88NQNMJ_cKT8ITIeEq3EWv0-OMoyPZXpV2HWlBy9KHKWGAYtw-qiyIRc1xPwyHRVMASzNRNSbFX5D2Dz-_gT8m6gWDuT2Gq0XQdWdTirzpu89d_xlIoiqFf5d1NS9RE_PXI-krMY1l1FZ-nyxjkGlUw293IHN53uyAcVSYRjkCkR4k6VFuR20klt4_H96uuk5-u08miFf2B7wZt8ltR4YeAiobhWPtDTH-NAP5AHEW77XxJvlkUZ8h9Rb79Z6X-I74I7qBW73eICf8SBEWxKdCfnGUauJMhh8vBrWh-Tw3doqnEr3lLcdUxwNAvbn1dvQgzEkUniswuyVfw2EqlrDXhB87cyxr8XOwqampxgVcB3QlOOznY210CTr3a0BY4GCHd6t5XdTG6p2XPfBU34-rkJUsdDAaTaFgnzqbu-8ZPLDyN7YolUmRe7VnQoxhsSZ_GOgJaJ1lOxSirVFRqYibKUr_oJ20S4Zk_cqN_kZHlwXIa8ML0lnDHlZeLe6jrh9E3wR_pZYXfMKDM4PuiSQ2BWeFqTl4gEbg6ykJUvJUCqJSoW5lqNh1yS02cx-3XXO35qqF2DQ_4N_mN5phecXQK9RPf_PXEgYGbuf4S91wa1ft_AqTzcaHXycI0yeagqHVeNEwiPGKSIyF0qOQrbFTiFr4ABQ0NmxnzQhxE-Oh3LR26QubQLqultAiGlwQ10Bvt-uAu0oElL4WXlEl16Emu1RzuPbE9MLMgtH7W2q1P9-Xaenkc-LEHso1PUtkxZ5vds9GIvYnIRN3uchagaGflV3rmLRsXLPgwzV0ixT-Wzl62mh0-qUPdtId5I99Vu5iG5OQPZdeF4ADoDs-Bkq405_ZsvCLHoosZSKNMF4Crdgn4mAUy5AyaHyFJVMutBEr7D8p3-NRV3LowvIjEZZCvS7qmCIB_NEyHo3Sg6eHlIpJOyGIgr4Me9HGT-tphEucfRA8Sg5y-QKOVzJR78rtWKAB13Cc4m6VPCU5QeBORTAwtTmAmTCgb6WNxbW1Quk0GclSQGmoTT9H9n_lWtGVDhsxnsps4ICp2NLC9oi0wPjkNLPn7Rs-TxHb3JQ7WCU2ak5rSeHXNACW3oQn6Bp0To0pQKLsre0fXNqSliZZ9DjseIvxyu1Jn2mxr6kuOAsznaU6zRAh3Anz9JGvsOKCl9VhevdzjCIAvDz1Ne5_uWAyrmR5QMp4BI6Mup2qCCWPjz9JfkVci_XGb_t6QRBfsOcgu92ma4QiXInJ2TZ4gpCL0FpGcKPJNc4_RadbCrRvjYJHPJl6-SMiG3OcXi3cC0fiD21ZSCNWcZKarAAQHde3UFFbol2PIGKFIkmoF8Q4fnlJdTsr8PXUcxo2V4cM5kFkRHqHNoYXJkX2lkzg07ZCmicGQA.OGCKBD244sF0A-fK6dS44xSzBQFDAoUWrxb62cJ6hJs',
    }

    response = requests.post('https://discord.com/api/v9/auth/register', cookies=cookies, headers=headers, json=json_data)

    html = response.text

    taken = 'Email is already registered.'

    if taken in html:
        return f'true'
    else:
        return f'false'
