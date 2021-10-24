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

    def fit_transform(self, corpus):
        """
        :param corpus: список строк с текстом
        :return: Терм-документная матрица для этого списка текстов размера (n_samples, n_features)
        """
        # Заполняем список features
        for row_number in corpus:
            string_ = row_number.lower().split(' ')
            self.corpus.append(string_)
            for word in string_:
                if word not in self.features:
                    self.features.append(word)
        # Заполняем count_matrix
        for row_number, current_string in enumerate(self.corpus):
            self.count_matrix.append([])
            for _, word in enumerate(self.features):
                self.count_matrix[row_number].append(current_string.count(word))
        return self.count_matrix

    def get_feature_names(self):
        """
        :return: возвращает список уникальных слов из корпуса текстов
        """
        return self.features


a = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(a)
print(vectorizer.get_feature_names())
print(count_matrix)
