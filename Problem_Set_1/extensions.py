filename = input('Enter the name of the file')
filename_lst = filename.split('.')
extension = filename_lst[-1].strip().lower()
if (extension == 'jpg'):
    print('image/jpeg')
elif(extension == 'jpeg'):
    print('image/jpeg')
elif(extension =='png'):
    print('image/png')
elif(extension =='gif'):
    print('image/gif')
elif(extension =='zip'):
    print('application/zip')
elif(extension =='pdf'):
    print('application/pdf')
elif(extension =='txt'):
    print('text/plain')
else:
    print('application/octet-stream')