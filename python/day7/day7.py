from dataclasses import dataclass
from typing import List

def load_input_text():
    for row in open("python/day7/day-7-input.txt", "r"):
        r = row.strip().split("contain")
        bag = r[0].strip()
        inside = r[1].split(",")
        yield bag, [i.strip().replace(".","") for i in inside]

def fake_lemmatisation(input_rows):
    for bag, inside in input_rows:
        bag = bag.replace("bags","").strip()
        inside = [i.replace("bags","").strip() for i in inside]
        inside = [i.replace("bag","").strip() for i in inside]
        inside = [i.replace("no other","").strip() for i in inside]
        inside = [i for i in inside if i]
        yield bag, inside

def remove_numbers_from_bags(lemmatised_input):
    for bag, inside in lemmatised_input:
        new_inside = []
        for i in inside:
            i = ''.join([l for l in i if not l.isdigit()]).strip()
            new_inside.append(i)
        yield bag, new_inside

def build_dict_of_bags(lemmatised_input):
    bags = {}
    for bag, inside in lemmatised_input:
        bags[bag] = inside

    return bags

def invert_dict_of_lists(dict_of_bags):
    inverted_dict = {}
    for k, v in dict_of_bags.items():
        for x in v:
            inverted_dict.setdefault(x,[]).append(k)
    return inverted_dict

def find_allowable_bag(bag_can_hold, bag_to_search_for):
    all_bag_types = list(bag_can_hold.keys())

    total = 0
    for bag in all_bag_types:
        total += can_contain_bag(bag_to_search_for, bag_can_hold, bag)

    return total


def can_contain_bag(bag_to_search_for, bag_can_hold_dict, bag_being_searched):
    if bag_to_search_for in bag_can_hold_dict[bag_being_searched]:
        # this bag can hold it directly
        return True
    if not bag_can_hold_dict[bag_being_searched]:
        # this bag can't hold anything
        return False
    # by here the bag must be able to hold something
    # but it can't hold our bag directly.
    # so we inspect its children!
    for bag in bag_can_hold_dict[bag_being_searched]:
        if can_contain_bag(bag_to_search_for, bag_can_hold_dict, bag):
            return True
    else:
        return False
        



if __name__ == "__main__":
    i = load_input_text()
    i = fake_lemmatisation(i)
    i = remove_numbers_from_bags(i)
    bag_can_hold = build_dict_of_bags(i)
    # bag_can_be_held_by = invert_dict_of_lists(bag_can_hold)
    print(find_allowable_bag(bag_can_hold, "shiny gold"))
