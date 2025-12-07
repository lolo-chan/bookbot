def count_words(string):
    return len(string.split())

def count_characters(string):
    count_dict = {}
    for i in string:
        if i.lower() in count_dict:
            count_dict[i.lower()] += 1
        else:
            count_dict[i.lower()] = 1
    return count_dict

def sort_on(items):
    return items["num"]
    
def sort_counts(count_dict):
    sorted_list = []
    for i in count_dict:
        temp_dict = {"char": i, "num": count_dict[i]}
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

