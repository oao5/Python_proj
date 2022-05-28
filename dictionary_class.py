import math

from Jesus_new.Itamar.HW.HW3 import class_linklist as LinkList


class Dictionary:

    def __init__(self, mod):
        self.__counter = 0
        self.__mod = mod
        self.__dict_object = [None for _ in range(mod)]
        self.__alpha = 0

    def set(self, key, value):
        self.__counter += 1
        temp = None
        for n in range(self.__mod):
            check = self.__dict_object[n]
            if isinstance(check, LinkList.LinkedList):
                if self.__dict_object[n].len() > self.__alpha:
                    self.__alpha = self.__dict_object[n].len()
        location = hash(key) % self.__mod
        part = LinkList.LinkedList(key, value)
        list_in_location = self.__dict_object[location]
        if list_in_location is None:  # Scenario 1
            self.__dict_object[location] = part
        elif part.key == self.__dict_object[location].key:  # scenario 2
            self.__dict_object[location].value = part.value
            self.__counter -= 1
            self.__alpha -= 1
        else:
            while list_in_location is not None:  # scenario 3
                if part.key == list_in_location.key:
                    list_in_location.value = part.value
                    self.__counter -= 1
                    self.__alpha -= 1
                    break
                else:
                    temp = list_in_location
                    list_in_location = list_in_location.get_next()
            if list_in_location is None:
                temp.set_next(part)
        self.__reset()

    def __resize_prime(self,any_mod):
        if any_mod == 1:
            any_mod = 2
        any_mod = (any_mod * 2) + 1
        while True:
            max_divisor = math.floor(math.sqrt(any_mod))
            for d in range(2, max_divisor + 1):
                if any_mod % d == 0:
                    any_mod = any_mod + 2
                    break
            if d == max_divisor:
                break
        return any_mod

    def __reset(self):
        if self.__mod <= self.__alpha * 2:
            self.items()
            new_mod = self.__resize_prime(self.__mod * 2)
            save_items = self.items()
            self.__mod = new_mod
            new_dict = Dictionary(new_mod)
            for i in range(len(save_items)):
                new_dict.set(save_items[i][0], save_items[i][1])
            self.__dict_object = new_dict.__dict_object

    def __getitem__(self, item):
        return self.__dict_object[item]

    def __str__(self):
        output = ""
        for i in range(self.__mod):
            output += "\n=============================\n"
            output += f"In position {i} there exists the following value:\n"
            if isinstance(self.__dict_object[i], LinkList.LinkedList):
                output += str(self.__dict_object[i])
            else:
                output += f"None"
        return output

    def len(self):
        return self.__counter

    def get(self, key, default=None):
        location = hash(key) % self.__mod
        temp = self.__dict_object[location]
        while temp is not None:
            if temp.key == key:
                return temp.value
            else:
                temp = temp.next
        if temp is None and default is None:
            raise KeyError()
        else:
            return default

    def delete(self, key):
        location = hash(key) % self.__mod
        if self.__dict_object[location] is None:
            raise KeyError("Key not exist")
        head = self.__dict_object[location]
        sec = head.get_next()
        if head.key == key:
            self.__dict_object.pop(location)
            self.__dict_object.insert(location, sec)
        else:
            if head.get_next() is None:
                raise KeyError("Key not exist")
            while head.get_next() is not None:
                if head.key == key:
                    nod.set_next(sec)
                    break
                else:
                    nod = head
                    head = head.get_next()
                    sec = head.get_next()

    def keys(self):
        set_of_key = {None}
        for i in range(self.__mod):
            hot_list = self.__dict_object[i]
            while hot_list is not None:
                set_of_key.add(int(hot_list.key))
                hot_list = hot_list.get_next()
        set_of_key.discard(None)
        return set_of_key

    def items(self):
        items = []
        for i in range(self.__mod):
            temp = self.__dict_object[i]
            while temp is not None:
                tuple_the_creator = (temp.key, temp.value)
                items.append(tuple_the_creator)
                temp = temp.get_next()
        return items

    def values(self):
        values = []
        for i in range(self.__mod):
            temp = self.__dict_object[i]
            while temp is not None:
                values.append(temp.value)
                temp = temp.get_next()
        return values

    def exists(self, key):
        keys = self.keys()
        for i in range(len(keys)):
            if list(keys)[i] == key:
                return True
        return False

    def alpha(self):
        return self.__alpha

