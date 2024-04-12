import re

# Regex ifadeleri
regex_patterns = [
    r'\b(5\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})\b(?:\s+|\s*-\s*)(\d{2}/\d{2})\b(?:\s+|\s*-\s*)(\d{3})\b',
    r'\b(4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})\b(?:\s+|\s*-\s*)(\d{2}/\d{2})\b(?:\s+|\s*-\s*)(\d{3})\b',
    r'\b(6\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})\b(?:\s+|\s*-\s*)(\d{2}/\d{2})\b(?:\s+|\s*-\s*)(\d{3})\b',
    r'\b(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})\b(?:\s+|\s*-\s*)(\d{2}/\d{2})\b(?:\s+|\s*-\s*)(\d{3})\b'
]

# Kart bilgilerini bul ve veriler.txt'ye kaydet
def find_and_save_credit_card_info(input_file, output_file):
  with open(input_file, 'r', encoding='utf-8') as f:
    input_data = f.read()

    with open(output_file, 'w') as f:
        for pattern in regex_patterns:
            matches = re.findall(pattern, input_data)
            for match in matches:
                # Kart numarası, son kullanım tarihi ve CVV numarasını al
                card_number, expiry_date, cvv = match[0], match[1], match[2]
                f.write(f"{card_number}|{expiry_date}|{cvv}\n")

# Ana program
if __name__ == "__main__":
    input_file = 'b.txt'  # Kart bilgilerinin bulunduğu dosya
    output_file = 'veriler.txt'  # Kart bilgilerinin kaydedileceği dosya
    find_and_save_credit_card_info(input_file, output_file)
    print("Kart bilgileri veriler.txt dosyasına kaydedildi.")
