from time import sleep
from datetime import datetime


class User:
    def __init__(self):
        self.nickname = ''
        self.password = ''
        self.age = int()

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return '{}'.format(self.nickname)

    def __repr__(self):
        return 'Object of class User({}, {}, {})'.format(self.nickname, self.password, self.age)

    def __eq__(self, other):
        if self.nickname == other.nickname and hash(self.password) == hash(other.password):
            return True
        else:
            return False


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if self.title == other.title and self.duration == other.duration:
            return True
        else:
            return False


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User()

    def log_in(self, nickname, password):
        login_error = 2  # Переменная login_error фиксирует ошибки при входе: нет ошибки (0);
                        # ввод неверного пароля (1);  ввод несуществующего имени (2).
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                    self.current_user = user
                    print(f'Привет, {nickname}! Вход выполнен.')
                    login_error = 0
                    break
            elif user.nickname == nickname and hash(user.password) != hash(password):
                print(f'Введён неверный пароль. Вход не выполнен. Попытайтесь войти снова.')
                login_error = 1
                break
            else:
                continue
        if login_error == 2:
            print(f'Пользователь с именем {nickname} не существует. '
                  'Чтобы получить доступ к содержимому, пройдите регистрацию или войдите под другим именем.')


    def register(self, nickname, password, age):
        registered_user = User()  # registered_user - регистрируемый пользователь.
        registered_user.nickname = nickname
        registered_user.password = password
        registered_user.age = age
        register_error = False # Переменная register_error фиксирует ошибки при регистрации.
                                # Значение False - нет ошибок.
        if not self.users:
            self.users.append(registered_user)
        else:
            for user in self.users:
                if user.nickname == nickname:
                    print(f'Пользователь с именем {nickname} уже существует. Измените имя и повторите регистрацию.')
                    register_error = True # Ошибка регистрации.
                    break
                else:
                    continue
        if register_error == False:
            # print(f'Привет, {nickname}! Регистрация прошла успешно. Вход выполнен.')
            self.users.append(registered_user)
            self.current_user = registered_user

    def log_out(self):
        self.current_user = None

    def add(self, *added_videos): # added_videos - список добавляемых объектов класса Video.
        new_videos = [] # new_videos - список фильмов (из добавляемых), которых ранее не было на платформе.
        for added_video in added_videos:
            comparison_res = False # Результат сравнения видео; начальное значение False;
                                # False остаётся, если видео из списка *added_videos не было в списке self.videos
            for video in self.videos:
                if added_video != video:
                    continue
                else:
                    comparison_res = True
                    break
            if comparison_res == False:
                new_videos.append(added_video)
        self.videos = self.videos + new_videos
        return self.videos


    def get_videos(self, search_word):
        requested_videolist = [] # Список видео, содержащих поисковое слово.
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                requested_videolist.append(video.title)
        return requested_videolist

    def watch_video(self, title):
        if self.current_user.nickname != '':
            # video_finded = False # Переменная, фиксирующее наличие запрашиваемого фильма в списке videos.
            for video in self.videos:
                if video.title == title:
                    # video_finded = True
                    if video.adult_mode == True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу!')
                        break
                    else:
                        time_start = datetime.now().timestamp()
                        for i in range (int(video.duration) + 1):
                            time_end = datetime.now().timestamp()
                            video.time_now = int(time_end - time_start)
                            print(video.time_now, end=' ')
                            sleep(1)
                        video.time_now = 0
                        print('Конец видео.')
            # if video_finded == False:
                # print('Видео не найден.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# print(ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в чужой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


# ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ.
print('')
# Проверка поиска
print(ur.get_videos('рук'))
print(ur.get_videos('ПРОГ'))

# Проверка входа в UrTube.
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.log_in('drug', 'Trunb56')
ur.log_in('vasya_pupkin', 'um')

# Проверка сброса текщего пользователя UrTube.
ur.log_out()
print(ur.current_user)