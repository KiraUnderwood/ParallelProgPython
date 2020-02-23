#!/usr/bin/env python3
""" Two hungry people, anxiously waiting for their turn to take soup """

import threading

slowcooker_lid = threading.Lock()  # protect variable lock
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)  # condit variable. aquire lock heck on condition, then wait on condition, if is true

def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid: # context manager to lock the lid
            while (person_id != (soup_servings % 5)) and (soup_servings > 0): # check if it's your turn CONDITION
                print('Person', person_id, 'checked... then put the lid back.')
                soup_taken.wait()  # place where you should wait untill signaled to wait on condition again
            if (soup_servings > 0):
                soup_servings -= 1 # it's your turn; take some soup!
                print('Person', person_id, 'took soup! Servings left:', soup_servings)
                soup_taken.notify_all()  # to wake up all of the waiting threads

if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=hungry_person, args=(i,)).start()
