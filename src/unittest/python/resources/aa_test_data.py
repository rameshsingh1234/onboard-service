from src.unittest.python.utils import read_config_file

""" Read application config file"""
conf = read_config_file.read_config('/home/amith/Desktop/Onboard-Service-Vishwaas/onboard-service-AUG09/onboard'
                                    '-service/src/main/python/resources/application.json')

aa_valid_schema = [
    (
        f"{conf.get('AAurl')}",
        "sahamati-admin",
        "Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN",
        "sahamati-ops",
        "AA",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "AAtest",
                "id": "AAtestEntity"
            },
            "entityinfo": {
                "name": "AAtest",
                "id": "AAtestEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "baseurl": "https://aauat.finvu.in/API/V1",
                "webviewurl": "https://webvwdev.finvu.in/onboarding",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099",
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

aa_create_schema = [
    (
        f"{conf.get('AAurl')}",
        "sahamati-admin",
        "Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN",
        "sahamati-ops",
        "AA",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "AA1test",
                "id": "AA1testEntity"
            },
            "entityinfo": {
                "name": "AA1test",
                "id": "AA1testEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "baseurl": "https://aauat.finvu.in/API/V1",
                "webviewurl": "https://webvwdev.finvu.in/onboarding",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099a1",
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


aa_invalid_schema = [
    (
        f"{conf.get('AAurl')}",
        "sahamati-admin",
        "Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN",
        "sahamati-ops",
        "AA",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",

            "entityinfo": {
                "name": "AAtest",
                "id": "AAtestEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "baseurl": "https://aauat.finvu.in/API/V1",
                "webviewurl": "https://webvwdev.finvu.in/onboarding",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099a5",
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

aa_exits_schema = [
    (
        f"{conf.get('AAurl')}",
        "sahamati-admin",
        "Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN",
        "sahamati-ops",
        "AA",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "AA2test",
                "id": "AA2testEntity"
            },
            "entityinfo": {
                "name": "AA2test",
                "id": "AA2testEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "baseurl": "https://aauat.finvu.in/API/V1",
                "webviewurl": "https://webvwdev.finvu.in/onboarding",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099a2",
                    "kty": "RSA",
                    "n": "abcU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
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

aa_request_schema = [
    (
        f"{conf.get('AAurl')}",
        "sahamati-admin",
        "Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN",
        "sahamati-ops",
        "AA",

        {
            "ver": "1.0",
            "timestamp": "2021-07-30 14:21:19.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "AA3test",
                "id": "AA3testEntity"
            },
            "entityinfo": {
                "name": "AA3test",
                "id": "AA3testEntity",
                "code": "AAFINVU",
                "entityhandle": "@finvu",
                "baseurl": "https://aauat.finvu.in/API/V1",
                "webviewurl": "https://webvwdev.finvu.in/onboarding",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "380a1ca9-7e0e-45cc-b585-50d1d0203099a3",
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
