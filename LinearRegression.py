# -*- coding: utf-8 -*-
"""
Regresión Lineal por mínimo cuadrado.
Aplicación: Coeficiente de Expansión Térmica del Acero.
"""
__author__ = "Gonzalo Chacaltana"

import sys, csv
import numpy as np
from matplotlib import pyplot as plt 

class LinearRegression(object):
    
    def __init__(self):
        """
        x = Temperaturas
        y = Coeficiente de expansión térmica
        """
        self.x, self.y = np.array([]), np.array([])

    def input_data(self,filename):
        with open(filename, mode='r') as datafile:
            reader = csv.reader(datafile, delimiter=",")
            for row in reader:
                self.x = np.append(self.x,int(row[0]))
                self.y = np.append(self.y,float(row[1]))

    def show_data(self):
        print("\n{} {}".format("".ljust(20, "-"),"".ljust(46, "-")))
        print("{} {}".format("Temperatura en F*".center(20), "Coeficiente de expansion termica (en 10**-6)".center(46)))
        print("{} {}".format("".ljust(20, "-"),"".ljust(46, "-")))
        print("{} {}".format("Variable x".center(20),"Variable y".center(46)))
        print("{} {}".format("".ljust(20, "-"),"".ljust(46, "-")))
        for k in range(len(self.x)):
            print("{} {}".format(str(self.x[k]).center(20),str(self.y[k]).center(46)))

    def show_graph_data(self):
        plt.style.use('classic')
        plt.scatter(self.x, self.y,alpha=0.5, color="royalblue", s=75)
        plt.grid(True)
        plt.ylabel("y = Coeficiente de Expansión Térmica (10**-6)")
        plt.xlabel("x = Temperatura (en F°)")
        plt.title("Gráfico: Coeficiente de expansión térmica del acero por temperatura")
        plt.show()
    
    def calculate_rl(self):
        self.n = len(self.x)
        self.sum_x = np.sum(self.x)
        self.sum_x_x = np.sum(self.x**2)
        self.sum_y = np.sum(self.y)
        self.sum_xy = np.sum(self.x*self.y)
        self.A = np.array([[self.n,self.sum_x], [self.sum_x, self.sum_x_x]])
        self.dA = np.linalg.det(self.A)
        self.B = np.array([[self.sum_y], [self.sum_xy]])
        self.X = np.dot(np.linalg.inv(self.A),self.B)
        self.k1, self.k2 = self.X[0],self.X[1]
        self.y_rl = self.x*self.k2 + self.k1
    
    def show_calculate_rl(self):
        print("\n")
        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        print("{} {} {} {} {}".format("I".center(6),"T".center(12), "& (10**-6)".center(12),"T.& (10**-4)".center(12),"T**2".center(12)))
        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        print("{} {} {} {} {}".format("".center(6),"x".center(12), "y".center(12),"x*y".center(12),"x**2".center(12)))
        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        
        for k in range(len(self.x)):
            print("{} {} {} {} {}".format(
                str(k+1).center(6),
                str(self.x[k]).center(12),
                str(self.y[k]).center(12),
                str(round((self.x[k]*self.y[k])/100,3)).center(12),
                str(self.x[k]**2).center(12)))

        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        print("{} {} {} {} {}".format("".center(6),str(self.sum_x).center(12),str(round(self.sum_y/100,5)).center(12),str(round(self.sum_xy/10000,4)).center(12),str(self.sum_x_x).center(12)))
        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        print("{} {} {} {} {}".format("n".center(6),"sum_x".center(12),"sum_y".center(12),"sum_xy".center(12),"sum_x_x".center(12)))
        print("{} {} {} {} {}".format("".ljust(6, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-"),"".ljust(12, "-")))
        
        input("")
        print("\nCalculos para hallar la ecuacion matricial: A.X = B")
        print("Donde: ")
        print("Vector X = Inversa(A)*B")

        print("\nHallando la Matriz A")
        print("A = np.array([[n,sum_x], [sum_x, sum_x_x]])")
        print("A = {}".format(self.A))
        input("")

        print("\nHallando la Matriz B")
        print("B = np.array([[sum_y], [sum_xy]])")
        print("B = {}".format(self.B))
        input("")

        print("\nDeterminante de la Matriz A")
        print("Si det(A]) != 0 => A tiene inversa")
        print("d.A = np.linalg.det(A)")
        print("d.A = {}".format(self.dA))
        input("")

        print("\nHallando X")
        print("X = Inversa(A) * B")
        print("X = np.dot(np.linalg.inv(A),B)")
        print("X = {}".format(self.X))
        input("")

        print("\nEl valor k1 = {}".format(self.k1))
        print("\nEl valor k2 = {}".format(self.k2))
        input("")

        print("\nRegresion Lineal")
        print("RL = k1 + k2.x")
        print("RL = {}".format(self.y_rl))
    
    def show_graph_linear_regresion(self):
        plt.style.use('classic')
        plt.scatter(self.x, self.y,alpha=0.5, color="royalblue", s=75)
        plt.grid(True)
        plt.plot(self.x,self.y_rl,color="red")
        plt.ylabel("y = Coeficiente de Expansión Térmica (10**-6)")
        plt.xlabel("x = Temperatura (en F°)")
        plt.title("Gráfico: Regresion Lineal para el coeficiente de expansión térmica del acero por temperatura")
        plt.show()