from pathlib import Path
def sort_files():
    general_dir = Path(__file__).parent
    downloads_dir = general_dir / 'downloads'

    suffixes = {
        'code': ['.py', '.js', '.cpp'],
        'audio': ['.mp3', '.wav'],
        'images': ['.png', '.jpg', '.jpeg'],
        'documents': ['.txt', '.pdf']
    }

    images_dir = downloads_dir / 'images'
    audio_dir = downloads_dir / 'audio'
    code_dir = downloads_dir / 'code'
    documents_dir = downloads_dir / 'documents'
    others_dir = downloads_dir / 'others'

    images_dir.mkdir(exist_ok=True)
    audio_dir.mkdir(exist_ok=True)
    code_dir.mkdir(exist_ok=True)
    documents_dir.mkdir(exist_ok=True)
    others_dir.mkdir(exist_ok=True)
    found_files = False
    for file in downloads_dir.iterdir():
        if file.is_file():
            found_files = True
            if file.suffix.lower() in suffixes['images']:
                replace_file(file, images_dir)
            elif file.suffix.lower() in suffixes['documents']:
                replace_file(file, documents_dir)
            elif file.suffix.lower() in suffixes['code']:
                replace_file(file, code_dir)
            elif file.suffix.lower() in suffixes['audio']:
                replace_file(file, audio_dir)
            else:
                replace_file(file, others_dir)
    if not found_files:
        print("Файлів не знайдено для обробки")

def replace_file(file, dir):
    target = dir / file.name
    if not target.exists():
        file.replace(target)
        print(f"{file.name} -> {dir.name}")
    else:
        print(f"Файл {file.name} вже знаходиться в папці {dir.name}")

def show_struct():
    general_dir = Path(__file__).parent
    downloads_dir = general_dir / 'downloads'
    for item in downloads_dir.iterdir():
        if item.is_dir():
            for file in item.iterdir():
                print(f"{item.name} -> {file.name}")
        else:
            print(f"Файл {item.name}")

def main():
    print("Ви у організаторі файлів")
    while True:
        print("\nВиберіть пункт: ")
        print("1 - відсортувати файли")
        print("2 - показати структуру папок")
        print("3 - вийти")
        num = input("Введіть цифру: ")
        if num not in ('1', '2', '3'):
            print("Ви вийшли за межі.")
        elif num == '1':
            sort_files()
        elif num == '2':
            show_struct()
        else:
            break

if __name__ == '__main__':
    main()

