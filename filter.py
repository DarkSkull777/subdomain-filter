import argparse

# daftar subdomain / kata yang tidak berguna
BLACKLIST = [
    "cpcallenders",
    "cpcalendars",
    "cpanel",
    "cpcontacts",
    "webmail",
    "mail",
    "webdisk",
    "whm",
    "autodiscover"
]

def filter_domains(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            line_strip = line.strip()
            lower_line = line_strip.lower()

            # cek apakah line mengandung kata blacklist
            if any(bad in lower_line for bad in BLACKLIST):
                continue  # skip / hapus baris

            outfile.write(line_strip + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filter domain/subdomain yang tidak berguna"
    )
    parser.add_argument("-l", "--list", required=True, help="File input list domain")
    parser.add_argument("-o", "--output", required=True, help="File output hasil filter")

    args = parser.parse_args()

    filter_domains(args.list, args.output)
    print(f"[+] Filtering selesai. Hasil disimpan di: {args.output}")
