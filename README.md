# zipcrk

Şifreli ZIP dosyalarının şifrelerini kaba kuvvet saldırısı ile kırmaya yarayan bir araçtır.

## Gereksinimler

zipcrk aşağıdaki kütüphaneleri kullanır.

* Colorama

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/zipcrk.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -v        | Verbose. Çıktı göstermek için kullanılır. |
| -w        | Wordlist. Parolaların bulunduğu wordlist dosyasını belirtmek için kullanılır. |
| -z        | Zipfile. Saldırı yapılacak zip dosyasını belirtmek için kullanılır. |

```bash
usage: zipcrk.py [-h] --wordlist WORDLIST --zipfile ZIPFILE [--verbose]

options:
  -h, --help           show this help message and exit
  --wordlist WORDLIST
  --zipfile ZIPFILE
  --verbose
```

## Örnekler

```python
python3 zipcrk.py -z test.zip -w rockyou.txt -p toor -v
```
