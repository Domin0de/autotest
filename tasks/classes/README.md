# Classes Task

## Stage 1

A new robotaxi business Toogle has recently become established in the local area. Update the class ``RoboTaxi`` to represent Toogle's robotaxis. The RoboTaxis should have the following attributes:
- ``passengers``: list of names (string)
- ``model``: string
- ``capacity``: number
- ``destination``: name of current destination

The RoboTaxis should have the following methods:
- ``board_taxi(string)`` - adds the name string to the ``passengers`` list, if there is still capacity. If the taxi is full, it should print "(name) cannot board the taxi, it is full." instead.
- ``alight_taxi(string)`` - removes the name string from the ``passengers`` list, if the name is in the list. If the name is not in the list, it should print "(name) cannot alight the taxi, they are not a passenger." instead.
- ``set_destination(string)`` - sets the ``destination`` attribute to the destination string
- ``get_model()`` - returns the model of the taxi
- ``get_capacity()`` - returns the capacity of the taxi
- ``get_passengers()`` - returns the list of passenger on the taxi
- ``get_destination()`` - returns the destination of the taxi or "None" if none is set

## Stage 2

Update the class ``ToogleHub`` to represent the taxi-hubs. The ToggleHub should have the following attributes:
- ``taxis``: list of ``RoboTaxi`` instances
- ``location``: string
- ``space``: number

The ToggleHub should have the following methods:
- ``add_taxi(RoboTaxi)`` - adds the RoboTaxi instance to the ``taxis`` list, if there is still space. If the hub is full, it should print "Cannot add new taxi to this hub, the hub is full." instead
- ``remove_taxi(RoboTaxi)`` - removes the RoboTaxi instance from the ``taxis`` list, if the RoboTaxi instance is in the list. If the RoboTaxi instance is not in the list, it should print "Cannot remove the taxi from this hub, it is not based here." instead
- ``get_average_capacity()`` - gets the average capacity of the taxis within the hub and returns it with 2 decimal places of precision.
- ``get_waiting_taxis()`` - returns number of RoboTaxis in the hub which have no passengers and no destination attribute set
- ``get_model_distribution()`` - counts the number of each model for the RoboTaxis at that hub, and prints them in descending order then alphabetically with format: "(model): X | (model): Y", or prints "No models" otherwise
- ``reset_taxis()`` - removes the passengers and sets the destination to an empty string for every taxi at that hub
- ``get_location()`` - returns the location of the hub
- ``get_space()`` - returns the space in the hub

### Stage 3

Toogle has recently introduced subscription services for their passengers, so need to have unique data for each passenger. Update the ``Passenger`` class, and all other relevant classes to replace the previously stored passenger names. The Passenger should have the following attribtues:
- ``name``: string
- ``subscription``: string ("Free", "Basic", "Premium")
- ``favourite_destination``: string

The Passenger should have the following methods:
- ``upgrade_subscription()`` - upgrades the subscription by replacing "Free" subscriptions with "Basic", "Basic" with "Premium", and printing "(name) already has the maximum subscription." instead
- ``get_subscription()`` - returns the subscription plan
- ``set_favourite_destination(string)`` - sets the ``favourite_destination`` attribute to the favourite destination string
- ``get_favourite_destination()`` - returns the favourite destination else "None" if none is set

The ToggleHub should now have these additional methods:
- ``get_favourite_destinations()`` - counts the number of favourite destinations for each passenger in the RoboTaxis at that hub, and prints the destination names in descending order then alphabetically with format: "(destination): X | (destination): Y", or prints "No destinations" otherwise
- ``get_subscription_distribution()`` - counts the number of subscriptions for each passenger in the RoboTaxis at that hub, and prints them with format: "Premium: X | Basic: Y | Free: Z"

The RoboTaxi should have methods modified as follows:
- ``get_passengers()`` - return the list of names from passengers on the taxi