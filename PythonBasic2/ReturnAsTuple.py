def imperial(cm):  # Returning multiple value will return as tuples
    inch = cm * 0.393700787
    foot = cm / 30
    temp_tuple = (inch, foot)
    # The following code produce exactly same result
    # return temp_tuple
    # return inch, foot
    return (inch, foot)


if __name__ == '__main__':
    print(imperial(30))
    a_tuple = imperial(30)
    print(a_tuple)
    # Multiple value assigning
    inch, foot = imperial(30)
    print(inch)
    print(foot)