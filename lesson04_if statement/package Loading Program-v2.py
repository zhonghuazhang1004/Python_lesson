total_weight = 0
sent_package = 0
current_package_weight = 0
items = 0
unused_weight_list = {}


plan_items = int(input("How many items you are going to send: "))

program_running = True

while program_running:

    added_weight = input("Please enter the weight you want to added ( 1 ~ 10kg ):")

    # verify input is a number or not, if yes > continue, if no > print error msg
    if added_weight.isdigit():
        added_weight = int(added_weight)

        # verify user's input within[1~10]
        if 1 < added_weight < 10:

            total_weight += added_weight
            current_package_weight += added_weight
            items += 1

            if items < plan_items:
                if current_package_weight == 20:
                    unused_weight_perPackage = 0

                    print("--------------------------------")
                    print(f"*****Package sent (weight = {current_package_weight})*****")
                    sent_package += 1
                    print(f">Sent package No. = {sent_package}")
                    print(f">Current package weight = {current_package_weight}")
                    unused_weight_perPackage = 20 - current_package_weight
                    unused_weight_list[sent_package] = unused_weight_perPackage
                    print(f">unused weight:{unused_weight_perPackage}")
                    current_package_weight = 0
                    print(f"Sent items ={items}")
                    print(f">Total loaded weight = {total_weight}")
                    print("--------------------------------\n")
                elif current_package_weight > 20:
                    unused_weight_perPackage = 0


                    print("--------------------------------")
                    current_package_weight -= added_weight
                    total_weight -= added_weight
                    items -= 1
                    sent_package += 1
                    print(f"*****Package sent (weight = {current_package_weight})*****")
                    print(f">Sent package No. = {sent_package}")
                    print(f">Current package weight = {current_package_weight}")

                    unused_weight_perPackage = 20 - current_package_weight
                    unused_weight_list[sent_package] = unused_weight_perPackage
                    print(f">unused weight:{unused_weight_perPackage}")
                    current_package_weight = 0

                    print(f"Sent items ={items}")
                    print(f">Total loaded weight = {total_weight}")

                    print("--------------------------------\n")
            else:
                print("--------------------------------")
                print(f"*****Package sent (weight = {current_package_weight})*****")
                sent_package += 1
                print(f">Sent package No. = {sent_package}")
                print(f">Current package weight = {current_package_weight}")
                unused_weight_perPackage = 20 - current_package_weight
                unused_weight_list[sent_package] = unused_weight_perPackage
                print(f">unused weight:{unused_weight_perPackage}")
                current_package_weight = 0
                print(f"Sent items ={items}")
                print(f">Total loaded weight = {total_weight}")
                print("----------*****All items sent*****------------\n")


                program_running = False



        elif added_weight == 0:
            print("-----No more goods need to be added, System out!------")
            program_running = False
        else:
            print("-----Enter error! Please enter proper weight ( 1 ~ 10kg ):----- ")

    else:
        print("-----Enter error!Please enter a number-----")

print("--------------Program Result------------------")
print(f"Total sent package = {sent_package}")
print(f"Total sent weight = {total_weight}")
print(f"Unused weight = {sent_package * 20 - total_weight}\n")
max_unused_key = max(unused_weight_list, key=unused_weight_list.get)
max_unused_value = unused_weight_list[max_unused_key]
print(f"Package : {max_unused_key} has max unused weight = {max_unused_value}")

print("-----------------------------------------------\n")
