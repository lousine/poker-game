from poker_logic import Poker

class Test_Poker:
    """This is the code to start poker game.   
    It gives you an opportunity to select the number of players.   
    The number of players varies between 2 and 7, as, traditionally, poker has been thought of as a game for 2 to 7 players. 
    """ 
    def main ():
        numPlayers = eval (input ("Number of players: "))
        while (numPlayers < 2 or numPlayers > 7):
            numPlayers = eval( input ("Number of players: "))
        a=int(numPlayers)
        print("\n")
        names= ["Gevorg", "Dan Bilzerian", "Lusine A", "Lusine Gh", "Yenok", "Gevorg 2", "Elon Musk"]
        b = "We have {} players: ".format(a)
        print(b)
        for i in range(a):
            print(i+1,names[i],end =". ")
        print("\n")
        game = Poker (numPlayers)
        game.play()  
        print("\n")
        for i in range(numPlayers):
            curPlayer=game.players[i]
            print ("Player "+ str(i+1) + " holds " , end="")
            game.Royal(curPlayer)
       
        pmax=max(game.list_t)
        imax=game.list_t.index(pmax)
        fin_winner= "\nPlayer {} wins!!! Congratulations,{}!".format(imax+1, names[imax])
        print (fin_winner)
    main()
