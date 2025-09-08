from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotFound  # here are HttpRequest, HttpResponse, HttpResponseForbidden and so on; QueryDict class, ...
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from main_app.models import Greeting, Student, Faculty, StudentFaculty, Band, Musician, Book, Author, Publisher


def index(request):
    return HttpResponse("Hello, world!")


def page2(request):
    return render(request, "page2.html")


def page3_view(request):
    all_greetings = Greeting.objects.all() # will be written to all_greetings: QuerySet
    return render(request, "page3.html", context={"data": all_greetings})


def page4_view(request):
    greetings_dict = []
    for elem in Greeting.objects.all():
        greetings_dict.append(f'lang: {elem.language}, text: {elem.text}\n')
    return render(request, "page4.html", context={"data2": greetings_dict})


def get_user_name(request):
    name = request.GET.get('name', 'гость')
    return HttpResponse(f'Привет, {name}!')


def get_rect_area(request):
    width = request.GET.get('width', None)
    height = request.GET.get('height', None)

    if width is None or height is None:
        return HttpResponse("Нет данных")

    result = str(int(width) * int(height))
    return HttpResponse(result)


def operate(request):
    data = request.GET
    a = data.get('a', None)
    b = data.get('b', None)
    operation = data.get('operation', None)

    if a is None or b is None or operation is None:
        return HttpResponse("Нет данных")
    else:
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            if a < 0 or b < 0:
                return HttpResponse('Неверный формат a или b')
        else:
            return HttpResponse('Неверный формат a или b')

    if operation == 'add':
        return HttpResponse(f'{int(a) + int(b)}')
    elif operation == "subtract":
        return HttpResponse(f'{int(a) - int(b)}')
    return HttpResponse('Неверный формат operation')


def get_text(request):
    text = request.GET.get('text', None)
    if text is None:
        return HttpResponse("Нет данных")
    return HttpResponse(str(text.count(" ") + 1))


def get_params_list(request):
    result = ', '.join(request.GET.values())
    return HttpResponse(result)


def get_client_info_json(request):
    headers = request.headers
    keys = ("User-Agent", "Accept-Language", "Host")

    has_auth = False
    if "Authorization" in headers.keys():
        has_auth = True

    result = dict()
    for key in keys:
        result[key] = headers.get(key, 'Unknown')

    result["has_authorization"] = True if has_auth else False

    return JsonResponse(result)


def verify_post(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.get('text'))
    return HttpResponse("Пришлите POST запрос")


def registration(request):
    if request.method == "POST":
        features = dict()

        for field in ['username', 'email', 'password']:
            if not request.POST.get(field):
                return HttpResponse("Заполните все поля")
            else:
                features[field] = request.POST.get(field)

        return render(request, 'index_12.html', context=features)
    return HttpResponse("Не POST-запрос. Просьба направить POST-запрос для регистрации")


def email_validation(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        if email is not None and not ' ' in email and '@' in email and '.' in email:
            return HttpResponse("Емайл в порядке")
        return HttpResponse("Укажите корректный емайл")

    elif request.method == "GET":
        email = request.GET.get('email', None)
        if email is not None and not ' ' in email and '@' in email and '.' in email:
            return HttpResponse("Емайл в порядке")
        return HttpResponse("Укажите корректный емайл")
    return HttpResponse("Некорректный метод")


def file_data(request):
    super_file = request.FILES.get('my_super_file')
    if super_file:
        if super_file.name[-4:] == '.txt':
            data = super_file.read()
            return HttpResponse(data)
        return HttpResponse("Поддерживаются только текстовые файлы")
    return HttpResponse("Файл не найден")


def file_data_2(request):
    if request.method == 'GET':
        return HttpResponse("Пришлите POST запрос с файлом")

    document = request.FILES.get('document')

    if document:
        document_content = document.read()

        if document_content.count(' ') != 0:
            return HttpResponse(f"В файле {document.name} {document_content.count(' ') + 1} слов")
        return HttpResponse(f"В файле {document.name} {0} слов")

    return HttpResponse("Файл не найден")


# learning CRUD basics


# def get_book_params(request):
#     books = Book.objects.all()
#     return render(request, 'index_16.html', context={"books_data": books})


# def change_author(request):
#     Book.objects.filter(title='Муму', author='Пушкин').update(author="Тургенев")


# def get_data_by_id(request):
#     book_id = request.GET.get('id')
#
#     try:
#         book = Book.objects.get(id=book_id)
#         return HttpResponse(f"{book.title} - {book.author}")
#     except Book.DoesNotExist:
#         return HttpResponseNotFound("Такой книги нет")


# def create_delete(request):
#     new_ids = []
#     Book.objects.create(title='NewBook', author='NewAuthor')
#     Book.objects.create(title='NewBook2', author='NewAuthor')
#
#     Book.objects.filter(title='NewBook', author='NewAuthor').delete()
#     Book.objects.filter(title='NewBook2', author='NewAuthor').delete()


def view(request):
    if request.method == 'GET':
        data = request.GET

        first = data.get('first_name')
        second = data.get('second_name')

        if not first or not second:
            return JsonResponse({"message": "Студент не найден"}, status=404)

        new_student = Student.objects.create(first_name=first, second_name=second)
        return JsonResponse({"message": "Студент с именем {} {} создан с id {}".format(new_student.first_name,
                                                                                       new_student.second_name,
                                                                                       new_student.id)})

    return JsonResponse({"message": "Метод не поддерживается"}, status=405)


def visits_count(request):
    try:
        request.session['visits_count'] += 1
    except KeyError:
        request.session['visits_count'] = 1
    return HttpResponse(f"Вы посетили эту страницу {request.session['visits_count']} раз(а).")


def clear_session(request):
    request.session.clear()
    return HttpResponse("Сессия очищена")


class Greeting(View):
    def get(self, request):
        guest_name = request.GET.get('name', 'Гость')
        return HttpResponse(f'Привет, {guest_name}!')


class GetToken(View):
    def post(self, request):
        token = request.POST.get('token', None)

        if token is None:
            return HttpResponse("Токен не найден")
        return HttpResponse(f"Токен получен: {token}")


class SaveSessionData(View):
    def post(self, request):
        request.session['my_value'] = request.POST.get('my_value')

    def get(self, request):
        if (value := request.session.get('my_value')) is not None:
            return HttpResponse(value)
        return HttpResponse("Значение не установлено")


def get_faculty_info_from_student(request):
    students = []
    for student in StudentFaculty.objects.all():
        students.append(student)
    return render(request, 'students.html', context={'students': students})


def band_and_musicians_view(request):
    # Получить всех музыкантов группы
    band = Band.objects.get(id=36)
    band_musicians = band.musicians.all()

    # Получить все группы, в которых играет музыкант
    musician = Musician.objects.get(id=61)
    musician_bands = musician.bands.all()

    # Подготовка данных для ответа
    data = {
        "band": band.name,
        "band_musicians": [musician.name for musician in band_musicians],
        "musician": musician.name,
        "musician_bands": [band.name for band in musician_bands],
    }

    return JsonResponse(data)


def just_learning_queryset_view(request):
    books_1 = Book.objects.all()
    books_2 = Book.objects.filter(pages__gt = 300)
    books_3 = Book.objects.filter(pages__gt=300, rating__gt=4.5)
    books_4 = Book.objects.filter(author__country="Япония")
    books_5 = Book.objects.filter(title__icontains="django")
    author_1 = Author.objects.filter(name="Антон Чехов")
    authors_1 = Author.objects.filter(books__pages__gt=200)
    authors_2 = Author.objects.exclude(books__rating__lt=4)
    authors_3 = Author.objects.filter(books__rating__lt=2, books__pages__gt=500)
    publishers = Publisher.objects.filter(books__author__country="Австралия")


def user_info_view(request):

    user = request.user

    if user.is_authenticated:
        print(f'Привет, {user.username}!')
    else:
        return HttpResponse('Пожалуйста, войдите в систему.')

    print(f'Username: {user.username}')
    print(f'id: {user.id}')
    print(f'Емайл: {user.email}')
    print(f'Имя: {user.first_name}')
    print(f'Фамилия: {user.last_name}')
    print(f'Является ли админом: {user.is_superuser}')

    return HttpResponse('Информация о пользователе выведена в консоль')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)    # logout() also exists in django.contrib.auth
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('Неверное имя пользователя или пароль')

    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def check_authentification(request):
    user = request.user

    if user.is_authenticated:
        return HttpResponse(f'{user.username}, {user.email}')

    return redirect('/login/')


def create_user_from_post(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        User.objects.create_user(username=username, email=email, password=password)

    return HttpResponse("Not a POST request")


def authenticate_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('login success')

        return HttpResponse('login fail')

    return HttpResponse("Not a POST request")


def logout_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            logout(request)

        return HttpResponse("user is not authenticated")

    return HttpResponse("not a POST request")

