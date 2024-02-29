import nmap

def allports():

  begin = int(input("Begin of Range (or 0 to default): "))
  end = int(input("End of Range (or 0 to default): "))
  target = input("Target: ")

  if (begin == 0  and end == 0):
    begin = 0
    end = 65535
    
  scanner = nmap.PortScanner() 
    
  for i in range(begin,end+1): 
    
      
      res = scanner.scan(target,str(i)) 
    
      
      
      
      
      
      res = res['scan'][target]['tcp'][i]['state'] 

      print(f'port {i} is {res}.') 


def default():
  begin = 20
  end = 80
  target = input('Target: ')
    
  scanner = nmap.PortScanner() 
    
  for i in range(begin,end+1): 
    
      
      res = scanner.scan(target,str(i)) 
    
      
      
      
      
      
      res = res['scan'][target]['tcp'][i]['state'] 
    
      print(f'port {i} is {res}.') 



def menu():
  print(''' 
                    ___.-------.___
                _.-' ___.--;--.___ `-._
             .-' _.-'  /  .+.  \  `-._ `-.
           .' .-'      |-|-o-|-|      `-. `.
          (_ <O__      \  `+'  /      __O> _)
            `--._``-..__`._|_.'__..-''_.--'
                  ``--._________.--''


''')

  c = int(input('1)AllPorts; 2)DefaultPorts :'))

  if(c == 1):
    allports()
  
  elif(c == 2):
    default()

menu()