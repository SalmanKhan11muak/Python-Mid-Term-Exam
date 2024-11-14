class Hall:
    def __init__(self,rows,cols,hall_no):
        self.__seats={}
        self.__show_list=[]
        self.row=rows
        self.col=cols
        self.hall_no=hall_no


    def _initialize_seats(self):
           return [[0 for _ in range(self.col)] for _ in range(self.row)]


    def entry_show(self,show_id,movie_name,time):
         show_info=(show_id,movie_name,time)
         self.__show_list.append(show_info)
         self.__seats[show_id] = self._initialize_seats()

        
    def book_seats(self,show_id,seat_for_book):
        if show_id not in self.__seats:
              raise ValueError(f'show id {show_id} not exist')
        
        show_seats = self.__seats[show_id]

        for row,col in seat_for_book:
            if row < 0 or 0 > col:
                raise ValueError('nagative row & col not allow')
            
            if show_seats[row][col] != 0:
                raise ValueError('sir,That Seat Already Booked')
            
            show_seats[row][col] = 1

    def view_show_list(self):
        for show_id,movie_name,time in self.__show_list:
            print(f'MOVIE NAME:{movie_name}({show_id}) SHOW ID:{show_id} TIME:{time}')


    def view_available_seat(self,show_id):
        if show_id not in self.__seats:
            raise ValueError(f'sir,You gives a wrong id of a show')
        
        show_seats=self.__seats[show_id]
        for seat in show_seats:
            print(' '.join(map(str,seat)))




class Star_Cinema:
    hall_list=[]

    @classmethod
    def entry_hall(self,hall):
        self.hall_list.append(hall)


cinema=Star_Cinema()
hall_01= Hall(7,7,1)
cinema.entry_hall(hall_01)
hall_01.entry_show(111,'Jawan Maji','12/11/2024 11:00 AM')
hall_01.entry_show(333,'Sujon Maji','12/11/2024 02:00 PM')


def option():
    print(
        """ 
            1. View all show today
            2. view avalable seat
            3. book ticket
            4. exit 
            """ )

while(True):
    option()
    n=int(input("enter option: "))

    if(n==1):
        print('-----------------------------------------------------------------')
        for hall in Star_Cinema.hall_list:
            hall.view_show_list()
        print('-----------------------------------------------------------------')
        

    elif(n==2):
        show_id=int(input('ENTER SHOW ID:'))
        flag=False
        for hall in Star_Cinema.hall_list:
            if show_id in [show[0] for show in hall._Hall__show_list]:
                hall.view_available_seat(show_id)
                flag=True
                break

        if not flag:
            print('Wrong show id!!')
       
    elif(n==3):
        show_id=int(input('Show Id:'))
        num_of_tickets=int(input('Number of Tickets?:'))
        
        no_of_seat_for_book=[]
        for _ in range(num_of_tickets):
            row = int( input('Enter Seat Row:') )

            col = int( input('Enter Seat Col:') )
            no_of_seat_for_book.append((row,col))

        for hall in Star_Cinema.hall_list:
                hall.book_seats(show_id,no_of_seat_for_book)
                print(f'Seats{no_of_seat_for_book}booked for show {show_id}')

    elif(n==4):
        print('You successfully Exit')
        break
    else:
        print('Oops !! please choose option b/w 1 to 4')

