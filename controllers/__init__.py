# register controllers that will be used
from controllers.shelters_controller import shelters
from controllers.animals_controller import animals
from controllers.home_controller import home

registerable_controllers = [
    shelters,
    animals,
    home
]