# Scum Drop Generator
The Scum drop generator is a bot for the Scum game
that will create a random or set number of drops in
either a random or specific zone or zones.

Use the settings.ini file to change the parameters.
Doing so will allow you to drop any number of cargo
drops in any number of zones (specified or random)
or over the entire map (use the keyword "WORLD").

## settings.ini
    [settings]
        minimum_random sets the low end of random drops
        maximum_random sets the high end of random drops
        set_number sets a specified number of drops
            setting this higher than zero will over-ride
            creating a random number of drops. If you want
            a random number, this should be set to 0.
        number_of_zones_to_drop sets the number of random zones.
            the number of
            drops will be evenly distributed among all of the zones,
            ie: if 30 drops are created, and there are 3 zones, then
            each zone will have 10 drops each.
            Set this to 0 if you want to specify specific zones
    [multiple.zones]
        lists the specific zones to create drops in.
        use the keyword WORLD to create drops over the entire
        map. Add zones by creating new entries below 'zone1 =',
        such as zone2 = then the zone, so it would look like:
            zone1 = C4
            zone2 = A0
            zone3 = B2
        You can add any number of zones, however the number of
        drops will be evenly distributed among all of the zones,
        ie: if 30 drops are created, and there are 3 zones, then
        each zone will have 10 drops each.