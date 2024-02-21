total_weight: int = 0
sent_package: int = 0
package_weight = 0

unused_weight_list = {}

# ask user how many package they would like to send
plan_package = int(input("How many packages you are going to send: "))

program_running = True

while program_running:

    added_weight = input("Please enter the weight you want to added ( 1 ~ 10kg ):")

    # verify input is a number or not, if yes > continue, if no > print error msg
    if added_weight.isdigit():
        added_weight = int(added_weight)



        # verify user's input within[1~10]
        if 1 < added_weight < 10:
            total_weight = total_weight + added_weight
            package_weight = package_weight + added_weight
            print(f">Current package weight = {package_weight}")

            if package_weight == 20:
                unused_weight_pertime = 0
                print("--------------------------------\n")

                print(">This package sent ( = 20 kg)")
                sent_package = sent_package + 1
                print(f">Sent package No. = {sent_package}")
                print(f">Total loaded weight = {total_weight}\n")
                unused_weight_pertime = 20 - package_weight
                print(f"Package No.: {sent_package}------Unused weight = {20 - package_weight}")
                unused_weight_list[sent_package] = unused_weight_pertime
                package_weight = 0

                print("--------------------------------\n")
            elif package_weight > 20:
                unused_weight_pertime = 0
                print("--------------------------------\n")
                package_weight = package_weight - added_weight
                print(">This package sent ( > 20 kg)")
                sent_package = sent_package + 1
                print(f">Sent package No. = {sent_package}")
                unused_weight_pertime = 20 - package_weight
                print(f"Package No.: {sent_package}------Unused weight = {20 - package_weight}")
                total_weight = total_weight - added_weight
                print(f">Total loaded weight = {total_weight}\n")
                unused_weight_list[sent_package] = unused_weight_pertime
                package_weight = 0


                print("--------------------------------\n")

            if sent_package == plan_package:
                print("Already hit packages limitation, System out!")
                program_running = False



        # if user input = 0, means no more goods add, program terminate
        elif added_weight == 0:
            print("-----No more goods need to be added, System out!------")
            program_running = False
        else:
            print("-----Enter error! Please enter proper weight ( 1 ~ 10kg ):----- ")
    else:
        print("-----Enter error!Please enter a number-----")

# program result:
print("--------------Program Result------------------\n")
print(f"Total sent package = {sent_package}")
print(f"Total sent weight = {total_weight}")
print(f"Unused weight = {sent_package * 20 - total_weight}\n")
max_unused_key = max(unused_weight_list, key=unused_weight_list.get)
max_unused_value = unused_weight_list[max_unused_key]
print(f"Package : {max_unused_key} has max unused weight = {max_unused_value}")

print("-----------------------------------------------\n")