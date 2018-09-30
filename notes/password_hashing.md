# Password Hashing

## Hashing Passwords

``` python
>> from werkzeug.security import generate_password_hash
>>> hash = generate_password_hash("MyPassword")
>>> hash
'pbkdf2:sha256:50000$R3VN68hP$cf04eb3427bab6e930add4b41b2829ea19808118d668a20af9610081a2b9b9af'
>>> hash2 = generate_password_hash("MyPassword")
>>> hash2
'pbkdf2:sha256:50000$yLNvCAJM$0167fdff17df4634c0f58baf53c3a9f2a615303ce1d25a22453df329d8c7c8dc'
```

## Checking Password Hashes

``` python
>>> from werkzeug.security import check_password_hash
>>> check_password_hash(hash, 'MyPassword')
True
>>> check_password_hash(hash, 'MyPassword2')
False
>>> check_password_hash(hash2, 'MyPassword')
True
>>> check_password_hash(hash2, 'sdfsdfsfd')
False
>>>
```