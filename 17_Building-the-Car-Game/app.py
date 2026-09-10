#   ___             ___                
#  / __|__ _ _ _   / __|__ _ _ __  ___ 
# | (__/ _` | '_| | (_ / _` | '  \/ -_)
#  \___\__,_|_|    \___\__,_|_|_|_\___|
                                     

is_started = False
while True:
  command = input("> ").lower()
  if command == "help":
      print("start - to start the car\nstop - to stop the car\nquit - to exit") 
  elif command == "start":
      if is_started:
          print("Car is already started")
      else:
          is_started = True
          print("Car Started...")
  elif command == "stop":
      if not is_started:
          print("Ca Is already stopped!")
      else:
          is_started = False
          print("Car Stopped")
  elif command == "quit":
      break
  else:
      print("Please Enter a Valid Command")