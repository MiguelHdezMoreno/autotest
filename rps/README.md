# Rock, Paper, Scissors Game

This is a simple command-line game of Rock, Paper, Scissors. The user plays against the computer, which makes its choice randomly.

## How to Play

1. Run the script with the command `python rps.py`.
2. When prompted, enter your choice: Rock, Paper, or Scissors. The input is not case-sensitive.
3. The computer's choice will be printed, and then the result of the game.

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both the user and the computer make the same choice, it's a tie.

## Code Overview

The script contains two main functions:

- `user_choice()`: This function gets the user's choice. If the user enters an invalid choice, they are prompted to enter their choice again.
- `play_RPS()`: This function implements the game logic. It gets the user's choice, randomly determines the computer's choice, and then determines the result of the game based on the rules of Rock, Paper, Scissors.

The game starts automatically when the script is run.



# Juego de Piedra, Papel, Tijeras

Este es un sencillo juego de Piedra, Papel, Tijeras para la línea de comandos. El usuario juega contra la computadora, la cual elige su opción al azar.

## Cómo Jugar

1. Ejecuta el script con el comando `python rps.py`.
2. Cuando se te solicite, ingresa tu elección: Piedra, Papel o Tijeras. La entrada no distingue entre mayúsculas y minúsculas.
3. La elección de la computadora se imprimirá y luego se mostrará el resultado del juego.

## Reglas del Juego

- Piedra vence a Tijeras
- Tijeras vencen a Papel
- Papel vence a Piedra
- Si tanto el usuario como la computadora eligen la misma opción, es un empate.

## Descripción del Código

El script contiene dos funciones principales:

- `user_choice()`: Esta función obtiene la elección del usuario. Si el usuario ingresa una opción inválida, se le solicita que ingrese su elección nuevamente.
- `play_RPS()`: Esta función implementa la lógica del juego. Obtiene la elección del usuario, determina al azar la elección de la computadora y luego determina el resultado del juego basado en las reglas de Piedra, Papel, Tijeras.

El juego comienza automáticamente cuando se ejecuta el script.
