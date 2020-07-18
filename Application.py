# -*- coding: utf-8 -*-
"""
Aplicación
"""
__author__ = "Gonzalo Chacaltana"

import os.path
from LinearRegression import LinearRegression


class Application(object):
    def __init__(self):
        self.line_lenght = 30

    def clear_window(self, wait=False):
        if wait:
            input("\n[Enter] Ir al menu principal.")
        return os.system('clear')

    def run(self):
        self.input_data_file()
        self.display_options()

    def input_data_file(self):
        self.clear_window()
        self.datafile = input("\nIngresar nombre del fichero de datos (.csv): ")
        if (not os.path.exists(self.datafile)):
            raise Exception("Archivo no existe.")
        self.rl = LinearRegression()
        self.rl.input_data(self.datafile)

    def display_options(self):
        self.clear_window()
        while(True):
            try:
                print ("-".ljust(90, "-"))
                print("Aplicacion de Regresion Lineal - Caso: Coeficiente de Expansion Termica del Acero.")
                print ("-".ljust(90, "-"))
                print("1. Mostrar datos cargados")
                print("2. Mostrar grafico de Temperatura vs Coeficiente de expansion termica.")
                print("3. Mostrar calculo de Regresion Lineal.")
                print("4. Mostrar grafico de Regresion Lineal.")
                print("0. Salir.")
                self.option = int(input(" -> "))
            except Exception:
                self.clear_window()
            self.switch_options()
            if (self.option == 0):
                break

    def switch_options(self):
        if self.option == 1:
            self.clear_window()
            self.rl.show_data()
            self.clear_window(True)
        elif self.option == 2:
            self.clear_window()
            self.rl.show_graph_data()
            self.clear_window(True)
        elif self.option == 3:
            self.clear_window()
            self.rl.calculate_rl()
            self.rl.show_calculate_rl()
            self.clear_window(True)
        elif self.option == 4:
            self.clear_window()
            self.rl.show_graph_linear_regresion()
            self.clear_window(True)
        elif self.option == 0:
            self.clear_window()
        elif self.option > 3:
            self.clear_window()
        else:
            self.clear_window()
