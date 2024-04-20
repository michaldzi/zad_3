import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict


def get_files(directory):

    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def sort_files_by_extension(files):

    sorted_files = defaultdict(list)
    for file in files:
        _, extension = os.path.splitext(file)
        sorted_files[extension].append(file)
    return sorted_files


def move_files(files_by_extension, destination_folder):

    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(destination_folder, extension.strip("."))
        os.makedirs(extension_folder, exist_ok=True)
        for file in files:
            shutil.move(file, extension_folder)


def process_directory(directory):

    files = get_files(directory)
    sorted_files = sort_files_by_extension(files)
    move_files(sorted_files, directory)


def parallel_process_directories(root_directory, num_threads=4):

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for root, _, _ in os.walk(root_directory):
            executor.submit(process_directory, root)


if __name__ == "__main__":
    root_folder = "tutaj podaj ścieżkę folderu"
    parallel_process_directories(root_folder)
