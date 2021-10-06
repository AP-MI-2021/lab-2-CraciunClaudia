def is_palindrome(n):
    '''
    Determina daca un numar este palindrom.
    -Input: n
     -Output : "Numarul este palindrom" sau "Numarul nu este palindrom"
    '''
    inv = 0
    x = n
    ogl=0
    while n!= 0:
        ogl=ogl * 10 + n % 10
        n = n / 10
    if x == ogl :
        print(f'Numarul este palindrom')
    elif x !=ogl :
        print(f'Numarul nu este palindrom')

def get_base_2(n: str):
    '''
    Transforma un numar din baza 10 in baza 2
    Input : n
    Output : nr
    '''
    b = 2
    p = 1
    nr = 0
    while n > 0:
        nr = nr + ( n % b) * p
        n= n / b
        p = p * 10
    return nr

def get_n_choose_k(n: int , k: int):
    '''
    Calculeaza combinari de n luate cate k
    Input: k,n
    x= n!
    y=k!
    z= (n-k)!
    Output:rez
    '''
    x=1
    y=1
    z=1

    for i in range (1,n):
        x = x * i
    for i in range (1,k):
        y = y * i

     dif=n-k
    for i in range (1,dif):
        z = z * i
    rez = ( x / (y * z))
        return rez

def test_is_palindrome():
    assert is_palindrome(2332) == True
    assert is_palindrome(9874) == False
    assert is_palindrome(567765) == True
    assert is_palindrome(23) == False

def test_get_base_2():
    assert test_get_base_2(2567) == 101000000111
    assert test_get_base_2(5677) == 1011000101101
    assert test_get_base_2(8000) == 1111101000000 

def test_get_n_choose_k():
    assert test_get_n_choose_k(5,7) == 21