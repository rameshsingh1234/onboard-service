import os

from src.unittest.python.utils import read_config_file

conf = read_config_file.read_config(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "testHeaders.json"))

fiu_valid_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIU",

        {
            "ver": "1.0",
            "timestamp": "2021-03-30 18:41:54.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu@finarkein"
            },
            "entityinfo": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu@finarkein",
                "code": "fiu@finarkein",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7a11",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK"
                         "-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "tokeninfo": {
                    "url": "https://www.finvu.in/fip/tokens",
                    "maxcalls": 100,
                    "desc": "string"
                },
                "signature": {
                    "signValue": "eyJraWQiOiJrZXlJZDEiLCJhbGciOiJSUzI1NiJ9"
                },
                "inboundports": [
                    "port"
                ],
                "outboundports": [
                    "port"
                ],
                "ips": [
                    "ips"
                ]
            }
        },
        201
    )

]

fiu_entity_api_request_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIU",

        {
            "ver": "1.0",
            "timestamp": "2021-03-30 18:41:54.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu1@finarkein"
            },
            "entityinfo": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu1@finarkein",
                "code": "fiu1@finarkein",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7ab1",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "tokeninfo": {
                    "url": "https://www.finvu.in/fip/tokens",
                    "maxcalls": 100,
                    "desc": "string"
                },
                "signature": {
                    "signValue": "eyJraWQiOiJrZXlJZDEiLCJhbGciOiJSUzI1NiJ9"
                },
                "inboundports": [
                    "port"
                ],
                "outboundports": [
                    "port"
                ],
                "ips": [
                    "ips"
                ]
            }
        },
        201
    )

]

fiu_create_entity = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIU",

        {
            "ver": "1.0",
            "timestamp": "2021-03-30 18:41:54.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu2@finarkein"
            },
            "entityinfo": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu2@finarkein",
                "code": "fiu2@finarkein",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7ab2",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "tokeninfo": {
                    "url": "https://www.finvu.in/fip/tokens",
                    "maxcalls": 100,
                    "desc": "string"
                },
                "signature": {
                    "signValue": "eyJraWQiOiJrZXlJZDEiLCJhbGciOiJSUzI1NiJ9"
                },
                "inboundports": [
                    "port"
                ],
                "outboundports": [
                    "port"
                ],
                "ips": [
                    "ips"
                ]
            }
        },
        201
    )

]

fiu_invalid_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIU",

        {
            "ver": "1.0",
            "timestamp": "2021-03-30 18:41:54.0",
            "txnid": "29ae-11e8-a8d7-0290",

            "entityinfo": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu5@finarkein",
                "code": "fiu5@finarkein",
                "oldEntityId": "testEntity",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7a13",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "tokeninfo": {
                    "url": "https://www.finvu.in/fip/tokens",
                    "maxcalls": 100,
                    "desc": "string"
                },
                "signature": {
                    "signValue": "eyJraWQiOiJrZXlJZDEiLCJhbGciOiJSUzI1NiJ9"
                },
                "inboundports": [
                    "port"
                ],
                "outboundports": [
                    "port"
                ],
                "ips": [
                    "ips"
                ]
            }
        },
        400
    )

]

fiu_create_entity_exist_schema = [
    (
        f"{conf.get('url')}",
        f"{conf.get('client_id')}",
        f"{conf.get('client_secret')}",
        f"{conf.get('user_type')}",
        "FIU",

        {
            "ver": "1.0",
            "timestamp": "2021-03-30 18:41:54.0",
            "txnid": "29ae-11e8-a8d7-0290",
            "requester": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu3@finarkein"
            },
            "entityinfo": {
                "name": "Finarkein Analytics Pvt. Ltd.",
                "id": "fiu3@finarkein",
                "code": "fiu3@finarkein",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7ab3",
                    "kty": "RSA",
                    "n": "gU8PDUSzaHtMOYJd9NDLJ-2dAE1lXUCgZK-N6y9vRDCurscfQlTHKZliBbhiEsMCk70_nbDie6YKXWavJKj0X4nzoa1H7jrRjKa7R80BlqtSKl95TuynUChrHvvsvcjDSXp4d4PCNZ0Hdp7j0K-QSiR4OHGb3Irm9vgv3tPdh00ijPwqFJRFSkofFiUSRp-7BXWQXvnnH0sEIMvGjCxj4hAz3J35X5KPfRaax5MCQPr1-WkOgGYvpNPaDjSjsvhtOZQMcmvy_AaoRk6FADHkIRJU14dzw9alI4dp5Yp52CRg-bPDYReQe4e3j4I8DP3i0JTkV_fJOgDKPnFpRDmDNw",
                    "use": "sig"
                },
                "tokeninfo": {
                    "url": "https://www.finvu.in/fip/tokens",
                    "maxcalls": 100,
                    "desc": "string"
                },
                "signature": {
                    "signValue": "eyJraWQiOiJrZXlJZDEiLCJhbGciOiJSUzI1NiJ9"
                },
                "inboundports": [
                    "port"
                ],
                "outboundports": [
                    "port"
                ],
                "ips": [
                    "ips"
                ]
            }
        },
        409
    )

]

