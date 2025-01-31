import numpy as np

def dice_stimulator():

    num_rolls = 1000    # Number of rolls
    rolls = np.random.randint(1, 7, num_rolls)  # 1000 random rolls

    unique, counts = np.unique(rolls, return_counts=True)
    probabilties = counts / num_rolls 

    for num, prob in zip(unique, probabilties):
        print(f"The probability of getting {num} is {prob: .2%}")

if __name__ == '__main__':
    dice_stimulator()