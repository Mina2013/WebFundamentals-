def my_dict():
    my_dict = {'My name is': 'Mina',
                'My age is':'36',
                'My country of birth is':'Algeria',
                'My favorite language is':'Python'}
    for key,data in sorted (my_dict.iteritems()):
        print key, data
my_dict()
###/****/Print any dictionary***/###
# def print_dictionary_values(dic):
#     for some_key, some_value in dic.iteritems():
#         print "My" + " " + some_key + " " + "is" + " " + str(some_value)
