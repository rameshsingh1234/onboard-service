# test_data.py
from src.unittest.python.utils import read_config_file

""" Read application config file"""
conf = read_config_file.read_config('/home/krishna/Tibil/sahamati/onboard-service/src/main/python/resources'
                                    '/application.json')
fiu_valid_schema = [
    (
        f"{conf.get('url')}",
        "sahamati-admin",
        "VKWZNwLdnfC6Izh2vdt0UgIlEkPzRynl",
        "sahamati-ops",
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
                "oldEntityId": "testEntity",
                "entityhandle": "fiu",
                "baseurl": "https://ode.finarkein.com/aa/fiu",
                "certificate": {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "5ebd671b-762c-49b0-99ce-65642b113d7b",
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
