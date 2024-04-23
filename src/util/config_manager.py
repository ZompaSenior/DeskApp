"""Modulo per la gestione delle configurazioni dell'applicazione."""

# Standard Import
import configparser

# Site-package Import

# Project Import
from util import option_manager as om
from util import path_manager as pm
# from util import config_manager_constants as cmc


class ConfigManager(configparser.ConfigParser):
    """Classe per gestire le configurazioni iniziali dell'applicazione."""
    
    def __init__(self,
                 path: pm.PathManager,
                 option: om.OptionManager):
        """
        Il costruttore della classe.
        
        Args:
            option (OptionManager): il gestore delle configurazionida riga di
                comando.
        """
        super().__init__()
            # interpolation = configparser.ExtendedInterpolation)
            # default_sction = S_DEFAULT)
        
        self.__config_path = path.config_path
        
        self.read(self.__config_path, "utf-8")
        
    def save(self):
        """Permette di salvare le modifiche apportate alla configurazione"""
        
        with open(self.__config_path, 'w') as f:
            self.write(f)
        
