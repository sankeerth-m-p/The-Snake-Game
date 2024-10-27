#Snake Game Using Linked List and Pygame

About
This is a classic Snake Game created with Python using linked lists for the snake’s body and pygame for graphics. Each segment of the snake is managed with a linked list, which lets the snake grow easily when it eats food. pygame is used to handle game visuals, user input, and screen updates.

How It Works
Linked List for Snake: Each part of the snake is stored as a node in a linked list. The head node is the snake’s head, and each new node added becomes part of its body. When the snake eats food, we add a new node to make it longer.

Pygame for Graphics: pygame displays the game window, draws the snake and food, and lets the player control the snake with arrow keys.
