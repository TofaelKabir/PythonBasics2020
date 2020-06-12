class Students:
    id = ""
    name = ""
    group = ""
    gpa = ""

    def setValue(self, id, name, group, gpa):
        self.id = id
        self.name = name
        self.group = group
        self.gpa = gpa

    def display(self):
        print(f"ID:{self.id},Name:{self.name},Group:{self.group},GPA:{self.gpa}")


st = Students()
st.id = 103
st.name = "Mohammad Sharif"
st.group = "Commerce"
st.gpa = 4.99
st.display()
print("_____________________________________")
# We can set the value by using setValue()
st1 = Students()
st1.setValue(101, "Mohammad Tofayel", "Science", 5.00)
st1.display()
print("_____________________________________")
st2 = Students()
st2.setValue(102, "Mohammad Sohag", "Commerce", 4.99)
st2.display()
