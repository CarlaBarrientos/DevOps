import virtualbox
vbox = virtualbox.VirtualBox()
sessions = {}
menu_options = {
    1: 'Create a VM',
    2: 'Delete a VM',
    3: 'Stand up a VM',
    4: 'Poweroff a VM',
    5: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def create_vm():
    name = input('Enter the vm name: ')
    disk = input('Enter disk location: ')
    os = input('Enter OS type: ')
    try:
        disk_location = "{}/{}/{}.vdi".format(disk, name, name)
        hdd = vbox.create_medium(format_p="vdi",
                                 location=disk_location,
                                 access_mode=virtualbox.library.AccessMode.read_write,
                                 a_device_type_type=virtualbox.library.DeviceType.hard_disk)
        vm = vbox.create_machine(name=name,
                                 os_type_id=os,
                                 settings_file="",
                                 groups=[],
                                 flags="")
        vm.add_storage_controller("SATA", virtualbox.library.StorageBus.sata)
        vbox.register_machine(vm)
    except:
        print('Can not create new virtual machine.')


def delete_vm():
    name = input('Enter the vm name: ')
    try:
        vm = vbox.find_machine(name)
        vm.remove()
    except:
        print('The name entered does not exist!')


def standup_vm():
    try:
        name = input('Enter the vm name: ')
        vm = vbox.find_machine(name)
        session = virtualbox.Session()
        sessions[name] = session
        progress = vm.launch_vm_process(session, "gui", [])
        progress.wait_for_completion()
    except:
        print('Could not standup the specified machine.')


def poweroff_vm():
    try:
        name = input('Enter the vm name: ')
        sessions[name].console.power_down()
    except:
        print('There is no session running for the specified machine.')


if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            create_vm()
        elif option == 2:
            delete_vm()
        elif option == 3:
            standup_vm()
        elif option == 4:
            poweroff_vm()
        elif option == 5:
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
