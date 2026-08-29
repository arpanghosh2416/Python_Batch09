def my_function(title, *args, **kwargs):
    print(f"Title: {title}")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "John", "Doe", age=30, email="john@example.com")