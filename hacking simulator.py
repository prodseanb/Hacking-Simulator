# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:44:23 2021
Hacking simulator - A mini hacking simulator game using the cmd module. 
Goal: Hack into 4 user accounts, delete a document. 
To access a user account, you will find a password stored somewhere in a text file. 
You will also need a username, also stored in a text file. The password consists of random strings,
although, it also contains a series of clues within the strings. To advance to the next level/user, you will find a
text file containing the next password required to access the next user. 
@author: sean bachiller
"""
from cmd import Cmd
import time




myDirectories = {"Users" : "", "Logs" : "", "bin" : "" }
binDirectory = {"bandit.txt" : "", "user1.txt" : "", "random" : ""}

myUsers = {"rosem" : "", "chrisk" : "", "elonm" : "", "dinac" : ""}


class myTerminal(Cmd):
    user_doc = 'user_doc'
    user2_doc = 'user2_doc'
    user3_doc = 'user3_doc'
    user4_doc = 'user4_doc'
    
    success_delete = ''
    success_delete2 = ''
    success_delete3 = ''
    success_delete4 = ''
    
    prompt = 'Anonymous@SecureLine> '
    intro = """Welcome. This is a SecureLine server for BigTech Industries.\n
               You have 4 targets.\n
               Your goal is to access each user's file through a login portal.\n
               You will need a username and a password to login to an account.\n
               Once you have logged in, delete the document in the user's directory to advance to the next level.\n
               Good luck.\n
               HINT: Type ? to list commands\n"""
    
    
    def do_ls(self, line):
        "List directories."
        if myTerminal.prompt == 'Anonymous@SecureLine> ':
            for key, value in myDirectories.items(): #home directory contents
                print(key, value)
        elif myTerminal.prompt == 'Anonymous@SecureLine\\Bin> ':
            for key, value in binDirectory.items(): #bin contents
                print(key, value)
        elif myTerminal.prompt == 'Anonymous@SecureLine\\Logs> ':
                print('logs.txt')
        elif myTerminal.prompt == 'Anonymous@SecureLine\\Users> ': 
            for key, value in myUsers.items():
                print(key, value)
        

        elif ( #if user is logged in and have not yet deleted the document
                myTerminal.success_delete == '' and 
                myTerminal.prompt == 'elonm@SecureLine> ' 
                 ):
            print(myTerminal.user_doc)
            
        elif (myTerminal.success_delete == 'Successfully deleted \'user_doc\' file.' and
              myTerminal.prompt == 'elonm@SecureLine> ' 
               ):
            print('lvlpass.txt') #Congrats - advance to the next user - contains next user password.
            
        elif ( #if user is logged in and have not yet deleted the document
                myTerminal.success_delete4 == '' and 
                myTerminal.prompt == 'rosem@SecureLine> ' 
                 ):
            print(myTerminal.user4_doc)
      
        elif (myTerminal.success_delete4 == 'Successfully deleted \'user4_doc\' file.' and
              myTerminal.prompt == 'rosem@SecureLine> ' 
               ):
            print('lvl4pass.txt')        
        
        elif ( #if user is logged in and have not yet deleted the document
                myTerminal.success_delete3 == '' and 
                myTerminal.prompt == 'chrisk@SecureLine> ' 
                 ):
            print(myTerminal.user3_doc)
      
        elif (myTerminal.success_delete3 == 'Successfully deleted \'user3_doc\' file.' and
              myTerminal.prompt == 'chrisk@SecureLine> ' 
               ):
            print('lvl3pass.txt') #Congrats - advance to the next user - contains next user password.
            
        elif ( #if user is logged in and have not yet deleted the document
                myTerminal.success_delete2 == '' and 
                myTerminal.prompt == 'dinac@SecureLine> ' 
                 ):
            print(myTerminal.user2_doc)
           
        elif (myTerminal.success_delete2 == 'Successfully deleted \'user2_doc\' file.' and
              myTerminal.prompt == 'dinac@SecureLine> ' 
               ):
            print('lvl2pass.txt')        #Congrats - advance to the next user - contains next user password.
            
            
        elif ( #if user tries to access the directory without logging in
                myTerminal.prompt == 'Anonymous@SecureLine\\Users\\rosem> ' 
                    or myTerminal.prompt == 'Anonymous@SecureLine\\Users\\chrisk> '
                    or myTerminal.prompt == 'Anonymous@SecureLine\\Users\\elonm> '
                    or myTerminal.prompt == 'Anonymous@SecureLine\\Users\\dinac> '
                    
                    ):
                print("Permission denied: You do not have access to this directory. Login to a SecureLine account associated with this user.")
                
                
    #DELETE FILE
    def do_rm(self, args):
        "Delete files/folders: rm <filename>"
        if  myTerminal.prompt == 'elonm@SecureLine> ' and args == 'user_doc':
            myTerminal.success_delete = 'Successfully deleted \'user_doc\' file.'
            print(myTerminal.success_delete)
            
        elif  myTerminal.prompt == 'rosem@SecureLine> ' and args == 'user4_doc':
            myTerminal.success_delete4 = 'Successfully deleted \'user4_doc\' file.'
            print(myTerminal.success_delete4)
            
        elif  myTerminal.prompt == 'chrisk@SecureLine> ' and args == 'user3_doc':
            myTerminal.success_delete3 = 'Successfully deleted \'user3_doc\' file.'
            print(myTerminal.success_delete3)
                
        elif  myTerminal.prompt == 'dinac@SecureLine> ' and args == 'user2_doc':
            myTerminal.success_delete2 = 'Successfully deleted \'user2_doc\' file.'
            print(myTerminal.success_delete2)
            
        
        
            
    def do_EOF(self, line): #exit
        return True
    
    def postloop(self): #print command info using ?. e.g. ? ls
        print
    
    def do_cat(self, args): 
        "Read the contents of a file: cat <file>"
        if args == 'logs.txt' and myTerminal.prompt == 'Anonymous@SecureLine\\Logs> ':
            # (IGNORE) random log text
            time.sleep(0.2)
            f = open('logs1.txt', 'r') #random log text
            log_contents = f.read()
            print(log_contents)
            f.close()
        elif args == 'user1.txt' and myTerminal.prompt == 'Anonymous@SecureLine\\Bin> ':
            time.sleep(0.2)
            f = open('user1.txt', 'r') #contains usernames
            user1_contents = f.read()
            print(user1_contents)
            f.close()
        elif args == 'bandit.txt' and myTerminal.prompt == 'Anonymous@SecureLine\\Bin> ':
            time.sleep(0.2)
            f = open('bandit.txt', 'r') #contains a password
            bandit_contents = f.read()
            print(bandit_contents)
        
        elif (args == 'lvlpass.txt' and myTerminal.prompt == 'elonm@SecureLine> ' 
              and myTerminal.success_delete == 'Successfully deleted \'user_doc\' file.'):
            
            print('pInternPrtPN36QITSp3EQaw936yaFoF')
            
        elif (args == 'lvl2pass.txt' and myTerminal.prompt == 'dinac@SecureLine> ' 
              and myTerminal.success_delete2 == 'Successfully deleted \'user2_doc\' file.'):
            print('dopnAYKhQqualiYNgjWxGoRMb5luKopn')
            
        elif (args == 'lvl3pass.txt' and myTerminal.prompt == 'chrisk@SecureLine> '
              and myTerminal.success_delete3 == 'Successfully deleted \'user3_doc\' file.'):
            print('koReBOKuIDCTOwhWk7jZC0RTdopnAYKh')
            
        elif (args == 'lvl4pass.txt' and myTerminal.prompt == 'rosem@SecureLine> ' 
              and myTerminal.success_delete4 == 'Successfully deleted \'user4_doc\' file.'):
            print('Congratulations! You have successfully sabotaged BigTech Industries. Type EOF to terminate the program.')
    
    
    
    
    def do_cd(self, args): 
        "Change remote working directory: cd <path>"
        if args.lower() == 'users':
            myTerminal.prompt = 'Anonymous@SecureLine\\Users> ' #Change prompt
            
            #cd / back into the home directory, prevents changing back into default prompt when logged in.
        elif (args == '/' and myTerminal.prompt == 'Anonymous@SecureLine\\Users> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Logs> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Bin> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Users\\rosem> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Users\\elonm> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Users\\chrisk> ' or
              myTerminal.prompt == 'Anonymous@SecureLine\\Users\\dinac> '):
            
                myTerminal.prompt = 'Anonymous@SecureLine> '
        elif args.lower() == 'logs': #Change prompt
            myTerminal.prompt = 'Anonymous@SecureLine\\Logs> '
        elif args.lower() == 'bin': #Change prompt
            myTerminal.prompt = 'Anonymous@SecureLine\\Bin> '
            
        #Users subdirectory
        elif args == 'rosem' or args.lower() == 'users/rosem':
          
          myTerminal.prompt = 'Anonymous@SecureLine\\Users\\rosem> '
          
        elif args == 'chrisk' or args.lower() == 'users/chrisk':
          
          myTerminal.prompt = 'Anonymous@SecureLine\\Users\\chrisk> '
          
        elif args == 'elonm' or args.lower() == 'users/elonm':
          
          myTerminal.prompt = 'Anonymous@SecureLine\\Users\\elonm> '
          
        elif args == 'dinac' or args.lower() == 'users/dinac':
          
          myTerminal.prompt = 'Anonymous@SecureLine\\Users\\dinac> '
          
    
    
    def do_login(self, line):
        "Access user directories through a SecureLine account."
        login = input('login as: ')
        if login == 'elonmac432432':
            password = input('password: ')
            if password == 'bodatab9jbbUNNfktd78OOadminOltut':
                
                myTerminal.prompt = 'elonm@SecureLine> ' #if username and password are valid, change the prompt.
    
            else:
                print('Invalid password.')
     
                
        elif login == 'dinacdum12':
            password = input('password: ')
            if password == 'pInternPrtPN36QITSp3EQaw936yaFoF':
                
                myTerminal.prompt = 'dinac@SecureLine> ' #if username and password are valid, change the prompt.
            else:
                print('Invalid password.')

    
        elif login == 'christoking34':
            password = input('password: ')
            if password == 'dopnAYKhQqualiYNgjWxGoRMb5luKopn':
              
                myTerminal.prompt = 'chrisk@SecureLine> ' #if username and password are valid, change the prompt.
            else:
                print('Invalid password.')
    
    
        elif login == 'rosemsan2000':
            password = input('password: ')
            if password == 'koReBOKuIDCTOwhWk7jZC0RTdopnAYKh':
                
                myTerminal.prompt = 'rosem@SecureLine> ' #if username and password are valid, change the prompt.
                
            else:
                print('Invalid password.')
        
        else:
               print('Invalid username.')
               
               
               
    def do_logout(self, line):
        "Log out of a user account."
        if (myTerminal.prompt == 'elonm@SecureLine> ' or myTerminal.prompt == 'dinac@SecureLine> '
            or myTerminal.prompt == 'chrisk@SecureLine> ' or myTerminal.prompt == 'rosem@SecureLine> '):
            
            myTerminal.prompt = 'Anonymous@SecureLine> ' #Back to default prompt when logged out
            
if __name__ == '__main__':
    myTerminal().cmdloop()