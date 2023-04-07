#реализовать консольное приложение заметки, с сохранением, чтением,
#добавлением, редактированием и удалением заметок. Заметка должна
#содержать идентификатор, заголовок, тело заметки и дату/время создания
#или последнего изменения заметки. Сохранение заметок необходимо сделать
#в формате json или csv формат (разделение полей рекомендуется делать через
#точку с запятой). Реализацию пользовательского интерфейса студент может
#делать как ему удобнее, можно делать как параметры запуска программы
#(команда, данные), можно делать как запрос команды с консоли и
#последующим вводом данных, как-то ещё, на усмотрение студента.
from datetime import datetime
import csv
from sys import argv


class Note:
    def __init__(self, id=None, title=None, body=None, created_at=None):
        self.id = id or app.notes[-1].id + 1
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f'Заметка №{self.id}: {self.title} {self.created_at}'


class App:
    notes=[]

    def add(self):
        title = input('Введите заголовок: ')
        body = input('Введите саму заметку: ')
        note = Note(title=title, body=body)
        self.notes.append(note)
        print(f'Заметка успешно создана! {note}')
        return note

    def read(self):
        note_id = input('Введите идентификатор заметки: ')
        note = self.notes[int(note_id)-1]
        print(note, '\n', note.body)
    def delete(self):
        note_id = int(input('Введите идентификатор заметки, которую хотите удалить: '))
        note = self.notes[note_id - 1]
        answer = input(f'Вы точно хотите удалить заметку {note}? Ответьте yes или no: ')
        if answer == 'yes':
            for note in self.notes[note_id:]:
                print('before', note)
                note.id = note.id - 1
                print('after', note)
            self.notes = self.notes[:note_id -1] + self.notes[note_id:]
        print('Заметка удалена!')

    def edit(self):
        note_id = input('Введите идентификатор заметки: ')
        note = self.notes[int(note_id) - 1]
        title = input('Введите новый заголовок (или нажмите enter, чтобы оставить старый): ')
        body = input('Введите новую заметку (или нажмите enter, чтобы оставить старую): ')
        if title:
            note.title = title
        if body:
            note.body = body
        print('Заметка изменена!')

    def select(self):
        year_select = int(input('Введите год создания заметки: '))
        month_select = int(input('Введите месяц: '))
        day_select = int(input('Введите день: '))
             # print(note.created_at.year)

        for note in self.notes:
            if ((note.created_at.year == year_select)&(note.created_at.month == month_select)&(note.created_at.day == day_select)):
                print(note)
        return

    def list(self):
        for note in self.notes:
            print(note)
        return

    def read_from_file(self):
        with open('notes.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                id, title, body, created_at = row
                created_at = datetime.strptime(created_at, '%d.%m.%Y %H:%M:%S')
                note = Note(int(id), title, body, created_at=created_at)
                self.notes.append(note)

    def save_to_file(self):
        with open('notes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for note in self.notes:
                dt = datetime.strftime(note.created_at, '%d.%m.%Y %H:%M:%S')
                writer.writerow([note.id, note.title, note.body, dt])

app = App()
app.read_from_file()
main_instruction = 'Введите команду add, edit, delete, read, list, select, exit:   '
command = ''

while command != 'exit':
    command = input(main_instruction)
    if command == 'add':
        app.add()
    elif command == 'list':
        app.list()
    elif command == 'read':
        app.read()
    elif command == 'delete':
        app.delete()
    elif command == 'edit':
        app.edit()
    elif command == 'select':
        app.select()

try:
    app.save_to_file()
except Exception:
    print('Упс, мы не смогли сохранить твои заметки :(')
else:
    print('Мы сохранили твои заметки, до новых встреч!')
