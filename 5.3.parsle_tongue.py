def find_secret_messages(file_path, chunk_size=1024):
    secret_messages = []
    current_word = ""
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            for byte in chunk:
                char = chr(byte)
                if 'a' <= char <= 'z':
                    current_word += char
                elif char == '!':
                    if len(current_word) >= 5:
                        secret_messages.append(current_word + '!')
                    current_word = ""
                else:
                    current_word = ""

    return secret_messages

messages = find_secret_messages('logo.jpg')
print("המסרים הסודיים שנמצאו:")
for msg in messages:
    print(msg)