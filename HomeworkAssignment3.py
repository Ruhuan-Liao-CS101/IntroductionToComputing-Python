# exercise 1

s1 = "Rocket Lab launches a Photon satellite. "
s2 = "The launch company said it has sent its first in-house-designed and -built operational satellite into orbit. " 
s3 = '''"First Light" was deployed to orbit on Rocket Lab's 14th Electron mission, ''' 
s4 = '''"I Can't Believe It's Not Optical," which lifted off from Launch Complex 1 in New Zealand on August 31. ''' 
s5 = "The mission's primary customer was a 100kg microsatellite for Capella Space."
print(len(s1+s2+s3+s4+s5))


# exercise 2

# using the index
s = "I love Python!"
print(s[7]+s[8]+s[9]+s[10]+s[11]+s[12]+s[13])

# using string slicing
print(s[7:])

# using string slicing with negative index
print(s[-7]+s[-6]+s[-5]+s[-4]+s[-3]+s[-2]+s[-1])