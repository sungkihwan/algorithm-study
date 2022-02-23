class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % \
               (self.name, self.position)

    def __add__(self, other):
        return self.name + other.name

abc = SoccerPlayer("kiki","sung",1)
abcd = SoccerPlayer("mozzi","yum",2)

print(abc.__str__())
abc.change_back_number(3)
print(abc.__add__(abcd))


class Note(object):
    def __init__(self, content = None):
        self.content = content

    def write(self, content):
        self.content = content

    def remove(self):
        self.content = ""

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content


class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self,note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())