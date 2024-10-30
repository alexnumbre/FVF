
import os

class DirectoryAnalyzer:
    def __init__(self, path='.'):
        self.path = path
        self.sizes = {}

    def calculate_sizes(self):
        for root, dirs, files in os.walk(self.path):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    size = os.path.getsize(file_path)
                    self.sizes[file_path] = size
                except FileNotFoundError:
                    continue  # Игнорируем отсутствующие файлы

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)))
                    self.sizes[dir_path] = size
                except FileNotFoundError:
                    continue  # Игнорируем отсутствующие директории

    def print_sorted_sizes(self):
        sorted_sizes = sorted(self.sizes.items(), key=lambda item: item[1], reverse=True)
        for path, size in sorted_sizes:
            print(f"{path}: {size} bytes")

if __name__ == "__main__":
    analyzer = DirectoryAnalyzer()
    analyzer.calculate_sizes()
    analyzer.print_sorted_sizes()
