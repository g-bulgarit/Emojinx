import codecs
import emoji # extensive use :)
import re as witchcraft


#\<(.+)>|\:(.*):  #<media omitted> or :smh:

def sanitize(filepath):
    sanitized_list = []
    # Clean all lines that contain 'media omitted'
    # Clean all lines that do not contain :<something>:
    with codecs.open(filepath, encoding='utf-8') as f:
        for line in f:
            line = emoji.demojize(line)

            # Remove all date and time information
            line = witchcraft.sub('^(.*\s)[-]+\s','', line)

            # Check media messages:
            is_emoji = len(witchcraft.findall('\:(.*)\:', line))
            is_media = len(witchcraft.findall('\<(.+)\>', line))
            if is_media or not is_emoji:
                continue
            else:
                sanitized_list.append(line)

    return sanitized_list

def separate_emojis(sanitized_line_list):
    emoji_tracker = {}
    return emoji_tracker


if __name__ == "__main__":
    fp = sanitize('data/wa_log.txt')
    print(fp)
    separate_emojis(fp)
    pass
