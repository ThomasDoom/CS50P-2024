name = input("File name: ").lower().strip()
name = name.split('.')[-1]

match name:
    case "gif" | "png" | "jpeg":
        print(f"image/{name}")
    case "jpg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "pdf" | "zip":
        print(f"application/{name}")
    case _:
        print("application/octet-stream")
