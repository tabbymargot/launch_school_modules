"""
PROBLEM:
Clarifying questions:
- How low / high can a layer be?
- How deep can a layer be?
- What is the relationship between upper and lower layers? For example, can a lower layer be more than one layer below the upper layer? Or is it immediately underneath the upper layer?
- What does 'supported by' mean?
- What is a block made of? What is a cube in code?

Input: 
- Integer representing the number of available blocks?
- String representations of blocks?
- Something else that represents the blocks?
Output: 
- Integer representing the number of blocks left over after building the tallest possible valid structure

Explicit rules
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Implicit rules:
- None

EXAMPLES

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

- Confirms analysis in diagram.
- There won't always be leftover blocks.
- One block is represented by the number 1.
- A lower layer is not valid if it has more blocks than it needs.

DATA STRUCTURES

- Needs to be some kind of ordered sequence of integers, each integer representing a layer.
- May need to include iteration as we add layers, so probably need to work with a mutable data structure (ie a list rather than a tuple).

ALGORITHM (lines in caps are lines added after I started coding)

1. Get the input specifying the number of blocks.

INITIALISE A VARIABLE (TO 0) TO STORE THE RUNNING TOTAL
INITIALISE A VARIABLE (TO 1) TO STORE THE NO. OF BLOCKS IN THE CURRENT LAYER

2.  Calculate how many layers there will be.
    - First layer == 1 (total)
        - If total less than input:
            - Store total as running total
            - Continue looping
        - Else break
    - Second layer (increment the integers to be multipied by 1) == 2 * 2 (total) 
        - Add together layer totals and add to running total
        - If total less than input:
            - Store this total as new running total
            - Continue looping
        - Else break
    - Continue, incrementing the multiplied integers by 1 each time, until the loop breaks.
3. Calculate how many blocks will be left over and return that value
    - Delete running total from input and return result

"""
'''

- running total of blocks that have been used
- set initial amount of blocks in next layer

LOOP
- add amount of blocks in next layer to running total
- calculate amount of blocks in next layer. FOR THIS NEED THE AMOUNT OF BLOCKS ALONG THE EDGE OF THE CURRENT LAYER, NOT JUST THE NO. OF BLOCKS IN THE CURRENT LAYER

- stop when running total is greater than total no of blocks.

- delete last layer
- calculate and return remaining blocks

'''

def calculate_leftover_blocks(number_of_input_blocks):
    blocks_used = 0
    blocks_in_current_layer = 1
    current_layer_edge = 1

    while True:
        blocks_used += blocks_in_current_layer
        current_layer_edge += 1
        blocks_in_current_layer = current_layer_edge * current_layer_edge
        
        # print(f'Blocks used: {blocks_used}')
        print(f'Current layer edge: {current_layer_edge}')
        # print(f'Blocks in current layer: {blocks_in_current_layer}')

        if blocks_used > number_of_input_blocks:
            blocks_used -= blocks_in_current_layer
            print(blocks_used)
            remainder = number_of_input_blocks - blocks_used
            print(remainder)
            return remainder



    # while blocks_used < number_of_input_blocks:
    #     blocks_used += blocks_in_current_layer
    #     print(f'Blocks used: {blocks_used}')
    #    along_edge_of = (blocks_in_current_layer + 1) * (blocks_in_current_layer + 1) # 2 + 2
    #     # print(blocks_used)
    #     print(f'Blocks in current layer: {blocks_in_current_layer}')
    #     break



print(calculate_leftover_blocks(10) == 1)