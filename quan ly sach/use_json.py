import json

def add_data():
    order=int(input("Numerical order: "))
    title=input("Title: ")
    author=input("Author: ")
    year=input("Year: ")

    dic = {
        'Numerical order: ' : order,
        'Title: ' : title,
        'Author: ': author,
        'Year: ': year
    }

    with open("books.json","r") as temp:
        data=json.load(temp)
        #data.append(dic)
        data[order] = dic

        with open("books.json","w") as save:
            json.dump(data,save)
            print("Thêm sách thành công")

def show_data():
    with open("books.json","r") as temp:
        data=json.load(temp)
        for i,m in data.items():
            for x,n in m.items():
                print(x,n)
            print("\n")

def detele_data():
    number = input("Enter the numerical order of book: ")

    with open("books.json","r") as get_data:
        data=json.load(get_data)

        if number in data:
            data.pop(number)

            with open("books.json","w") as delete:
                json.dump(data,delete)
                print("Xoa thanh cong")
        else: 
            print("Stt nay khong co trong thu vien!")

def update_data():
    number = input("Enter the numerical order of book: ")
    with open("books.json","r") as get_data:
        data=json.load(get_data)

        if number in data:
            title=input("Title: ")
            author=input("Author: ")
            year=input("Year: ")

            dic = {
                'Numerical order: ' : number,
                'Title: ' : title,
                'Author: ': author,
                'Year: ': year
            }
            data[number] = dic

            with open("books.json","w") as update:
                json.dump(data,update)
                print("Update thanh cong!")


while(True):
    print("Chon 1 trong 5: ")
    print("1: Them sach\n2:In danh sach\n3: Xoa danh sach\n4:Sua danh sach\n5:thoat")
    choice=int(input("Nhap 1 trong 5 lua chon! "))
    match choice:
        case 1:
            add_data()
        case 2:
            show_data()
        case 3:
            detele_data()
        case 4:
            update_data()
        case 5:
            exit(0)
