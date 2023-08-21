import json

class book:
    def __init__(self,order,title,author,year):
        self.order=order
        self.title=title
        self.author=author
        self.year=year

class library:

    def show_data(self):
        with open("library.json","r") as get:
            data=json.load(get)

        lis = []
        for ele in data:
            lis.append(ele)
        
        for ele in lis:
            for key,val in ele.items():
                print(key,val)

    def add_data(self):
        order=int(input("Numerical order: "))
        title=input("Title: ")
        author=input("Author: ")
        year=input("Year: ")

        with open("library.json","r") as get_data:
            data=json.load(get_data)
        add=[]
        for ele in data:
            add.append(ele)
        add.append(book(order,title,author,year))
        
        json_string = json.dumps(add, default=lambda x: x.__dict__)
        with open("library.json", "w") as file:
            file.write(json_string)
            print("Them sach thanh cong!")

    def delete_data(self):
        number = int(input("Enter the numerical order of book: "))

        with open("library.json","r") as get_data:
            data=json.load(get_data)

        for ele in data:
            if number==ele["order"]:
                data = [ ele for ele in data if ele["order"] != number]
                print("Da xoa thanh cong!!")
            else:
                print("STT ko co trong danh sach")

        with open("library.json","w") as save:
            json.dump(data,save)

    def update_data(self):
        number = int(input("Enter the numerical order of book: "))

        with open("library.json","r") as get_data:
            data=json.load(get_data)

        for ele in data:
            if number==ele["order"]:
                title=input("Title: ")
                author=input("Author: ")
                year=input("Year: ")
                ele["title"] = title
                ele["author"] = author
                ele["year"] = year
                print("Da cap nhat thanh cong!!")
            else:
                print("STT ko co trong danh sach")

        with open("library.json","w") as save:
            json.dump(data,save)

while(True):
    lib = library()
    print("Chon 1 trong 5: ")
    print("1: Them sach\n2:In danh sach\n3: Xoa danh sach\n4:Sua danh sach\n5:thoat")
    choice=int(input("Nhap 1 trong 5 lua chon! "))
    match choice:
        case 1:
            lib.add_data()
        case 2:
            lib.show_data()
        case 3:
            lib.detele_data()
        case 4:
            lib.update_data()
        case 5:
            exit(0)
