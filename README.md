# Subdomain Filter 🔍

Tool sederhana untuk memfilter subdomain/domain yang tidak berguna dari daftar blacklist.

## 📋 Blacklist default
- cpcallenders, cpcalendars, cpanel, cpcontacts
- webmail, mail, webdisk, whm, autodiscover

## 🚀 Cara penggunaan

```bash
python filter.py -l input.txt -o output.txt
```

Parameter:

Parameter Keterangan
-l, --list File input berisi daftar domain
-o, --output File output hasil filter

📝 Contoh

```bash
python filter.py -l domains.txt -o clean.txt
```

✨ Fitur

· Filter case-insensitive (tidak peduli huruf besar/kecil)
· Skip baris yang mengandung kata dalam blacklist
· Output terformat rapi
