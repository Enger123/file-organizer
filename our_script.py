from pathlib import Path

def downloads():
    general_dir = Path(__file__).parent
    return general_dir / 'downloads'

def sort_files():
    downloads_dir = downloads()

    suffixes = {
        'audio': ['.mp3', '.wav'],
        'code': ['.py', '.js', '.cpp'],
        'documents': ['.txt', '.pdf'],
        'images': ['.jpeg', '.png', '.jpg']
    }

    stats_moved = {
        'audio': 0,
        'code': 0,
        'documents': 0,
        'images': 0,
        'others': 0
    }

    audio_dir = downloads_dir / 'audio'
    code_dir = downloads_dir / 'code'
    documents_dir = downloads_dir / 'documents'
    images_dir = downloads_dir / 'images'
    others_dir = downloads_dir / 'others'

    audio_dir.mkdir(exist_ok=True)
    code_dir.mkdir(exist_ok=True)
    documents_dir.mkdir(exist_ok=True)
    images_dir.mkdir(exist_ok=True)
    others_dir.mkdir(exist_ok=True)

    for item in downloads_dir.iterdir():
        if item.is_dir() and item.name not in suffixes and item.name != 'others':
            print(f"До папки {item.name} немає суфіксів, по яким перекидати файли")
            suffix = input(f"Введіть суфікси для папки {item.name} через кому: ").strip().split(", ")
            suffixes[item.name] = suffix
            stats_moved[item.name] = 0

    found_files = False
    for file in downloads_dir.iterdir():
        if file.is_file():
            found_files = True
            matched = False
            for dir_name in suffixes:
                target_dir = downloads_dir / dir_name
                if file.suffix.lower() in suffixes[dir_name]:
                    matched = True
                    replace_file(file, target_dir)
                    stats_moved[dir_name] += 1
                    break
            if not matched:
                replace_file(file, others_dir)
                stats_moved['others'] += 1

    if not found_files:
        print("Файлів не знайдено для обробки")
    print(f"\nРезультат переміщень: ")
    for keys, values in stats_moved.items():
        print(f"{keys}: {values}")

def replace_file(file, dir):
    target = dir / file.name
    if not target.exists():
        file.replace(target)
        print(f"{file.name} -> {dir.name}")
    else:
        new_file = rename_file(file)
        replace_file(new_file, dir)

def rename_file(old_file):
    base_name = old_file.stem.split("(")[0]
    i = 1
    new_file = old_file.with_name(f"{base_name}{i}{old_file.suffix}")
    while new_file.exists():
        i += 1
        new_file = old_file.with_name(f"{base_name}{i}{old_file.suffix}")
    old_file.replace(new_file)
    return new_file

def show_struct():
    downloads_dir = downloads()
    for item in downloads_dir.iterdir():
        if item.is_dir():
            for file in item.iterdir():
                print(f"{item.name} -> {file.name}")
        else:
            print(f"Файл {item.name}")

def show_stats():
    general_stats = {
        'images': 0,
        'code': 0,
        'audio': 0,
        'documents': 0,
        'others': 0
    }
    downloads_dir = downloads()
    for item in downloads_dir.iterdir():
        if item.is_dir():
            if not item.name in general_stats:
                general_stats[item.name] = 0
            for file in item.iterdir():
                if file.is_file():
                    general_stats[item.name] += 1
    for dirs, values in general_stats.items():
        print(f"{dirs} - {values} файлів")

def main():
    print("Ви у організаторі файлів")
    while True:
        print("\nВиберіть пункт: ")
        print("1 - відсортувати файли")
        print("2 - показати структуру папок")
        print("3 - показати статистику по файлах в папках")
        print("4 - вийти")
        num = input("Введіть цифру: ")
        if num not in ('1', '2', '3', '4'):
            print("Ви вийшли за межі.")
        elif num == '1':
            sort_files()
        elif num == '2':
            show_struct()
        elif num == '3':
            show_stats()
        else:
            break

if __name__ == '__main__':
    main()

