import gc
import time
import tracemalloc

tracemalloc.start()

print("Garbage Collection Enabled:", gc.isenabled())

class Student:

    def __init__(self, name):

        self.name = name
        self.reference = None

def create_objects():

    objects = []

    for i in range(10000):

        obj1 = Student("Student1")
        obj2 = Student("Student2")

        obj1.reference = obj2
        obj2.reference = obj1

        objects.append(obj1)
        objects.append(obj2)

    return objects

print("\nCreating objects...")

objects = create_objects()

print("Objects created successfully!")

current, peak = tracemalloc.get_traced_memory()

print("\nMemory Before Garbage Collection:")
print("Current Memory:", current)
print("Peak Memory:", peak)

del objects

start_time = time.time()

collected = gc.collect()

end_time = time.time()

current, peak = tracemalloc.get_traced_memory()

print("\nGarbage Collection Results:")

print("Objects Collected:", collected)

print("Memory After Garbage Collection:")
print("Current Memory:", current)
print("Peak Memory:", peak)

print(
    "\nGarbage Collection Time:",
    end_time - start_time,
    "seconds"
)

tracemalloc.stop()

print("\nGarbage Collection Experiment Completed!")
