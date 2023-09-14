import json
import os.path
from datetime import datetime


class Note:
    def __init__(self, id, title, body, creation_time):
        self.id = id
        self.title = title
        self.body = body
        self.creation_time = creation_time
        self.last_modified_time = creation_time

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "creation_time": str(self.creation_time),
            "last_modified_time": str(self.last_modified_time)
        }
    @classmethod

    def from_dict(cls, d):
        return cls(
            id=d["id"],
            title=d["title"],
            body=d["body"],
            creation_time=datetime.fromisoformat(d["creation_time"]),
        )
    def __repr__(self):
        return f"<Note {self.title} ({self.id})>"
    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                data = json.load(f)
        else:
            data = {"notes": []}
        return data

    def save_notes(data):
        with open("notes.json", "w") as f:
            json.dump(data, f, indent=4)

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите основную часть заметки: ")
        timestamp = datetime.now()
        id = len(data["notes"]) + 1
        note = Note(id, title, body, timestamp)
        data["notes"].append(note.to_dict())
        self.save_notes(data)
        print(f"Заметка '{title}' создана.")

    def read_note(self):
        identifier = input("Введите id заметки или заголовок: ")
        for note_dict in data["notes"]:
            if str(note_dict["notes"]) == identifier or note_dict["title"] == identifier:
                note = Note.from_dict(note_dict)
                print(note.title)
                print(note.body)
                print(note.create_time)
                print(note.last_modified_time)
                return
            print(f"Заметка '{identifier}' не найдена.")

    def update_note(self):
        identifier = input("Введите id заметки или заголовок: ")
        for note_dict in data["notes"]:
            if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:
                title = input(f"Введите новый заголовок ({note_dict['title']}): ")
                body = input(f"Введите новый вариант основной части заметки ({note_dict['body']}): ")
                note_dict["title"] = title or note_dict["title"]
                note_dict["body"] = body or note_dict["body"]
                note_dict["last_modified_time"] = str(datetime.now())
                self.save_notes(data)
                print(f"Заметка '{note_dict['title']}' обновлена.")
                return
            print(f"Заметка '{identifier}' не найдена.")

    def delete_note(self):
        identifier = input("Введите id заметки или заголовок: ")
        for note_dict in data["notes"]:
            if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:
                data["notes"].remove(note_dict)
                self.save_notes(data)
                print(f"Заметка '{note_dict['title']}' удалена.")
                return
            print(f"Заметка '{identifier}' не найдена.")

    def list_notes(self):
        for note_dict in data["notes"]:
            note = Note.from_dict(note_dict)
            print(note.title)
            print(note.body)
            print(note.creation_time)
            print(note.last_modified_time)
            print()

    def main(self):
        global data
        data = self.load_notes()

        while True:
            action = input(
                "Введите 'n' чтобы создать новую заметку, 'r' чтобы читать заметку, 'u' чтобы обновить заметку, 'd' удалить заметку, 'l' чтобы выводить списком все заметки, или 'q' выйти из заметки: ")
            if action == "n":
                self.create_note()
            elif action == "r":
                self.read_note()
            elif action == "u":
                self.update_note()
            elif action == "d":
                self.delete_note()
            elif action == "l":
                self.list_notes()
            elif action == "q":
                break
            else:
                print("Некорректное действие.")

    if __name__ == "__main__":
        main()

