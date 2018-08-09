# by the time I'm writing this comment in Aug 2018 I don't remember why or when I wrote it
# but I'm pretty sure I never finished it because I realized none of my friends new enough
# computer skills to be able to take this quiz in the first place and so I had no audience
# so that's why this has a few syntax errors that will never be resolved. sorry to  my fans.


print('''
Ever wondered what kind of NCFCAer you are? Hit space to take this quiz and fin out.
''')
#starting quiz
user_input = input()
#determining class
if(user_input == " "):
    print("""
        Are you Rebecca Murch or Sarah Cox?
            a) yes
            b) no
        Enter 'a' or 'b' to choose.""")
    user_input = input()
    while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):   
		print("Error: enter 'a' or 'b'")
		user_input = input("Enter 'a' or 'b' to choose.")
        #RESULT == IO QUEEN
        if user_input in ("A", "a"):
            print("""
            You are: IO QUEEN:
            You slay at IO and everyone thinks you're amazing. Congrats!
            """)
            done = True
        #determining age
        elif user_input in ("B", "b"):
            print("""
            Were you the youngest you could be when you started NCFCA?
                a) yes
                b) no
            Enter 'a' or 'b' to choose.
            """)
        user_input = input()
        while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
    		print("Error: enter 'a' or 'b'")
    		user_input = input("Enter 'a' or 'b' to choose.")
            #determining level of caring for little kids
            if  user_input in ("A", "a"):
                print("""
                Do you care how you place?
                    a) yes
                    b) it is what it is
                    c) I couldn't care less
                Enter 'a' 'b' or 'c' to choose.
                """)
                user_input = input()
                while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B") and (user_input != 'c') and (user_input != 'C')):
            		print("Error: enter 'a' 'b' or 'c'")
            		user_input = input("Enter 'a' 'b' or 'c' to choose.")
                #determining class of child
                if user_input in ("A", "a")
                    print("""
                    Have you ever won a tournament?
                        a) yes
                        b) no
                    Enter 'a' or 'b' to choose.
                    """)
                    user_input = input()
                	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                		print("Error: enter 'a' or 'b'")
                		user_input = input("Enter 'a' or 'b' to choose.")
                    #Result == CHILD PRODIGY
                    if user_input in ("A", "a"):
                		print("""
                        You got: Child Prodigy
                        You've probably had older siblings in the league which is great because people were probably asking you for info on debate cases since back when you were a wee timer and now you're a prodigy.
                        You will probably be famous someday as 'the kid that won everything'
                        """)
                		done = True
                    #Result == Born 'n' Bred NCFCAer
                	elif user_input in ("B", "b"):
                		print("""
                		You got: Born 'n' Bred NCFCAer
                        You've been around for a while and you're going places. You may not have won a tournament, but you're probably a killer NCFCAer anyway.
                		""")
                        done = True
                #Result == LOWKEY NCFCAer
                elif user_input in ("B", "b"):
                    print("""
                    You are: Lowkey NCFCAer
                    You care a little, but you're probably just in it for the lolz and the memes
                    """)
                    done = True
                #Result == My Mom Made Me Do it
                elif user_input in ("C", "c"):
                    print("""
                    You are: 'My Mom Made Me Do it'
                    The name says it all.
                    You're really only doing NCFCA to check it off on your high school transcript because your mom made you do it.
                    """)
                    done = True
            #determining level of caring for older kids
            elif user_input in ("B", "b"):
                print("""
                Do you care how you place?
                    a) yes
                    b) it is what it is
                    c) I couldn't care less
                Enter 'a' 'b' or 'c' to choose.
                """)
                user_input = input()
                while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B") and (user_input != 'c') and (user_input != 'C')):
            		print("Error: enter 'a' 'b' or 'c'")
            		user_input = input("Enter 'a' 'b' or 'c' to choose.")
                #determining debater or nah
                if user_input in ("A", "a"):
                    print("""
                    Do you do debate?
                        a) yes
                        b) no
                    Enter 'a' or 'b' to choose.
                    """)
                    user_input = input()
                	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                		print("Error: enter 'a' or 'b'")
                		user_input = input("Enter 'a' or 'b' to choose.")
                    #Determining Debate Intensity
                    if user_input in ("A", "a"):
                        print("""
                        Is every round life or death?
                            a) yes
                            b) no
                        Enter 'a' or 'b' to choose.
                        """)
                        user_input = input()
                    	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                    		print("Error: enter 'a' or 'b'")
                    		user_input = input("Enter 'a' or 'b' to choose.")
                        #Determining Debate and Speech Intensity
                        if user_input in ("A", "a"):
                            print("""
                            How many speeches do you do?
                                a) none / only limited prep
                                b) a few
                                c) ALL THE ONES I CAN
                            Enter 'a' 'b' or 'c' to choose.
                            """)
                            user_input = input()
                        	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                        		print("Error: enter 'a' or 'b'")
                        		user_input = input("Enter 'a' 'b' or 'c' to choose.")
                            #Determining if you have a life
                            if user_input in ("A", "a"):
                                print("""
                                Do you do a sport besides debate?
                                    a) yes
                                    b) no
                                Enter 'a' or 'b' to choose.
                                """)
                                user_input = input()
                            	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                            		print("Error: enter 'a' or 'b'")
                            		user_input = input("Enter 'a' or 'b' to choose.")
                                #Result == "my other debate box is a gym bag"
                                if user_input ("A", "a"):
                                    print("""
                                    You are: The "My other debate box is a gym bag" NCFCAer
                                    Debate is cool and all, but it's not your whole life. Congrats, you're well rounded!
                                    """)
                                    done = True
                                #Result == DEBATE IS THE NAME OF THE GAME
                                elif user_input ("B", "b"):
                                    print("""
                                    You are: The "DEBATE IS THE NAME OF THE GAME" NCFCAer
                                    Debate is probably THE most important activity in your life - except for maybe Chorale.
                                    """)
                                    done = True
                            #Result == Do or Die Debater
                            elif user_input in ("B", "b"):
                                print("""
                                You are: Do or Die Debater
                                Debate is important to you, and you're pretty competitive, but you might actually have a life outside of NCFCA.
                                """)
                                done = True
                            #Result == Ironman/Marathoner
                            elif user_input in ("B", "b"):
                                print("""
                                You are: Ironman/Marathoner
                                YOU GO ALL IN, BABY! You might have had a life and activities out of NCFCA, but if you did, you've definitely quit all of it by now.
                                """)
                                done = True
                        #Result == LOWKEY NCFCAer
                        elif user_input in ("B", "b"):
                            print("""
                            You are: Lowkey NCFCAer
                            You care a little, but you're probably just in it for the lolz and the memes
                            """)
                            done = True
                    elif user_input in ("B", "b"):
                        print("""
                        How many speeches do you do?
                            a) a feW
                            b) AS MANY AS I CAN
                        Enter 'a' or 'b' to choose.
                        """)
                        user_input = input()
                    	while ( (user_input != "a") and (user_input != "A") and (user_input != "b") and (user_input != "B")):
                    		print("Error: enter 'a' or 'b'")
                    		user_input = input("Enter 'a' or 'b' to choose.")
                        #Result == I have a life
                        if user_input in ("A", "a"):
                            print("""
                            You are: The "I have a life" NCFCAer
                            Congratulations! You have a life outside of NCFCA! Good job.
                            """)
                            done = True
                        #Result == Ironman/Marathoner
                        elif user_input in ("B", "b"):
                            print("""
                            You are: Ironman/Marathoner
                            YOU GO ALL IN, BABY! You might have had a life and activities out of NCFCA, but if you did, you've definitely quit all of it by now.
                            """)
                            done = True
                #Result == LOWKEY NCFCAer
                elif user_input in ("B", "b"):
                    print("""
                    You are: Lowkey NCFCAer
                    You care a little, but you're probably just in it for the lolz and the memes
                    """)
                    done = True
                #Result == My mom made me do it
                elif user_input in ("C", "c"):
                    print("""
                    You are: 'My Mom Made Me Do it'
                    The name says it all.
                    You're really only doing NCFCA to check it off on your high school transcript because your mom made you do it.
                    """)
                    done = True
