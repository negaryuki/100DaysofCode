# FileNotFound Error

try:
  file = open("file.text")
  a_dictioanary = {"key":"value"}
  print(a_dictioanary["abc"])
  
except FileNotFoundError:
  open("file.text","w")
  file.write("something")

except KeyError as error_message:
  print(f'there is no{error_message}')
  
else:
  content =file.read()
  print(content)
  
finally:
  file.close()
  print("File was closed")
 
#-------------------------------------------------------------

 # When to create our own exception and error
 
# Example: BMI calculator
# we will add an error that does not allow un reasonable heights

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
  raise ValueError(" Human Height should not be over 3 meters")

bmi = weight / height ** 2

print(bmi)

  


