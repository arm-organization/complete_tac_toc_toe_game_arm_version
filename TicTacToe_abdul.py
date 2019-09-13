def tac_toc_game():
    i = 0
    a, b, c, d, e, f, g, h, k = '', '', '', '', '', '', '', '', ''

    def draw_board(a1, b1, c1, d1, e1, f1, g1, h1, k1):
        print('\n' * 100)
        print(f'  {a1}  ||  {b1}  ||  {c1}')
        print('------------------')
        print(f'  {d1}  ||  {e1}  ||  {f1}')
        print('------------------')
        print(f'  {g1}  ||  {h1}  ||  {k1}')

    while i < 6:
        i += 1
        # Player one +++++++++++++++++++++++++++++++++++++
        p1 = int(input('player 1  enter num from  1 - 9 :'))
        if p1 == 7:
            a = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 8:
            b = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 9:
            c = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 4:
            d = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 5:
            e = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 6:
            f = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 1:
            g = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 2:
            h = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p1 == 3:
            k = 'o'
            draw_board(a, b, c, d, e, f, g, h, k)
        else:
            break
        # checking winner++++++++++++++++++++++++++++++++
        if (a == 'o') and (b == 'o') and (c == 'o'):
            print('player 1  won ')
            break
        elif (d == 'o') and (e == 'o') and (f == 'o'):
            print('player 1  won ')
            break
        elif (g == 'o') and (h == 'o') and (k == 'o'):
            print('player 1  won ')
            break
        elif (a == 'o') and (d == 'o') and (g == 'o'):
            print('player 1  won ')
            break
        elif (b == 'o') and (e == 'o') and (h == 'o'):
            print('player 1  won ')
            break
        elif (c == 'o') and (f == 'o') and (k == 'o'):
            print('player 1  won ')
            break
        # checking steps +++++++++++++++++++++++++++++++++++++
        if i == 5:
            print(f' step no : {i}')
            print('Both winner')
            break

        # Player two +++++++++++++++++++++++++++++++++++++
        p2 = int(input('player 2 enter num from 1 - 9 :'))
        if p2 == 7:
            a = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 8:
            b = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 9:
            c = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 4:
            d = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 5:
            e = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 6:
            f = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 1:
            g = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 2:
            h = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        elif p2 == 3:
            k = 'x'
            draw_board(a, b, c, d, e, f, g, h, k)
        else:
            break
        # checking winner ++++++++++++++++++++++++++++++++
        if (a == 'x') and (b == 'x') and (c == 'x'):
            print('player 2  won ')
            break
        elif (d == 'x') and (e == 'x') and (f == 'x'):
            print('player 2  won ')
            break
        elif (g == 'x') and (h == 'x') and (k == 'x'):
            print('player 2  won ')
            break
        elif (a == 'x') and (d == 'x') and (g == 'x'):
            print('player 2  won ')
            break
        elif (b == 'x') and (e == 'x') and (h == 'x'):
            print('player 2  won ')
            break
        elif (c == 'x') and (f == 'x') and (k == 'x'):
            print('player 2  won ')
            break


choose_player = input('are you first player ? : ')
while True:
    if choose_player == 'yes':
        tac_toc_game()
        again_play = input('do you like to play again ?')
        if again_play == 'yes':
            tac_toc_game()
        else:
            print('good bye')
            break
    elif choose_player == 'no':
        print('ask your friend to start')
        tac_toc_game()
    else:
        break
