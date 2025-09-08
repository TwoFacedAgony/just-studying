from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound  # here are HttpRequest, HttpResponse, HttpResponseForbidden and so on; QueryDict class, ...
from django.shortcuts import render
from django.views import View

from main_app.models import Greeting, Student, StudentFaculty, Faculty


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


def get_all_faculty_students(request):
    itmo_faculty = Faculty.objects.get(id=1)
    itmo_students = itmo_faculty.studentfaculty_get.all()

    for student in itmo_students:
        print(f'ID: {student.id}, Name: {student.first_name} {student.last_name}')