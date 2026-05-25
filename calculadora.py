import requests
from flask import Flask, render_template, request


def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']
    


    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1} + {num2} = {resultado}'
        
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1} - {num2} = {resultado}'
        
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1} * {num2} = {resultado}'
        
    elif operacao == '/':
        resultado = num1 / num2
        etapas = f'{num1} / {num2} = {resultado}'
        if num1 == 0 or num2 == 0:
            resultado =("Operaçao com 0 invalida")
        else:
            print("")
    else:
        resultado = "Operaçao invalida"
        etapas = "A operaçao selecionada e invalida"
        return render_template('index.html',etapas=etapas,resultado=resultado)
            
              
   