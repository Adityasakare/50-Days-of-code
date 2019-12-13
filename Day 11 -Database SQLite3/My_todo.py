import DB_helper

def main():
    run = 1
    DB_helper.create_table()

    while run:
        print("\n")
        print('1. Insert New task intodo list \n'
              '2. View todo list \n'
               '3.Delete the task \n'
                '4.exits \n')

        x = input("Choose any above one option ")

if __name__ == "__main__": main()SP