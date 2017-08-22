def print_k_words_from_chars(char_list, prefix, k):
    print k
    if k == 0:
        print "---- prefix is----", prefix
        return

    for i in range(len(char_list)):
        print "i is", i
        new_prefix = prefix + char_list[i]
        print "new prefix is", new_prefix
        print_k_words_from_chars(char_list, new_prefix, k-1)
        