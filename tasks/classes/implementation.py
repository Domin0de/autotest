import sys

class RoboTaxi:
    pass

class ToogleHub:
    pass

class Passenger:
    pass

# DO NOT MODIFY BELOW THIS LINE
if __name__ == "__main__":
    creations = []

    while True:
        user_input = sys.stdin.readline().strip()
        if user_input == 'exit':
            break

        commands = user_input.split()
        # commands = [class, command, id, *args]
        action_id = int(commands[2])

        try:
            match commands[0]:
                case "r":
                    # Handle RoboTaxi commands
                    match commands[1]:
                        case "c":
                            # Handle RoboTaxi create command
                            nt = RoboTaxi(commands[3], int(commands[4]))
                            creations.append(nt)
                        case "b":
                            # Handle RoboTaxi board command
                            t = creations[action_id]
                            try:
                                p = creations[int(commands[3])]
                                t.board_taxi(p)
                            except:
                                t.board_taxi(commands[3])
                        case "a":
                            # Handle RoboTaxi alight command
                            t = creations[action_id]
                            try:
                                p = creations[int(commands[3])]
                                t.alight_taxi(p)
                            except:
                                t.alight_taxi(commands[3])
                        case "s":
                            # Handle RoboTaxi set destination command
                            t = creations[action_id]
                            t.set_destination(commands[3])
                        case "m":
                            # Handle RoboTaxi model command
                            t = creations[action_id]
                            print(t.get_model())
                        case "ca":
                            # Handle RoboTaxi capacity command
                            t = creations[action_id]
                            print(t.get_capacity())
                        case "gp":
                            # Handle RoboTaxi get passengers command
                            t = creations[action_id]
                            print(t.get_passengers())
                        case "gd":
                            # Handle RoboTaxi get destination command
                            t = creations[action_id]
                            print(t.get_destination())
                        case _:
                            print("Unknown RoboTaxi command")
                case "t":
                    # Handle ToogleHub commands
                    match commands[1]:
                        case "c":
                            # Handle ToogleHub create command
                            nh = ToogleHub(commands[3], int(commands[4]))
                            creations.append(nh)
                        case "a":
                            # Handle ToogleHub add command
                            h = creations[action_id]
                            h.add_taxi(creations[int(commands[3])])
                        case "r":
                            # Handle ToogleHub remove command
                            h = creations[action_id]
                            h.remove_taxi(creations[int(commands[3])])
                        case "ac":
                            # Handle ToogleHub average capacity command
                            h = creations[action_id]
                            print(h.get_average_capacity())
                        case "wt":
                            # Handle ToogleHub waiting taxis command
                            h = creations[action_id]
                            print(h.get_waiting_taxis())
                        case "md":
                            # Handle ToogleHub model distribution command
                            h = creations[action_id]
                            h.get_model_distribution()
                        case "rs":
                            # Handle ToogleHub reset command
                            h = creations[action_id]
                            h.reset_taxis()
                        case "l":
                            # Handle ToogleHub location command
                            h = creations[action_id]
                            print(h.get_location())
                        case "s":
                            # Handle ToogleHub space command
                            h = creations[action_id]
                            print(h.get_space())
                        case "fd":
                            # Handle ToogleHub favourite destinations command
                            h = creations[action_id]
                            h.get_favourite_destinations()
                        case "sd":
                            # Handle ToogleHub subscription distribution command
                            h = creations[action_id]
                            h.get_subscription_distribution()
                        case _:
                            print("Unknown ToogleHub command")
                case "p":
                    # Handle Passenger commands
                    match commands[1]:
                        case "c":
                            # Handle Passenger create command
                            np = Passenger(commands[3], commands[4])
                            creations.append(np)
                        case "u":
                            # Handle Passenger upgrade subscription command
                            p = creations[action_id]
                            p.upgrade_subscription()
                        case "s":
                            # Handle Passenger get subscription command
                            p = creations[action_id]
                            print(p.get_subscription())
                        case "sfd":
                            # Handle Passenger set favourite destination command
                            p = creations[action_id]
                            p.set_favourite_destination(commands[3])
                        case "gfd":
                            # Handle Passenger get favourite destination command
                            p = creations[action_id]
                            print(p.get_favourite_destination())
                        case _:
                            print("Unknown Passenger command")
                case _:
                    print("Unknown command")
        except:
            pass
