def getWordsInLevel(test_num : int):
    file_path = f"rec/lessons/lesson{test_num}.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()  