# generador-qr

## Dependències
En sistemes Debian:
```
sudo apt install python3 python3-qrcode python3-bs4 python3-requests
```

## Exemples
Amb la següent ordre generarem un QR per cada fitxer MP3 que hi ha al directori `8M`:
```
python3 genera-qr.py --url https://dat.upc.edu/8M --ext mp3
```
