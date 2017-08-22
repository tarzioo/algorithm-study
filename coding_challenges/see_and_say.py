def see_and_say(s):
    output = []

    for item in s:
        i = 0
        result = ""
        while i < len(item):
            count = 1

            while i + count < len(item) and (item[i] == item[i + count]):
                count += 1
            result += str(count) + item[i]
            i += count

        output.append(result)

    return output
