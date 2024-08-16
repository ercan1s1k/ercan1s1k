def update_readme(quotes, readme):
    with open(readme, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # Alıntılar bölümünü güncelle
    try:
        start_index = content.index('<!-- START_QUOTES -->\n') + 1
        end_index = content.index('<!-- END_QUOTES -->\n')
    except ValueError:
        print("README.md dosyasında gerekli etiketler bulunamadı.")
        return

    new_content = content[:start_index] + quotes + content[end_index:]

    with open(readme, 'w', encoding='utf-8') as f:
        f.writelines(new_content)

    # Debug print statements
    print("Alıntılar eklendi:")
    print(new_content[start_index:end_index])

if __name__ == '__main__':
    quotes_file = 'alintilar.txt'
    readme_file = 'README.md'
    quotes = read_quotes(quotes_file)
    print("Okunan alıntılar:", quotes)  # Hata ayıklama mesajı
    update_readme(quotes, readme_file)
