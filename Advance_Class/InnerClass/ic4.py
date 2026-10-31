class Computer:
  def __init__(self):
    self.cpu=self.CPU()
    self.ram=self.RAM()

  class CPU:
    def process(self):
      print("CPU Processing...")

  class RAM:
    def store(self):
      print("RAM storing...")

computer=Computer()
computer.cpu.process()
computer.ram.store()