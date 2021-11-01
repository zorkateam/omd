import math


class CountVectorizer:
    """
    Класс CountVectorizer:
    Поля:
    features - список уникальных слов в корпусе текстов
    count_matrix - Терм-документная матрица
    corpus - исходный корпус текстов
    Методы:
    fit_transform - формируем матрицу с количеством вхождений слов из features в корпус текстов
    get_feature_names - возвращает список уникальных слов из корпуса текстов
    """

    def __init__(self):
        self.features = []
        self.count_matrix = []
        self.corpus = []

    def fit_transform(self, corpus: list) -> list:
        """
        :param corpus: список строк с текстом
        :return: Терм-документная матрица для этого списка текстов размера (n_samples, n_features)
        """
        # Заполняем список features
        for text in corpus:
            string_ = text.lower().split(' ')
            self.corpus.append(string_)
            for word in string_:
                if word and word not in self.features:
                    self.features.append(word)
        # Заполняем count_matrix
        self.count_matrix = []
        for row_number, text in enumerate(self.corpus):
            self.count_matrix.append([])
            for word in self.features:
                self.count_matrix[row_number].append(text.count(word))
        return self.count_matrix

    def get_feature_names(self):
        """
        :return: возвращает список уникальных слов из корпуса текстов
        """
        return self.features

    def tf_transform(self, count_matrix: list) -> list:
        """
        :param count_matrix: list - cписок текстов
        :return: res: list - tf матрица для входной count_matrix
        """
        res = []
        for row in count_matrix:
            count_words = sum(row)
            res.append([round(x/count_words, 2) for x in row])
        return res

    def idf_transform(self, count_matrix: list) -> list:
        """
        Считаем idf для tf_matrix
        :param count_matrix: list
        :return: idf: list
        """
        res = []
        for i, word in enumerate(self.features):
            word_count = sum([row[i] > 0 for row in count_matrix])
            idf = round(math.log((len(count_matrix) + 1) / (word_count + 1)) + 1, 2)
            res.append(idf)
        return res


class TfidfTransformer:

    def __init__(self):
        pass

    def fit_transform(self, tf_matrix: list, idf: list) -> list:
        """
        делаем преобразование tf_idf для tf_matrix
        :param tf_matrix: list
        :param idf: list
        :return: tf_idf_matrix: list
        """
        tf_idf_matrix = []
        for row in tf_matrix:
            tf_idf_matrix.append([round(x*y, 2) for x, y in zip(row, idf)])
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform_tfidf(self, corpus: list) -> list:
        count_matrix = self.fit_transform(corpus)
        tf_matrix = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        return self.tf_idf.fit_transform(tf_matrix, idf)


def is_equal_lists(list_a: list, list_b: list) -> bool:
    """
    Проверяем равенство списков
    :param list_a: Первый список для проверки
    :param list_b: Второй список для проверки
    :return: bool
    """
    if len(list_a) != len(list_b):
        return False
    else:
        for a, b in zip(list_a, list_b):
            if a != b:
                return False
    return True


def make_tests() -> bool:
    """
    Проводим тесты методов класса CountVectorizer
    :return: bool
    """
    tests = {1: {'input': ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients '
                           'Parmesan to taste'],
                 'term_matrix': [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]],
                 'features': ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh', 'ingredients',
                              'parmesan', 'to', 'taste']},

             2: {'input': ['0', '', 'a', ''],
                 'term_matrix': [[1, 0], [0, 0], [0, 1], [0, 0]],
                 'features': ['0', 'a']},

             3: {'input': ['', '', '', ''],
                 'term_matrix': [[], [], [], []],
                 'features': []},

             4: {'input': ['Читайте классику снова и снова',
                           'Пушкина Демидовича Толстого',
                           'Решайте за завтраком решайте перед сном',
                           'Когда вас положат после сессии в дурдом'],
                 'term_matrix': [[1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]],
                 'features': ['читайте', 'классику', 'снова', 'и', 'пушкина', 'демидовича', 'толстого',
                              'решайте', 'за', 'завтраком', 'перед', 'сном', 'когда', 'вас', 'положат',
                              'после', 'сессии', 'в', 'дурдом']}
             }

    for test_number, test in tests.items():
        vectrzr = CountVectorizer()
        term_matrix = vectrzr.fit_transform(test['input'])
        features = vectrzr.get_feature_names()
        for row_term_matrix, row_test_matrix in zip(term_matrix, test['term_matrix']):
            assert is_equal_lists(row_term_matrix, list(row_test_matrix)), f'Тест {test_number}. Ошибка в term_matrix'
        assert is_equal_lists(features, test['features']), f'Тест {test_number}. Ошибка в списке features'
    return True


if __name__ == "__main__":
    if make_tests():
        print('Все тесты пройдены!')

    new_text2 = ['Семь бед один ответ',
                 'Костыль и велосипед',
                 'Семь бед один ответ',
                 'Вставь костыль изобрети велосипед']

    new_text = ['Crock Pot Pasta Never boil pasta again',
                'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = TfidfVectorizer()
    idf = vectorizer.fit_transform_tfidf(new_text)
    print(vectorizer.get_feature_names())
    print(idf)
