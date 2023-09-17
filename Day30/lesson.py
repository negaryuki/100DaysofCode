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

