import hashlib

password = input('Input the Password to Hash: ')

print('\nsha-1:\n')

setpass = bytes(password, 'utf-8')
hash_object = hashlib.sha1(setpass)
guess_pw = hash_object.hexdigest()
print(guess_pw)

print('\nMD5:\n')

setpass = bytes(password, 'utf-8')
hash_object = hashlib.md5(setpass)
guess_pw = hash_object.hexdigest()
print(guess_pw)

print('')
