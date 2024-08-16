import os

# Alıntılar dosyasının adı
quotes_file = 'alintilar.txt'

# GitHub profil README dosyasının adı
readme_file = 'README.md'

def read_quotes(file):
    with open(file, 'r', encoding='utf-8') as f:
        quotes = f.readlines()
    return quotes

def update_readme(quotes, readme):
    with open(readme, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # Alıntılar bölümünü güncelle
    start_index = content.index('<!-- START_QUOTES -->\n') + 1
    end_index = content.index('<!-- END_QUOTES -->\n')

    new_content = content[:start_index] + quotes + content[end_index:]

    with open(readme, 'w', encoding='utf-8') as f:
        f.writelines(new_content)

if __name__ == '__main__':
    quotes = read_quotes(quotes_file)
    update_readme(quotes, readme_file)
