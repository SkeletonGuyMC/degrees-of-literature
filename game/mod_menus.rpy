label bus_menu:
    if money == 1 or money >= 1:
        'It doesn\'t take long for a bus to arrive.'
        'I step onto the bus.'
    else:
        'I don\'t have enough money to catch the bus.'
        if location == "Fukuda":
            jump fukuda_menu
        elif location == "Fujimori":
            jump fujimori_menu
        elif location == "Tanaka":
            jump tanaka_menu
        elif location == "Akemi":
            jump akemi_menu
        elif location == "Izaya":
            jump izaya_menu
        elif location == "Sakamoto":
            jump sakamoto_menu
        elif location == "Izanagi":
            jump izanagi_menu
        elif location == "Haruo":
            jump haruo_menu
        elif location == "Hasewaga":
            jump hasewaga_menu
        elif location == "Makoto":
            jump makoto_menu
