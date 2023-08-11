import os

from src.unittest.python.utils import read_config_file

""" Read config file"""
conf = read_config_file.read_config(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "testHeaders.json"))


fip_valid_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIP",
        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "FIPtest",
                "id": "FIPtestEntity"
            },
            "entityinfo": {
                "name": "FIPtest",
                "id": "FIPtestEntity",
                "code": "FINVU",
                "entityhandle": "@finvu",
                "Identifiers": [
                    {
                        "category": "STRONG",
                        "type": "MOBILE"
                    }
                ],
                "baseurl": "https://aauat.finvu.in/API/V1",
                "fitypes": [
                    "DEPOSIT",
                    "RECURRING_DEPOSIT",
                    "TERM-DEPOSIT"
                ],
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099p1",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "inboundports": [
                    "8080"
                ],
                "outboundports": [
                    "9595"
                ],
                "ips": [
                    "103.224.243.153",
                    "103.224.243.227"
                ],
                "credentialsPk": {
                    "alg": "aS256",
                    "e": "VAQAB",
                    "kid": "4580a1ca9-7e0e-45cc-b585-50d1d0203099",
                    "kty": "AAR",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "abg"
                }
            }
        },
        201
    )
]

fip_create_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIP",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "FIP1test",
                "id": "FIP1testEntity"
            },
            "entityinfo": {
                "name": "FIP1test",
                "id": "FIP1testEntity",
                "code": "FINVU",
                "entityhandle": "@finvu",
                "Identifiers": [
                    {
                        "category": "STRONG",
                        "type": "MOBILE"
                    }
                ],
                "baseurl": "https://aauat.finvu.in/API/V1",
                "fitypes": [
                    "DEPOSIT",
                    "RECURRING_DEPOSIT",
                    "TERM-DEPOSIT"
                ],
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099p2",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "inboundports": [
                    "8080"
                ],
                "outboundports": [
                    "9595"
                ],
                "ips": [
                    "103.224.243.153",
                    "103.224.243.227"
                ],
                "credentialsPk": {
                    "alg": "aS256",
                    "e": "VAQAB",
                    "kid": "4580a1ca9-7e0e-45cc-b585-50d1d0203099",
                    "kty": "AAR",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "abg"
                }
            }
        },
        201
    )
]

fip_invalid_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIP",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",

            "entityinfo": {
                "name": "FIP4test",
                "id": "FIP4testEntity",
                "code": "FINVU",
                "entityhandle": "@finvu",
                "Identifiers": [
                    {
                        "category": "STRONG",
                        "type": "MOBILE"
                    }
                ],
                "baseurl": "https://aauat.finvu.in/API/V1",
                "fitypes": [
                    "DEPOSIT",
                    "RECURRING_DEPOSIT",
                    "TERM-DEPOSIT"
                ],
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099p4",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "inboundports": [
                    "8080"
                ],
                "outboundports": [
                    "9595"
                ],
                "ips": [
                    "103.224.243.153",
                    "103.224.243.227"
                ],
                "credentialsPk": {
                    "alg": "aS256",
                    "e": "VAQAB",
                    "kid": "4580a1ca9-7e0e-45cc-b585-50d1d0203099",
                    "kty": "AAR",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "abg"
                }
            }
        },
        400
    )
]

fip_exist_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIP",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "FIP2test",
                "id": "FIP2testEntity"
            },
            "entityinfo": {
                "name": "FIP2test",
                "id": "FIP2testEntity",
                "code": "FINVU",
                "entityhandle": "@finvu",
                "Identifiers": [
                    {
                        "category": "STRONG",
                        "type": "MOBILE"
                    }
                ],
                "baseurl": "https://aauat.finvu.in/API/V1",
                "fitypes": [
                    "DEPOSIT",
                    "RECURRING_DEPOSIT",
                    "TERM-DEPOSIT"
                ],
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099pp2",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "inboundports": [
                    "8080"
                ],
                "outboundports": [
                    "9595"
                ],
                "ips": [
                    "103.224.243.153",
                    "103.224.243.227"
                ],
                "credentialsPk": {
                    "alg": "aS256",
                    "e": "VAQAB",
                    "kid": "4580a1ca9-7e0e-45cc-b585-50d1d0203099",
                    "kty": "AAR",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "abg"
                }
            }
        },
        409
    )
]

fip_request_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIP",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "FIP3test",
                "id": "FIP3testEntity"
            },
            "entityinfo": {
                "name": "FIP3test",
                "id": "FIP3testEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "Identifiers": [
                    {
                        "category": "STRONG",
                        "type": "MOBILE"
                    }
                ],
                "baseurl": "https://aauat.finvu.in/API/V1",
                "fitypes": [
                    "DEPOSIT",
                    "RECURRING_DEPOSIT",
                    "TERM-DEPOSIT"
                ],
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099p3",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "inboundports": [
                    "8080"
                ],
                "outboundports": [
                    "9595"
                ],
                "ips": [
                    "103.224.243.153",
                    "103.224.243.227"
                ],
                "credentialsPk": {
                    "alg": "aS256",
                    "e": "VAQAB",
                    "kid": "4580a1ca9-7e0e-45cc-b585-50d1d0203099",
                    "kty": "AAR",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "abg"
                }
            }
        },
        201
    )
]
