# Статические методы

class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

my_comment = Comment("My comment")

m_1 = Comment.merge_comments("Привет,","студент!")
print(m_1)
m_2 = Comment.merge_comments("Great","OK")
print(m_2)