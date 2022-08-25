Story = '''Marlin, a clown fish, is overly cautious with his son, Nemo,
 who has a foreshortened fin. When Nemo swims 
too
 close to the surface to prove himself, he is caught by a diver, and horrified Marlin must set out to find him. A blue reef fish named Dory 
  who has a really short memory  joins Marlin and complicates the encounters with sharks, jellyfish, and a host of ocean dangers. Meanwh
ile, Nemo plots his escape from a dentist's fish tank.'''


def check(s, find_story):
  # print(s.find(find_story))
  x = s.find(find_story)
  if x == -1:
    print("Your character isn't here.")
  else:
    print("Your character is at", x)
q = input("Who would you like to find?")

check(Story, q)
  
