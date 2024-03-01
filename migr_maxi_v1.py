import argparse
import json
import os
from pathlib import Path
import re

import pyjq
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    print("parser: ", parser)
    parser.add_argument('--path', type=dir_path)
    parser.add_argument('--keys', type=str)
    return parser.parse_args()


def dir_path(path):
    return path

args = parse_arguments()
path = args.path if args.path else os.path.dirname(os.path.realpath(__file__))
# Через это получаем путь. Если он не был передан в аргумент, то выдаст None в это значение, если был то выдаст путь.
# Так же добавил остановку скрипта если путь не валидный. Пример: --path=C:\\python\\ (Not work)


#testing
# Так же добавил остановку скрипта если путь не валидный. Пример: --path=C:\\python\\ (Not work)
#mb need this code:
#def dir_path(string):
#    if os.path.isdir(string):
#        return string
#    else:
#        raise NotADirectoryError(string)

#get path arg example
#if args.path:
#    path=args.path
#else:
#    path=os.path.dirname(os.path.realpath(__file__))

print("real_path:", os.path.dirname(os.path.realpath(__file__)))
print("path: ", path)
print("args",args)

with open(Path(path, 'config.json.dist'), encoding='utf-8') as file_dump:
    data_dist = json.load(file_dump)

with open(Path(path, 'config.json'), encoding='utf-8') as file_dump:
    data_config = json.load(file_dump)

with open(Path(path, 'config.json.dist'), encoding='utf-8') as file_dump:
    data_dist_bak = json.load(file_dump)

#print("data_dist_bak",data_dist_bak.keys())


# print("test data")
# print(data_dist_bak['chain_id'])
# val_test=data_dist_bak['chain_id']
# if isinstance(val_test, bool):
#    print("sssssssss1")
# elif isinstance(val_test, int):
#    print("2222")

# data_dist_bak = data_dist.copy() #is NOT work znd get BUG: data_dist_bak changed with data_sit
# print("data_dist_bak at the start", data_dist_bak)

# list=[]
# if list != []:
#    print("empty")
# else:
#    print("ss")

# list1=[1,2,3]
# print("len_list",len(list1))
# for i in range(1,len(list1)):
#    print(list1[i])

# len_list=[['shops', 0, 'region_id']]
# print("len_list")
# for i in len_list:
#    print(i)

# 0) testing data1 usage

# with open('1.json') as file_dump:
#    data1=json.load(file_dump)

# with open('2.json') as file_dump:
#    data2=json.load(file_dump)

# key="count"
# print("key")
# print(data1[key])
# key_for_replace=10
# print("key_for_replace:",key_for_replace)
# data1[key] = key_for_replace
# print("before")
# print(data1)

# data1[key] = 16
# print(data1[key])
# print(data1)

# data1[key] = "17"
# print("new_key")
# print(data1[key])
# print(data1)

# data1[key] = str(key_for_replace)
# print("after str")
# print(data1)

# list_test=['5M']
# list_test=[465]
# print("list_test:",list_test[0])
# print("type list_test is:", type(list_test))
# print("type list_test is:", type(list_test[0]))


# if isinstance(list_test[0],str):
#    print("string")
# else:
#    print("not str")

# list_test=[]
# print("type list_test is:", type(list_test))
# if len(list_test) == 0:
#    print("empty")
# print("len",len(list_test))


# print(data_dist_bak)
# print(data1)
# print(data1.items())
# new_data3 = data2
# path_var=
# variible="name"
# print(data_config['radius'])

# data1['name']="30"
# print(data1)

# print(data1[variible])
# variible2="count_var"
# variible3="count"
# var4="'count_var']['count']"
# print(data1['count_var']['count'])
# print(data1[variible2][variible3])

# data1['name']= "11"
# print(data1['name'])
# print(data1['parser_id'])

# 1) check that var, that was to be in olg config in doublequotes will be in bew confit in
# doublequotes to. But var type is string = work
# with open("config_new.json", "w") as out_data:
#    json.dump(data1, out_data, indent=2, separators=(',', ': '))

# 2) chech that var, that have type "dict" in old config migrate to new config without
# another changes = work
# dict_example=data1['temp']
# print(dict_example)

# with open('config_new.json') as file_dumpnew:
#    datanew=json.load(file_dumpnew)

# print(datanew)
# datanew['temp']=dict_example
# print(datanew)

# 3) check that i can save the path to inner_key in cpnfig in python_var
# and may get value this key, when i using varrible with PATH instead PATH to key
# = work, but only for first-level-keys. if i want use path-to-inner key, need more expression
# var_with_path="count_var"
# var_with_inner_path="inner_name"
# var_unites_two_path="[count_var][inner_name]"
# print('Hello')
# print(data1 (print(var_unites_two_path)))
# print(data1['count_var']['inner_name'])

# 4) check the get method #wokr
# inner_value=data1.get('count_var').get('inner_name') #work
# inner_value=data1.get('count_vars',[11,11,'00']) #if key not found, return [11,11,'00']
# print("AAA",inner_value)

# 5) loop with get recurse check and path - work
# inner_path_var=["count_var","inner_name"]
# print("inner_path= ",inner_path_var)
# iterate_data=data1
# print("runloop")

# for keys in inner_path_var:
#    iterate_data=iterate_data.get(keys)
#    print(iterate_data)

# 6) get path wint pyjq/ in bash it is: jq -c 'path(.. | .chat? // empty)' 1.json
# is work, but output is dict in any cases - is so wrong
# t=pyjq.all(
#    """
#    path(.. | .chat? // empty)
#    """, data1)

# print(t)

# 7) use another method to get path with pyjq. in forum is:
# "match = pyjq.all(f'.[]|select({query}==$value)', records, vars={"value": value})"
# work, but this method retun dict to
# but i can get first item in dict)

# match = pyjq.all(f'path(.. | .chat? // empty)', data1)
# print(match[0])

# 8) aand lets connect the received parts #work
# item_path=pyjq.all(
#    """
#    path(.. | .chat? // empty)
#    """, data1)

# print(item_path[0])

# iterate_data=data1
# for keys in (item_path[0]):
#    iterate_data=iterate_data.get(keys)
# print(iterate_data)

# 9) get all paths with pyjq #work
# all_paths=pyjq.all(
#    """
#    paths(scalars | true)
#    """, data1)

# print(all_paths)

# 10) rul all path loop and get all values in this path
# work, but python cant run get-vodule to path with doct ['source', 'excluded_params', 0]
# all_paths=pyjq.all(
#    """
#    paths(scalars | true)
#    """, data1)
# print(all_paths)

# for another_path in all_paths:
#    iterate_data=data1
#    for keys in another_path:
#        iterate_data=iterate_data.get(keys)
#    print("path=", another_path, "value=", iterate_data)

# _________next day

# 11) using loop with dict of path instead print(item_path) #work
# loop get all path wiyhout arrays and get their value
# but need more paths, also need arrays paths
# item_path=pyjq.all(
#    """
#    del(.. | arrays) | paths
#    """, data1)

# iterate_data = data1
# for path in item_path:
#    print(path)
#    iterate_data = data1
#    for keys in path:
#        print(keys)
#        iterate_data=iterate_data.get(keys)
#    print(iterate_data)

# 12) get dict with all path: aarays paths and paths without arrays
# modife the script - now hi not give object like "source"
# not_arrays_path=pyjq.all(
#    """
#    del(.. | select(type=="array")) | paths(scalars | true)
#    """, data1)
# print(not_arrays_path)

# only_arrays_path=pyjq.all(
#    """
#    path(..| select(type=="array"))
#    """, data1)
# print(only_arrays_path)
# all_path=not_arrays_path + only_arrays_path
# print(all_path)


# 13) set funk wich get value with path
# work only witj all_path varrible - 12 part
# func get all paths in "config_dist.json"

# def all_dist_paths_func(conf_dist_data):
#    not_arrays_path=pyjq.all(
#        """
#        del(.. | select(type=="array")) | paths(scalars | true)
#        """, conf_dist_data)
#    #print(not_arrays_path)

#    only_arrays_path=pyjq.all(
#        """
#        path(..| select(type=="array"))
#        """, conf_dist_data)
#    #print(only_arrays_path)

#    all_path=not_arrays_path + only_arrays_path
#    #print(all_path)
#    return (all_path)


# func get values witn the input_path

# def get_path_value_func(input_path, input_data):
#    iterate_data=input_data
#    for keys in input_path:

#        iterate_data = iterate_data.get(keys)
#    return (iterate_data)


# 14) set funk with check key exist
# work, func check thah each part of values from path is exist in config.json
# for example in ['source', 'region_id'] 'source' is exist in config.json and 'region_id'
# also is exist in config.json
# but not wokr without "all_dist_paths_func"

# def get_path_value_func(input_path, input_data):
#     iterate_data=input_data
#     for keys in input_path:
#         #check, that each element in path is exist in config.json return-keys, otherwice break loop
#         if keys in (iterate_data.keys()):
#             pass
#
#         else:
#             #print(input_path, "KEY_NOT_EXIST")
#             return("KEY_NOT_EXIST")
#
#         if (input_path.index(keys)) == (len(input_path)-1):
#             #print("PATH: ", input_path, "KEY_EXIST:")
#             print()
#         iterate_data = iterate_data.get(keys)
#     return (iterate_data)


# def get_path_value_func(input_path, input_data):
#    iterate_data=input_data
#    #print(input_path.index(input_path[-1]))
#    #print(input_path)
#    #print(input_path[-1])
#    for keys in input_path:
#        #print(keys)
#        #print(input_path.index(keys))
#        #print(iterate_data.keys())
#        #if (input_path.index(keys)) == input_path.index(input_path[-1]):
#            #print(iterate_data.keys())
#            #print(input_path[-1])


#        #check, that each element in path is exist in config.json return-keys, otherwice break loop
#        if keys in (iterate_data.keys()):
#            #print("KEY_EXIST")
#            print()
#        else:
#            print("PATH: ", input_path, "KEY_NOT_EXIST")
#            return("KEY_NOT_EXIST")
#            #break

#        if (input_path.index(keys)) == (len(input_path)-1):
#            print("PATH: ", input_path, "KEY_EXIST:")
#            #print(len(input_path))


#        iterate_data = iterate_data.get(keys)
#    return (iterate_data)


# 15) set funk which set the value "value_in_config" in cofig_new.json
# !!!bugs!!! - isinstance wrong udestand walues, if in confid values = false, isinstance thsink that is int type

# def set_value_with_path_func(input_path, input_value, input_data, str_flag):
#     #iterate_data=input_data
#     #print("input_path in set_value_with_path_func:", input_path)
#
#
#     for keys in input_path:
#         if (input_path.index(keys)) == (len(input_path)-1):
#
#             if str_flag == False:
#                 input_data[keys] = input_value
#             else:
#                 input_data[keys] = str(input_value)
#
#         else:
#             input_data = input_data.get(keys)
#     #print("value_setting_complete")
#     return ()


# 16) set run func with two configs: config.dist.json and config.json
#
# def run_func(dist_data_file, config_data_file, example_data):
#     #print("dist_data_file",dist_data_file)
#     #print("config_data_file", config_data_file)
#     not_exist_keys=[]
#     all_paths = all_dist_paths_func(dist_data_file)
#     for path in all_paths:
#         #print("path_in_run_func",path)
#
#         ## ---example block
#         # exchange path to str
#         exchange_need_path_in_bak = exchange_list_to_jq_path([path])
#         #print("exchange_need_path_in_bak:", exchange_need_path_in_bak)
#         # get value
#         value_in_bak_with_path = get_path_value_jq(exchange_need_path_in_bak, example_data)
#         #print("value_in_bak_with_path:", value_in_bak_with_path)
#         ## ---example block
#
#         if isinstance(value_in_bak_with_path[0], str):
#             input_str_flag=True
#         else:
#             input_str_flag=False
#
#         #print("input_str_flag",input_str_flag)
#
#         #    print("string in set_path_value_jq")
#         #    query = f'setpath([{path_one}];"{item_one}")'
#         #else:
#         #    query = f'setpath([{path_one}];{item_one})'
#         #    print("not str in set_path_value_jq")
#
#         #input_str_flag=False
#         ## ---example block
#
#
#         value_in_config = get_path_value_func(path, config_data_file)
#         #print(value_in_config[0])
#         if value_in_config == "KEY_NOT_EXIST":
#             print(path, "values not set!")
#             #not_exist_keys = not_exist_keys + path #not work
#             # work! method to create a list of lists
#             not_exist_keys.append(path)
#
#         else:
#             print("Will be set value:", value_in_config)
#             set_value_with_path_func(path, value_in_config, dist_data_file, input_str_flag)
#
#     #all not exisying path of keys
#
#     print("\n")
#     print("not_exist_keys in config.json:")
#     print(not_exist_keys)
#     for local_path in not_exist_keys:
#         print(local_path)
#     #print("dist_data_file end run func", dist_data_file)
#     #print("config_data_file end run func", config_data_file)
#
#     return ()


# 17) create logging, what key not find in config.json
# change logging logik:
# now funk "get_path_value_func" no print whats path not foun in config.json
# but "run_func" create list of list with all not found path and print his at the end of func


# 18) create func, that recursive find value of key
# def recursive_find_value(value_to_find, find_inside_data):
#     found = []
#     for keys, values in find_inside_data.items():
#         #print(keys)
#         if keys==value_to_find:
#             found.append(values)
#
#         elif isinstance(values, dict):
#
#             results = recursive_find_value(value_to_find, values)
#             for result in results:
#                 found.append(result)
#
#         elif isinstance(values, list):
#             for item_list in values:
#                 if isinstance(item_list, dict):
#
#                     another_result = recursive_find_value(value_to_find, item_list)
#                     for item_in_another_result in another_result:
#                         found.append(item_in_another_result)
#     #print("found",found)
#     return (found)


# 19) recursive_set_value #work

# def recursive_set_value(input_value, find_value, iterate_data):
#     # print(input_value)
#     global set_flag
#
#     for keys, values in iterate_data.items():
#         # print(keys)
#
#         if keys == find_value:
#
#             # print(set_flag)
#             if set_flag != True:
#                 # print(set_flag)
#                 iterate_data[keys] = input_value[0]
#                 set_flag = True
#
#             # found.append(values)
#
#         elif isinstance(values, dict):
#             # print("values", values)
#
#             recursive_set_value(input_value, find_value, values)
#
#         elif isinstance(values, list):
#             for item_list in values:
#                 # print(item_list)
#                 if isinstance(item_list, dict):
#                     # print("item_list:",item_list)
#                     recursive_set_value(input_value, find_value, item_list)


# 20)
# def all_path_wiht_key(inpyt_key, data):
#    query = f'path(.. | .{inpyt_key}? // empty)'
#    result = pyjq.all(query, data)
#    return(result)


# 21) check what path me need
# work only with func "all_path_wiht_key"
#
# def what_path_need(find_path, find_key, data):
#     set_path_list=find_path.split('.')
#     set_path_list.sort()
#     #print("set_list:", set_path_list)
#     list_of_correct_path=[]
#     for another_found_path in all_path_wiht_key(find_key,data):
#         #print("another_found_path",another_found_path)
#         new_list=[]
#         for item in another_found_path:
#             try:
#                 item = float(item)
#             except ValueError:
#                 #print("not a number\n")
#                 new_list.append(item)
#         new_list.sort()
#         #print("new_list",new_list)
#         #print("set_path_list",set_path_list)
#         if new_list == set_path_list:
#             #print("111")
#             #return(another_found_path)
#             list_of_correct_path.append(another_found_path)
#         #else:
#         #    print("222")
#     #return("PATH_AND_VALUE_NOT_FOUND (what_path_need)", "nedeed path:",find_path, "find key:", find_key)
#     #print("list_of_correct_path:",list_of_correct_path)
#     return(list_of_correct_path)


# 22) func that, get path as list and return path as jq string
#
# def exchange_list_to_jq_path(input_path):
#     # exchange all item in list to string #work
#     #print("input_path in exchange_list_to_jq_path",input_path)
#
#     #path_one=input_path[0]
#     #print("path_one in exchange_list_to_jq_path",path_one)
#
#     #new_list = []
#     return_list=[]
#     new_str=''
#
#     if len(input_path) != 0:
#
#         for path_one in input_path:
#             #print("path_one in exchange_list_to_jq_path",path_one)
#             new_list = []
#             for item in path_one:
#                 try:
#                     item = float(item)
#                     item = int(item)
#                     item = str(item)
#                     new_list.append(item)
#
#                 except ValueError:
#                     new_list.append(item)
#             #print(new_list)
#
#             new_str = ''
#             #print("new_str in loop",new_str)
#             for item in new_list:
#                 if item.isdigit():
#                     # print(item, "It's a number")
#                     if new_list.index(item) == 0:
#                         new_str = new_str + item
#                     else:
#                         new_str = new_str + "," + item
#                 else:
#                     item_in_doubleqoutes = f"\"{item}\""
#                     #print("item_in_doubleqoutes", item_in_doubleqoutes)
#                     if new_list.index(item) == 0:
#                         new_str = new_str + item_in_doubleqoutes
#                     else:
#                         new_str = new_str + "," + item_in_doubleqoutes
#                         # new_str = new_str+item_in_doubleqoutes
#             return_list.append(new_str)
#             #print("new_str", new_str)
#     else:
#         print("LIST_IS_EMPTY_IN_exchange_list_to_jq_path")
#         return()
#
#     #print("new_str itigi", new_str)
#     #print("return_list:",return_list)
#     #return(new_str)
#     return(return_list)


# 23) func get value with jq. input path, output value
#
# def get_path_value_jq(input_path, data):
#     if len(input_path) != 0:
#
#         item_path=input_path[0]
#
#         #query = f'getpath([{input_path}])'
#         query = f'getpath([{item_path}])'
#
#         result = pyjq.all(query, data)
#         #print("result in get_path_value_jq:",result)
#         if result[0] == None:
#             print("PATH_NOT_FOUND (get_path_value_jq):", input_path)
#         return (result)
#
#     else:
#         print("LIST_IS_EMPTY_IN_get_path_value_jq")
#         return ()


# 24) in unput func get values in config, paths in dist and set values for all paths in input_data
#
# def set_path_value_jq(input_values, input_paths, data, example_data):
#     #print("input_values in set jq:",input_values)
#     #print("input_paths: in set jq", input_paths)
#     if len(input_paths) != 0 and len(input_values) != 0:
#
#         item_one=input_values[0]
#         path_one=input_paths[0]
#         path_one_for_example=[path_one]
#         #print("path_one_for_example;", path_one_for_example)
#         #print("item_one in set_path_value_jq:",item_one)
#         #print("path_one in set_path_value_jq:",path_one)
#
#         #print("values_in_example_data in set_path_value_jq:")
#         value_for_example=get_path_value_jq(path_one_for_example,example_data)
#         #print("value_for_example:", value_for_example)
#
#         #if isinstance(item_one, str):
#         if isinstance(value_for_example[0], str):
#             #print("string in set_path_value_jq")
#             query = f'setpath([{path_one}];"{item_one}")'
#         else:
#             query = f'setpath([{path_one}];{item_one})'
#             #print("not str in set_path_value_jq")
#
#         #query = f'setpath([{input_paths}];{item_one})'
#         #query = f'setpath([{path_one}];"{item_one}")'
#
#         #query = f'setpath([{path_one}];{item_one})'
#
#         if item_one != None:
#             result = pyjq.all(query, data)
#             #print("result data in set_path_value_jq:", result)
#             return (result)
#             #print("111")
#         else:
#             #print("222")
#             print("None_VALUE_CANT_SET, no modification made")
#             return([data])
#         #print("result:", result)
#         return([data])
#     else:
#         print("LIST_IS_EMPTY_IN_set_path_value_jq")
#         return ([data])


# 25) get inputh path as str and set values for another func

# not use, because cant set global varrible for other func
# def get_input_arg_paths(input_arg_str):
#    print("input_arg_str:", input_arg_str)
#    path_list_with_arg = input_arg_str.split('=')
#    print("path_list_with_arg:", path_list_with_arg)
#    str_in_conf = path_list_with_arg[0]
#    conf_id = (str_in_conf.split(".")[-1])
#    print("str_in_conf:", str_in_conf)
#    print("conf_id:", conf_id)

#    str_in_dist = path_list_with_arg[1]
#    dist_id = (str_in_dist.split(".")[-1])
#    print("str_in_dist:", str_in_dist)
#    print("dist_id:", dist_id)


# ----------def all wokr func

# 14)
def get_path_value_func(input_path, input_data):
    #print("input_data",input_data)
    iterate_data = input_data
    #print("iterate_data_keys",iterate_data.keys())
    #print("input_path",input_path)
    #print("input_path",input_path)
    for keys in input_path:
        #print("keys",keys)
        # check, that each element in path is exist in config.json return-keys, otherwice break loop
        if keys in (iterate_data.keys()):
            pass

        else:
            # print(input_path, "KEY_NOT_EXIST")
            return ("KEY_NOT_EXIST")

        if (input_path.index(keys)) == (len(input_path) - 1):
            print("PATH: ", input_path, "KEY_EXIST:")  # work print

        iterate_data = iterate_data.get(keys)
    return (iterate_data)


# 13)

def all_dist_paths_func(conf_dist_data):
    only_arrays_path_after_regexp=[]
    not_arrays_path = pyjq.all(
        """
        del(.. | select(type=="array")) | paths(scalars | true)
        """, conf_dist_data)
    #print("not_arrays_path",not_arrays_path)

    only_arrays_path = pyjq.all(
        """
        path(..| select(type=="array"))
        """, conf_dist_data)
    #print("only_arrays_path",only_arrays_path)


    regex = re.compile('^(?!.*\d.*).*$')
    for i in  only_arrays_path:
        #print("i:",i)
        if re.search(regex, str(i)) != None:
            only_arrays_path_after_regexp.append(i)


    #print("only_arrays_path",only_arrays_path)
    #print("not_arrays_path",not_arrays_path)
    all_path = not_arrays_path + only_arrays_path_after_regexp
    #all_path = not_arrays_path + only_arrays_path
    #print("all_path",all_path)
    return (all_path)


# 15)
# !!!bugs!!! - isinstance wrong udestand walues, if in confid values = false, isinstance thsink that is int type

# def set_value_with_path_func(input_path, input_value, input_data, string_flag):
def set_value_with_path_func(input_path, input_value, input_data, example_data):
    # iterate_data=input_data
    # print("input_path in set_value_with_path_func:", input_path)

    # exchange path to str
    exchange_need_path_in_bak = exchange_list_to_jq_path([input_path])
    # print("exchange_need_path_in_bak:", exchange_need_path_in_bak)
    # get value
    value_in_bak_with_path = get_path_value_jq(exchange_need_path_in_bak, example_data)
    # print("value_in_bak_with_path:", value_in_bak_with_path)
    input_str_flag = ""
    if isinstance(value_in_bak_with_path[0], str):
        input_str_flag = "str_true"
        # print("str_true")
    elif value_in_bak_with_path[0] == False:
        input_str_flag = "all_false"
    elif value_in_bak_with_path[0] == True:
        input_str_flag = "all_false"
    elif isinstance(value_in_bak_with_path[0], int):
        input_str_flag = "int_true"
        # print("value_in_bak_with_path[0]", value_in_bak_with_path[0])
        # print("int_true")

    else:
        input_str_flag = "all_false"
        # print("all_false")
    # print("input_str_flag",input_str_flag)

    for keys in input_path:
        if (input_path.index(keys)) == (len(input_path) - 1):

            if input_str_flag == "str_true":
                # print("str_true")
                # print("input_data[keys]",input_data[keys])

                input_data[keys] = str(input_value)

                # print("input_value", input_value)
                # print("input_data in set",input_data)
            elif input_str_flag == "int_true":
                # print("int_true")
                input_data[keys] = int(input_value)
            else:
                # print("all_false")
                input_data[keys] = input_value

        else:
            input_data = input_data.get(keys)
    # print("value_setting_complete")
    return ()


# 16)

def run_func(dist_data_file, config_data_file, example_data):
    # print("dist_data_file",dist_data_file)
    # print("config_data_file", config_data_file)
    not_exist_keys = []
    all_paths = all_dist_paths_func(dist_data_file)
    #print("all_paths",all_paths)
    for path in all_paths:
        # print("path_in_run_func",path)

        ## exchange path to str
        # exchange_need_path_in_bak = exchange_list_to_jq_path([path])
        # print("exchange_need_path_in_bak:", exchange_need_path_in_bak)
        # get value
        # value_in_bak_with_path = get_path_value_jq(exchange_need_path_in_bak, example_data)
        # print("value_in_bak_with_path:", value_in_bak_with_path)

        value_in_config = get_path_value_func(path, config_data_file) #old method

        #exchange_need_path_in_runf = exchange_list_to_jq_path(need_path_in_config)
        # print("exchange_need_path_in_config_in_get_value:", exchange_need_path_in_config)
        # get value
        #value_in_config = get_path_value_jq(exchange_need_path_in_runf, data_config)
        # print("value_in_confid_with_path:", value_in_confid_with_path)


        #print("value_in_config_in_run:", value_in_config)

        if value_in_config == "KEY_NOT_EXIST":
            # print(path, "values not set!")
            # not_exist_keys = not_exist_keys + path #not work
            # work! method to create a list of lists
            # print("path in run_func", path)
            not_exist_keys.append(path)

        else:
            # print("Will be set value:", value_in_config)
            # set_value_with_path_func(path, value_in_config, dist_data_file, input_str_flag)
            set_value_with_path_func(path, value_in_config, dist_data_file, example_data)

    # all not exisying path of keys

    print("\n")
    print("not_exist_keys in config.json:")
    # print(not_exist_keys)
    for local_path in not_exist_keys:
        # print("not_exist_keys", not_exist_keys)
        # print("local_path",local_path)
        print(local_path)
    # print("dist_data_file end run func", dist_data_file)
    # print("config_data_file end run func", config_data_file)

    # print("end")
    # with open("config_new.json", "w") as file_out2:
    #    json.dump(dist_data_file, file_out2, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    print()
    return ()


# 18)

def recursive_find_value(value_to_find, find_inside_data):
    found = []
    for keys, values in find_inside_data.items():
        # print(keys)
        if keys == value_to_find:
            found.append(values)

        elif isinstance(values, dict):

            results = recursive_find_value(value_to_find, values)
            for result in results:
                found.append(result)

        elif isinstance(values, list):
            for item_list in values:
                if isinstance(item_list, dict):

                    another_result = recursive_find_value(value_to_find, item_list)
                    for item_in_another_result in another_result:
                        found.append(item_in_another_result)
    # print("found",found)
    return (found)


# 19)
def recursive_set_value(input_value, find_value, iterate_data):
    # print(input_value)
    global set_flag

    for keys, values in iterate_data.items():
        # print(keys)

        if keys == find_value:

            # print(set_flag)
            if set_flag != True:
                # print(set_flag)
                iterate_data[keys] = input_value[0]
                set_flag = True

            # found.append(values)

        elif isinstance(values, dict):
            # print("values", values)

            recursive_set_value(input_value, find_value, values)

        elif isinstance(values, list):
            for item_list in values:
                # print(item_list)
                if isinstance(item_list, dict):
                    # print("item_list:",item_list)
                    recursive_set_value(input_value, find_value, item_list)

    # print(found)
    return ()


# 20)
def all_path_wiht_key(inpyt_key, data):
    #query = f'path(.. | .{inpyt_key}? // empty)' #wrong work with sumbol '#' in  keys name
    query=f'paths | select(.[-1] == "{inpyt_key}")'
    result = pyjq.all(query, data)
    return (result)


# 21)
def what_path_need(find_path, find_key, data):
    set_path_list = find_path.split('.')
    set_path_list.sort()
    # print("set_list:", set_path_list)
    list_of_correct_path = []
    # print("set_path_list",set_path_list)
    # print("find_key",find_key)
    # print("all_path_wiht_key",all_path_wiht_key(find_key, data))
    for another_found_path in all_path_wiht_key(find_key, data):
        # print("another_found_path",another_found_path)
        new_list = []
        for item in another_found_path:
            try:
                item = float(item)
            except ValueError:
                # print("not a number\n")
                new_list.append(item)
        new_list.sort()
        # print("new_list_in_what_path_need",new_list)
        # print("find_path_in_list",set_path_list)
        if new_list == set_path_list and new_list != []:
            # print("111")
            # return(another_found_path)
            list_of_correct_path.append(another_found_path)
        # else:
        #    print("222")
    if list_of_correct_path != []:
        return (list_of_correct_path)
    else:
        print("PATH_AND_VALUE_NOT_FOUND", "nedeed path:", find_path, "find key:", find_key)
        return ("PATH_AND_VALUE_NOT_FOUND")

    # print("PATH_AND_VALUE_NOT_FOUND in what_path_need", "nedeed path:",find_path, "find key:", find_key)
    # print("in data", data)
    # print("list_of_correct_path:",list_of_correct_path)

    # return(list_of_correct_path)


# 22)
def exchange_list_to_jq_path(input_path):
    # exchange all item in list to string #work
    # print("input_path_in_exchange_list_to_jq_path",input_path)

    # print("path_one in exchange_list_to_jq_path",path_one)

    # new_list = []
    return_list = []
    new_str = ''

    if len(input_path) != 0:

        for path_one in input_path:
            # print("path_one in exchange_list_to_jq_path",path_one)
            new_list = []
            for item in path_one:
                try:
                    item = float(item)
                    item = int(item)
                    item = str(item)
                    new_list.append(item)

                except ValueError:
                    new_list.append(item)
            # print(new_list)

            new_str = ''
            # print("new_str in loop",new_str)
            for item in new_list:
                if item.isdigit():
                    # print(item, "It's a number")
                    if new_list.index(item) == 0:
                        new_str = new_str + item
                    else:
                        new_str = new_str + "," + item
                else:
                    item_in_doubleqoutes = f"\"{item}\""
                    # print("item_in_doubleqoutes", item_in_doubleqoutes)
                    if new_list.index(item) == 0:
                        new_str = new_str + item_in_doubleqoutes
                    else:
                        new_str = new_str + "," + item_in_doubleqoutes
                        # new_str = new_str+item_in_doubleqoutes
            return_list.append(new_str)
            # print("new_str", new_str)
    else:
        print("LIST_IS_EMPTY_IN_exchange_list_to_jq_path")
        return ()

    # print("new_str itigi", new_str)
    # print("return_list:",return_list)
    return (return_list)


# 23)
def get_path_value_jq(input_path, data):
    if len(input_path) != 0:

        item_path = input_path[0]

        # query = f'getpath([{input_path}])'
        query = f'getpath([{item_path}])'

        result = pyjq.all(query, data)
        # print("result in get_path_value_jq:",result)
        if result[0] == None:
            print("PATH_NOT_FOUND (get_path_value_jq):", input_path)
        return (result)

    else:
        print("LIST_IS_EMPTY_IN_get_path_value_jq")
        return ()


# 24)
#if key values - True or False, query not work:
# query = f'setpath([{path_one}];{item_one})'
#because python set in query python value "True" or "False" (with uppercase)
#but jq can uderstand only "true" or "false" (lowercase)
#to fix use block, but is so ugly
#        if item_one == False:
#            query = f'setpath([{path_one}];false)'

def set_path_value_jq(input_values, input_paths, data, example_data):
    # print("input_values in set jq:",input_values)
    # print("input_paths: in set jq", input_paths)
    if len(input_paths) != 0 and len(input_values) != 0:

        item_one = input_values[0]
        path_one = input_paths[0]
        path_one_for_example = [path_one]
        # print("path_one_for_example;", path_one_for_example)
        # print("item_one in set_path_value_jq:",item_one)
        # print("path_one in set_path_value_jq:",path_one)

        # print("values_in_example_data in set_path_value_jq:")
        value_for_example = get_path_value_jq(path_one_for_example, example_data)
        # print("value_for_example:", value_for_example)

        if item_one == False:
            query = f'setpath([{path_one}];false)'
        elif item_one == True:
            query = f'setpath([{path_one}];true)'
        else:
            if isinstance(value_for_example[0], str):
                # print("string in set_path_value_jq", value_for_example[0])
                query = f'setpath([{path_one}];"{item_one}")'
            else:
                query = f'setpath([{path_one}];{item_one})'
                # print("not str in set_path_value_jq")

        if item_one != None:
            result = pyjq.all(query, data)
            # print("result data in set_path_value_jq:", result)
            return (result)
            # print("111")
        else:
            # print("222")
            print("None_VALUE_CANT_SET, no modification made")
            return ([data])
        # print("result:", result)
        return ([data])
    else:
        print("Value_cant_set_in_current_twix")
        return ([data])


# 25)
# not use, because cant set global varrible for other func
def get_input_arg_paths(input_arg_str):
    # print("input_arg_str:", input_arg_str)
    path_list_with_arg = input_arg_str.split('=')
    # print("path_list_with_arg:", path_list_with_arg)
    str_in_conf = path_list_with_arg[0]
    conf_id = (str_in_conf.split(".")[-1])
    # print("str_in_conf:", str_in_conf)
    # print("conf_id:", conf_id)

    str_in_dist = path_list_with_arg[1]
    dist_id = (str_in_dist.split(".")[-1])
    # print("str_in_dist:", str_in_dist)
    # print("dist_id:", dist_id)


# _________ run all func

# test_run
# input_arg=['myf.py']
# input_arg=['myf.py','ids=id']
# input_arg=['myf.py','ids=id', 'shops.categories+categories=categories', 'shops.region_id+region_id=source.region_id+region_id','ops.ips+ips=ips.ops+ops']
# input_arg=['myf.py','metrics.push_interval_sec+push_interval_sec=metrics.push_interval_sec+push_interval_sec']
# input_arg=['myf.py','shops.ids+ids=source.shops.id+id']
# input_arg=['myf.py','shops.ids+ids=source.shops.id+id', 'shops.categories+categories=source.shops.categories+categories', 'shops.region_id+region_id=source.shops.region_id+region_id']
# input_arg=['myf.py','shops.categories+categories=source.shops.categories+categories', 'shops.region_id+region_id=source.shops.region_id+region_id']

# input_arg=['myf.py','ids=source.shops.id+id']

# input_arg=['myf.py','shops.categories+categories=source.shops.categories+categories']


# print("data_dist_bak before", data_dist_bak)
run_func(data_dist, data_config, data_dist_bak)  # main_run

args_str = args.keys if args.keys else ''
#print(f'args_str: ${args_str}')
if args.keys:
    args_str=args.keys

#elif ENVVAR:
#    print()

else:
    path=os.path.dirname(os.path.realpath(__file__))


args_list = args_str.split()

#print("args", args)
#print("args_list", args_list)

for count_of_args in range(0, len(args_list)):  # main_run
    curr_args_twix = args_list[count_of_args]  # main_run

    print()
    print("current_arg_twix:", curr_args_twix)

    # set all values from input arg
    path_list_with_arg = curr_args_twix.split('=')
    # print("path_list_with_arg:", path_list_with_arg)

    if '+' in path_list_with_arg[0]:
        left_arg = path_list_with_arg[0].split('+')
        # print("1111")
        # print("left_arg:",left_arg)
        str_in_conf = (left_arg[0])
        conf_id = (left_arg[1])
        # print("str_in_conf:", str_in_conf)
        # print("conf_id:", conf_id)
    else:
        # print("2222")
        str_in_conf = None
        conf_id = path_list_with_arg[0]
        # print("str_in_conf:", str_in_conf)
        # print("conf_id:", conf_id)

    if '+' in path_list_with_arg[1]:
        right_arg = path_list_with_arg[1].split('+')
        # print("3333")
        # print("right_arg:", right_arg)
        str_in_dist = (right_arg[0])
        dist_id = (right_arg[1])
        # print("str_in_dist:", str_in_dist)
        # print("dist_id:", dist_id)
    else:
        # print("444")
        str_in_dist = None
        dist_id = path_list_with_arg[1]
        # print("str_in_dist:", str_in_dist)
        # print("dist_id:", dist_id)

    # get left value
    print("get left value")
    if str_in_conf == None:
        print("find_path_in_config recursive")
        value_in_confid_with_path = recursive_find_value(conf_id, data_config)

        # return_value_in_confid_with_path=recursive_find_value(conf_id, data_config)
        # value_in_confid_with_path=return_value_in_confid_with_path[0]

        # print("values_in_example_data in set_path_value_jq:")
        # print(get_path_value_jq(path_one_for_example, example_data))

        # print("value_in_confid_with_path: no way",value_in_confid_with_path)
    else:
        # find path and value in config.json
        # print("find_path_in_config with jq")
        need_path_in_config = what_path_need(str_in_conf, conf_id, data_config)
        # print("need_path_in_config_in_get_value_with_jq:", need_path_in_config)
        if need_path_in_config != "PATH_AND_VALUE_NOT_FOUND":

            # exchange path to str
            exchange_need_path_in_config = exchange_list_to_jq_path(need_path_in_config)
            # print("exchange_need_path_in_config_in_get_value:", exchange_need_path_in_config)
            # get value
            value_in_confid_with_path = get_path_value_jq(exchange_need_path_in_config, data_config)
            # print("value_in_confid_with_path:", value_in_confid_with_path)

            # print("data_dist_bak:")
            # print(get_path_value_jq(exchange_need_path_in_config, data_dist_bak))
        else:
            value_in_confid_with_path = []

    # set in right
    if str_in_dist == None:
        print("find_path_in_dist")
        # print("in str_in_dist")
        set_flag = False
        recursive_set_value(value_in_confid_with_path, dist_id, data_dist)
    else:
        # find path in dist
        print("find_path_in_dist")
        need_path_in_dist = what_path_need(str_in_dist, dist_id, data_dist)
        # print("need_path_in_dist", need_path_in_dist)

        if need_path_in_dist != "PATH_AND_VALUE_NOT_FOUND":
            # exchange path to str
            exchange_path_in_dist = exchange_list_to_jq_path(need_path_in_dist)
            # print("exchange_path_in_dist:", exchange_path_in_dist)

            # print("data_dist_bak:")
            # print(get_path_value_jq(exchange_path_in_dist, data_dist_bak))

            # print("before")
            # print(data_dist)
            # set valuein config with path to dist witp path
            # print("value_in_confid_with_path", value_in_confid_with_path)
            change_data = set_path_value_jq(value_in_confid_with_path, exchange_path_in_dist, data_dist, data_dist_bak)
            # print("change_data", change_data)
            data_dist = change_data[0]
            # print("after")
            # print(data_dist)

# print("config_new.json")
# print(data_dist)
# print("data_dist_bak")
# print(data_dist_bak)

# logik "block with args"
# and now:
# first i have path, what i nedeed and key_name
# last item in nedeed_path and key_name is identical

# two: i get all path for this key in config.json with func "all_path_wiht_key"
# but is func arise in another func "what_path_need"

# three
# i compare nedeed path and all path of this key and return the path, that
# comparsion completed succesfully. it work do the func "what_path_need"

# four: now i need exchange list path to string, because jq make eat only string
# is do func "exchange_list_to_jq_path"

# five: func "get_path_value_jq" eating exchanget path and return value in this path


# block write
with open(Path(path, 'config_new.json'), "w") as file_out2:
    json.dump(data_dist, file_out2, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
