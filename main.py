import codecs
import emoji # extensive use :)
import re as witchcraft
import heapq
from operator import itemgetter
import matplotlib.pyplot as plt

def extract_all_emojis(string):
    grp = witchcraft.findall('\s:(.*):', string)
    grp = "".join(grp).strip().split(":")
    for item in grp:
        if item == "" or item == " ":
            grp.remove(item)
    return [str(target) for target in grp]

def sanitize(filepath):
    sanitized_list = []
    # Clean all lines that contain 'media omitted'
    # Clean all lines that do not contain :<something>:
    with codecs.open(filepath, encoding='utf-8') as f:
        for line in f:
            line = emoji.demojize(line)

            # Remove all date and time information
            line = witchcraft.sub('^(.*\s)[-]+\s','', line)

            # Check if message contains an Emoji:
            is_emoji = len(witchcraft.findall('\:(.*)\:', line))

            # Check media messages:
            is_media = len(witchcraft.findall('\<(.+)\>', line))

            if is_media or not is_emoji:
                continue
            else:
                line = extract_all_emojis(line)
                [sanitized_list.append(item) for item in line]

    return sanitized_list

def separate_emojis(sanitized_line_list):
    emoji_tracker = {}
    for item in sanitized_line_list:
        if item in emoji_tracker:
            emoji_tracker[item] += 1
        else:
            emoji_tracker[item] = 0
    return emoji_tracker

def get_max_values(n, input_dict):
    max_items = heapq.nlargest(n, input_dict.items(), key=itemgetter(1))
    maximi = dict(max_items)
    return(maximi)

if __name__ == "__main__":
    fp = sanitize('data/wa_log.txt')
    tracking_dictionary = separate_emojis(fp)
    max_emojis = get_max_values(10 ,tracking_dictionary)
    plt.figure()
    height = []
    x_axis = []
    for element in list(max_emojis.keys()):
        element = ":" + element + ":"
        x_axis.append(emoji.emojize(element))

    for key in max_emojis.keys():
        height.append(max_emojis[key])
    plt.bar(x_axis, height)
    plt.show()

