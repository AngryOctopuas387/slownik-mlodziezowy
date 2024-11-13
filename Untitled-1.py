
slownik={
    'jolo':'to żyje się tylko raz',
    'fejm':'to popularność',
    'swag':'słowa tożsame z polskim lansowaniem się czyli sztuką autoprezentacji',
    'hashtag':"nazwa znaku # używanego w social mediach do tagowania pewnych pojęć"

}
while True:

    pyt = input('podaj słowo które chcesz przetumaczyć: ')
  
    if pyt in slownik.keys():
        print(pyt,' oznacza: ',slownik[pyt])
    elif pyt == 'info':
        for i in slownik.keys():
            print(i)
    else:   
        print("nie ma takiego słowa w słowniku")
        print("wpisz info aby wyświetlić słownik")
        