# Generator Methods
'''
Special methods for advance control of generators:
- send(value): Sends a value to the generator and resumes its execution.
- close(): Closes the generator and raises a GeneratorExit exception inside it.
'''


def echo_gen():
  while True:
    received = yield
    print(f"Received: {received}")

gen = echo_gen()
# print(next(gen))  
next(gen)  # Start the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World

gen.close()  # Close the generator

# gen.send("This will raise an exception")  # Raises StopIteration exception


print()
def my_gen():
  try: #Raise Exception when the generator is closed
    yield "Start"
    yield "Middle"
    yield "End"
  finally: #Always execute this block when the generator is closed
    print("Generator is closing.")

gen = my_gen()
print(next(gen))  # Output: Start
print(next(gen))  # Output: Middle
print(next(gen))  # Output: End 
gen.close()  # Output: Generator is closing.