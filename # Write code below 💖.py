# Write code below 💖
g=0
r=0
h=0
s=0
print('Do you like Dawn or Dusk?')
ans = int(input('enter a bumber 1-2:'))
if ans==1:
  g=g+1
  r=r+1
elif ans==2:
  h=h+1
  s=s+1
else:
  print("wrong input")
print('When I’m dead, I want people to remember me as:')
ans = int(input('enter a bumber 1-4:'))
if ans ==1:
  h=h+2
elif ans ==2:
  s=s+2
elif ans==3:
  r=r+2
elif ans==4:
  g=g+2
else:
  print("wrong input")
print('Which kind of instrument most pleases your ear?')
ans = int(input('enter a bumber 1-4:'))
if ans ==1:
  s=s+4
elif ans ==2:
  h=h+4
elif ans==3:
  r=r+4
elif ans==4:
  g=g+4
else:
  print("wrong input")
if g>=h and g>=r and g>=s:
  print("Gryffindor")
elif h>=r and h>=s:
  print("Hufflepuff")
elif r>=s:
  print("Ravenclaw")
else:
  print('Slytherin')