# FSH Bruno API Test

API-testprojekt mot "Frans API" (studenthantering) med [Bruno](https://www.usebruno.com/) och pytest, från FSH-kursen.

## Innehåll

Projektet kombinerar två sätt att testa samma API:

- **Bruno-collection** (`.bru`-filer) – manuella/exploratoriska API-anrop: skapa, hämta, uppdatera och ta bort studenter
- **Pytest** (`tests/`) – automatiserade API-tester med en egen API-klient (`frans_api_helper_class.py`)

## Köra Bruno-collectionen

1. Öppna [Bruno](https://www.usebruno.com/) och importera mappen som en collection (`bruno.json` finns i roten).
2. Kör requesten "First request to Frans API" för att verifiera anslutning, kör därefter övriga requests.

## Köra pytest-testerna

```bash
pip install pytest requests
pytest tests/
```

## Struktur

```
├── *.bru                          # Bruno-requests (skapa, hämta, uppdatera, ta bort student m.fl.)
├── bruno.json                     # Bruno-collectionens konfiguration
└── tests/
    ├── frans_api_helper_class.py  # API-klient för Frans API
    ├── test_frans_api_class.py
    ├── test_frans_api_2026.py
    └── test_make_request.py
```
